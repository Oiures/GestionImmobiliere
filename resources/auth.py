import json
import sqlite3

from flask import request, Response, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def hash_password(password):
    password = generate_password_hash(password).decode('utf8')
    return password


def check_password(pw, password):
    return check_password_hash(pw, password)


class SignupApi(Resource):

    def post(self):
        r = request.get_json()

        user_lname = r.get('lname')
        user_fname = r.get('fname')
        user_birthday = r.get('birthday')
        user_email = r.get('email')
        user_password = hash_password(r.get('password'))

        query = u"INSERT INTO users (user_lname, user_fname, user_birthday, user_email, user_password) VALUES " \
                "('" + user_lname + "', '" + user_fname + "', '" + user_birthday + "', '" + user_email + "', '" \
                + user_password +"');"

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        cur.execute(query).fetchall()

        conn.commit()

        return {'user_id': str(cur.lastrowid)}, 200


class LoginApi(Resource):

    def post(self):
        r = request.get_json()

        user_email = r.get('email')
        user_password = r.get('password')

        query = "SELECT user_password, user_id FROM users WHERE"
        to_filter = []

        if user_email:
            query += ' user_email=?;'
            to_filter.append(user_email)
        else:
            return 404

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        results = cur.execute(query, to_filter).fetchall()
        results_password = results[0]["user_password"]
        results_id = results[0]["user_id"]

        authorized = check_password(str(results_password), user_password)
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(results_id), expires_delta=expires)
        return {'token': access_token}, 200

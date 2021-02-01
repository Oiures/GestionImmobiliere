from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class UsersApi(Resource):

    @jwt_required
    def get(self):
        query_parameters = request.args

        user_id = query_parameters.get('id')
        user_lname = query_parameters.get('lname')
        user_fname = query_parameters.get('fname')
        user_birthday = query_parameters.get('birthday')
        user_email = query_parameters.get('email')

        query = "SELECT * FROM users WHERE"
        to_filter = []

        if user_id:
            query += ' user_id=? AND'
            to_filter.append(user_id)
        if user_lname:
            query += ' user_lname=? AND'
            to_filter.append(user_lname)
        if user_fname:
            query += ' user_fname=? AND'
            to_filter.append(user_fname)
        if user_birthday:
            query += ' user_birthday=? AND'
            to_filter.append(user_birthday)
        if user_email:
            query += ' user_email=? AND'
            to_filter.append(user_email)

        if query_parameters:
            query = query[:-4] + ';'
        else:
            query = query[:-6] + ';'

        print("#### " + str(query))

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_users = cur.execute(query, to_filter).fetchall()

        return jsonify(all_users)

    @jwt_required
    def post(self):
        r = request.get_json()

        user_lname = r.get('lname')
        user_fname = r.get('fname')
        user_birthday = r.get('birthday')

        query = u"INSERT INTO users (user_lname, user_fname, user_birthday) VALUES " \
                "('" + user_lname + "', '" + user_fname + "', '" + user_birthday + "');"

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query).fetchall()

        conn.commit()

        return {'user_id': str(cur.lastrowid)}, 200

class UserApi(Resource):

    @jwt_required
    def get(self, user_id):
        query = "SELECT * FROM users WHERE"
        to_filter = []

        if user_id:
            query += ' user_id=?;'
            to_filter.append(user_id)
        else:
            return 404

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        return jsonify(results), 200

    @jwt_required
    def put(self, user_id):
        r = request.get_json()

        user_lname = r.get('lname')
        user_fname = r.get('fname')
        user_birthday = r.get('birthday')

        query = 'UPDATE users SET '
        to_filter = []

        if user_lname is not None:
            query += 'user_lname=?, '
            to_filter.append(user_lname)
        if user_fname is not None:
            query += 'user_fname=?, '
            to_filter.append(user_fname)
        if user_birthday is not None:
            query += 'user_birthday=?, '
            to_filter.append(user_birthday)

        query = query[:-2] + 'WHERE user_id=' + str(user_id) + ';'

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        conn.commit()

        return {'user_id': str(user_id)}, 200

    @jwt_required
    def delete(self, user_id):
        query = 'DELETE FROM users WHERE '
        to_filter = []

        query += 'user_id=? ;'
        to_filter.append(user_id)

        conn = sqlite3.connect('./database/ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        conn.commit()

        return {'user_id': str(user_id)}, 200
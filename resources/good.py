from flask import Flask, request, jsonify
from flask_restful import Resource
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class GoodsApi(Resource):

    def get(self):
        conn = sqlite3.connect('ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_goods = cur.execute('SELECT * FROM goods;').fetchall()

        return jsonify(all_goods)

    def post(self):
        r = request.get_json()

        good_name = r.get('name')
        good_description = r.get('description')
        good_city = r.get('city')
        good_type = r.get('type')
        good_rooms = str(r.get('rooms'))
        good_feature = r.get('feature')
        user_id = str(r.get('owner'))

        query = u"INSERT INTO goods (good_name, good_description, good_city, good_type, good_rooms, " \
                "good_feature, user_id) VALUES " \
                "('" + good_name +"', '" + good_description + "', '" + good_city + "', '" + good_type + "', " + good_rooms + \
                ", '" + good_feature + "', " + user_id +");"

        conn = sqlite3.connect('ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query).fetchall()

        conn.commit()

        return jsonify(results)


class GoodApi(Resource):

    def get(self, good_id):
        query = "SELECT * FROM goods WHERE"
        to_filter = []

        if good_id:
            query += ' good_id=?;'
            to_filter.append(good_id)
        else:
            return 404

        conn = sqlite3.connect('ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        return jsonify(results)

    def put(self, good_id):
        r = request.get_json()

        good_name = r.get('name')
        good_description = r.get('description')
        good_city = r.get('city')
        good_type = r.get('type')
        good_rooms = str(r.get('rooms'))
        good_feature = r.get('feature')
        user_id = str(r.get('owner'))

        query = 'UPDATE goods SET '
        to_filter = []

        if good_name is not None:
            query += 'good_name=?, '
            to_filter.append(good_name)
        if good_description is not None:
            query += 'good_description=?, '
            to_filter.append(good_description)
        if good_city is not None:
            query += 'good_city=?, '
            to_filter.append(good_city)
        if good_type is not None:
            query += 'good_type=?, '
            to_filter.append(good_type)
        if good_rooms is not None:
            query += 'good_rooms=?, '
            to_filter.append(good_rooms)
        if good_feature is not None:
            query += 'good_feature=?, '
            to_filter.append(good_feature)
        if user_id is not None:
            query += 'user_id=?, '
            to_filter.append(user_id)

        query = query[:-2] + 'WHERE good_id=' + str(good_id) + ';'

        conn = sqlite3.connect('ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        conn.commit()

        return jsonify(results)

    def delete(self, good_id):
        query = 'DELETE FROM goods WHERE '
        to_filter = []

        query += 'good_id=? ;'
        to_filter.append(good_id)

        conn = sqlite3.connect('ImmobCatalogue.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        conn.commit()

        return jsonify(results)
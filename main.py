import json

from flask import Flask, url_for, request, render_template, jsonify, session, redirect, make_response
from markupsafe import escape
import sqlite3

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


"""@app.route('/')
def index():
    ## Cookie
    #username = request.cookies.get('username')
    #resp = make_response(render_template(...))
    #resp.set_cookie('username', 'the username')
    #return resp
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))"""


@app.route('/api/v1/resources/goods/all', methods=['GET'])
def api_goods_all():
    conn = sqlite3.connect('ImmobCatalogue.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_goods = cur.execute('SELECT * FROM goods;').fetchall()

    return jsonify(all_goods)


@app.route('/api/v1/resources/goods', methods=['GET'])
def api_goods_filter():
    query_parameters = request.args

    good_id = query_parameters.get('id')
    good_type = query_parameters.get('type')
    good_city = query_parameters.get('city')
    good_rooms = query_parameters.get('rooms')
    user_id = query_parameters.get('owner')

    query = "SELECT * FROM goods WHERE"
    to_filter = []

    if good_id:
        query += ' good_id=? AND'
        to_filter.append(good_id)
    if good_type:
        query += ' good_type=? AND'
        to_filter.append(good_type)
    if good_city:
        query += ' good_city=? AND'
        to_filter.append(good_city)
    if good_rooms:
        query += ' good_rooms=? AND'
        to_filter.append(good_rooms)
    if user_id:
        query += ' user_id=? AND'
        to_filter.append(user_id)
    if not (good_id or good_type or good_city or good_rooms or user_id):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('ImmobCatalogue.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/resources/goods', methods=['POST'])
def api_goods_add():
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

"""@app.route('/movies/<int:index>', methods=['PUT'])
def api_goods_update(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def api_goods_delete(index):
    movies.pop(index)
    return 'None', 200"""


@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_users_all():
    conn = sqlite3.connect('ImmobCatalogue.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM users;').fetchall()

    return jsonify(all_users)


@app.route('/api/v1/resources/users', methods=['GET'])
def api_users_filter():
    query_parameters = request.args

    user_id = query_parameters.get('id')
    user_lname = query_parameters.get('lname')
    user_fname = query_parameters.get('fname')
    user_birthday = query_parameters.get('birthday')

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
    if not (user_id or user_lname or user_fname or user_birthday):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('ImmobCatalogue.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#### Fonctions pour les defs


def get_all_users():
    pass


def get_current_user():
    pass


"""#### Pour verifier les URL avec le shell Python
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('api_users_filter', username='John Doe'))

with app.test_request_context('/login', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/login'
    assert request.method == 'GET'"""
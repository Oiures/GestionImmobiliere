from flask import Flask, render_template
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

"""# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'"""


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

initialize_routes(api)
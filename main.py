from flask import Flask
from flask import request
from model import user
import config
from utility import guid
from utility.regex import is_email
from hashlib import md5
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Vela!'

@app.route('/user/register', methods=['POST'])
def user_register():
    if request.form['email'].strip() and request.form['password'] and request.form['nickname'].strip():
        user_email = request.form['email'].strip()
        user_password = request.form['password']
        user_nickname = request.form['nickname'].strip()
        if is_email(user_email):
            exist_user = user.User(config.db, {'email': user_email})
            if exist_user.password:
                ec = 1062
                em = 'Email already exists'
            else:
                user_id = guid.new('user')
                new_user = user.User(config.db, {'id': user_id})
                m = md5()
                m.update(request.form['password'])
                new_user.password = m.hexdigest()
                new_user.email = user_email
                new_user.nickname = user_nickname
                new_user.save()
                ec = 200
                em = 'ok'
        else:
            ec = 417
            em = 'Invalid email'
    try:
        2 < 1
    except:
        ec = 500
        em = 'Post data error'
    return json.dumps({'ec': ec, 'em': em})

@app.route('/user/login', methods=['POST'])
def user_login():
    user.register()

@app.route('/user/logout', method=['POST'])
def user_logout():
    user.login()
    
@app.route('/content/create', method=['POST'])
def content_create():
    content.create()
    
@app.route('/content/delete/<id>', method=['POST'])
def content_delete(id):
    content.delete(id)
    
@app.route('/content/upload', method=['GET','POST'])
def upload_file():
    content.upload()
    
@app.route('/snap/create', method=['POST'])
def snap_create():
    sanp.create()
    
@app.route('/route/create', method=['POST'])
def route_create():
    route.create()

@app.route('/vela/create', method=['POST'])
def vela_create():
    vela.create()


    


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

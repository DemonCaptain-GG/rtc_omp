from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    return f'name={name},pwd={pwd}'

@app.route('/tem')
def hallo_world():
    return render_template("index.html")

@app.route('/Buried-sdk')
def buried_sdk():
    id = request.values.get("id")
    return f"""
    <form action="/login">
        账号：<input name="name" value="{id}"><br>
        密码：<input name="pwd">
        <input type="submit">
    </form>
    """


if __name__ == '__main__':
    app.run()

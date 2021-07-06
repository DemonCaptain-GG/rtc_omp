from flask import Flask
from flask import request
from flask import render_template
import utils
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/login')
def login():
    name = request.values.get("name")
    pwd = request.values.get("pwd")
    return f'name={name},pwd={pwd}'

@app.route('/tem')
def hallo_world():
    return render_template("index.html")

@app.route('/time')
def gettime():
    return utils.get_tim()


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

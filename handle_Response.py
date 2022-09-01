from flask import Flask, jsonify, render_template, make_response

app = Flask(__name__)


# 返回元组
@app.route("/tuple")
def tuple_result():
    return "你好呀", 200, {"mjj": "ad"}


# 返回文本
@app.route("/text")
def get_text():
    return "文本信息"


# 返回字典，返回dict会直接转换成json
@app.route("/dict")
def get_dict():
    return {"status": 0}


# 返回json
@app.route("/json")
def get_json():
    return jsonify({"status": 0})


# 返回html页面
@app.route("/html")
def get_html():
    return render_template('demo.html')


# 设置额外
@app.route("/")
def index():
    resp=make_response(render_template("demo.html"))
    #设置cookie
    resp.set_cookie("username","the username")
    #设置响应头信息
    resp.headers["hongwarts"]="ad2"
    return resp

if __name__ == '__main__':
    app.run()

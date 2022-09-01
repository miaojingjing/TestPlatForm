from flask import Flask
from log_util import logger
# 需要导入request 对象，不是requests！！！
from flask import request

app = Flask(__name__)


# args
@app.route("/login", methods=["get"])
def login():
    logger.info(f"请求参数为：{request.args}")
    result = request.args
    a = result.get("a")
    b = result.get("b")
    print(f"a={a},b={b}")
    return {"code": 0, "msg": "get success"}


# json
@app.route("/regist/", methods=["post"])
def post_regist():
    logger.info(f"请求参数为：{request.json}")
    return {"code": 0, "msg": "post success"}


# form表单
# 注册，用户名、密码、邮箱
@app.route("/regist1/", methods=["put"])
def put_regist_form():
    name = request.form.get("name")
    pwd = request.form.get("pwd")
    logger.info(f"请求参数为：{request.form}")
    logger.info(f"name:{name},pwd:{pwd}")
    return {"code": 0, "msg": "put  form success"}


# 处理前端发来的文件请求
@app.route("/file", methods=["post"])
def file():
    fileObj = request.files.get("file")
    filename = fileObj.filename
    logger.info(f"文件名为：{filename}")
    fileObj.save("./logo.png")
    return {"code": 0, "msg": "post  file success"}


if __name__ == '__main__':
    app.run()

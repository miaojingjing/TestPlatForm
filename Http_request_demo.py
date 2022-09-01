from flask import Flask
from log_util import logger

app = Flask(__name__)

# get 请求
# methods 是一个列表类型，可以添加多种请求方式，get post put delete ...
@app.route('/testcase',methods=["get"])
def get_case():
    logger.info("这是get方法")
    return {"code":0,"msg":"get success"}

# post 请求
@app.route('/testcase',methods=["post"])
def post_case():
    logger.info("这是post方法")
    return {"code":0,"msg":"post success"}

# put 请求
@app.route('/testcase',methods=["put"])
def put_case():
    logger.info("这是put方法")
    return {"code":0,"msg":"put success"}

# delete 请求
@app.route('/testcase',methods=["delete"])
def delete_case():
    logger.info("这是delete方法")
    return {"code":0,"msg":"delete success"}

if __name__ == '__main__':
    app.run()

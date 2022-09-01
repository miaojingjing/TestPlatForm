# 1、导入flask模块
from flask import Flask

# 2、创建flask应用程序的实例，通过传递一个参数
# 当运行当前模块的时候，__name__==__main__ 如果是其他模块调用当前模块，此name就是当前模块的名字。
# flask底层会根据传的参数来确定编写的程序的根目录，通过根目录来获取到静态文件和模板文件的目录
# 此时，app就是flask的实例对象，通过这个实例对象
from log_util import logger

app = Flask(__name__)


# 装饰器，通过装饰器可以来改变一个普通函数，给他增加一些功能
# 这边的功能就是在root里面给传递了一个url,即路由。当定义了路由之后，就可以在浏览器里通过路由给我们后端服务器发送一个请求，
# 后端服务接收到请求后，就会把请求映射到方法上（比如这边的hello_world），然后去执行方法的代码，将结果返回到前端
# 例如：https://www.baidu.com/baidu?tn=monline_4_dg&ie=utf-8&wd=%E8%85%BE%E8%AE%AF%E8%AF%BE%E5%A0%82
#    https  ----协议
#    www.baidu.com---host 域名
#    /baidu 路由
#   tn=monline_4_dg&ie=utf-8&wd=%E8%85%BE%E8%AE%AF%E8%AF%BE%E5%A0%82   --请求参数
@app.route("/")
def hello_root():
    return "<p>Hello, World!</p >"


@app.route("/demo")
def hello_demo():
    return "<p>Hello, Tester!这是一个demo</p >"


# 动态路由 + 类型限定
@app.route('/user/<int:username>')
def dynamic_route(username):
    logger.info(f"这是一个动态路由，是{username} 同学的个人信息")
    return f"这是一个动态路由，是{username} 同学的个人信息"


# 启动入口
if __name__ == '__main__':
    # flask  服务启动起来，启动起来，这个服务一致在，轮询等待的方式，等待浏览器发来的请求，会一致接受请求，直到请求结束。
    # ctrl + C 无法停止，只有点击左侧的停止按钮
    app.run()

# 运行方式(两种)
# 一、运行方式 --- 代码调用
# if __name__ == '__main__':
#     app.run()

# 二、运行方式  命令行
# 1、bash(mac/linux)
# $ export FLASK_APP=mini_flask_demo
# $ flask run

# 2、cmd(windows)
# > set FLASK_APP=mini_flask_demo
# > flask run

# 3、 powershell(windows)
# $env:FLASK_APP=mini_flask_demo
# > flask run

from flask import Flask
from flask_restx import Resource, Api,Namespace
# Namespace 可以对接口进行分类

app = Flask(__name__)

# 创建Api实例对象
api = Api(app)

# 定义了两个命名空间Namespace
demo_ns=Namespace("demo",description='Demo的模块')
case_ns=Namespace("case",description='TestCase的模块')

# 添加路由(方式一、装饰器)
# @api.route('/hello','/mjj')

#这边定义的是子路由,如果没有，就传空 将@api.route('/hello')改成@demo_ns.route("")
@demo_ns.route("")
# 类要继承Resource模块
class Demo(Resource):
    # restful风格的get方法
    def get(self):
        return {'hello': 'world'}

    # restful风格的post方法
    def post(self):
        return {'post': 'world'}

    # restful风格的post方法
    def put(self):
        return {'put': 'world'}

    # restful风格的post方法
    def delete(self):
        return {'delete': 'world'}
#(方式二、api.add_resource)
#api.add_resource(Demo,'/hello')

#这边定义的是子路由
@case_ns.route("")
class TestCase(Resource):
    # restful风格的get方法
    def get(self):
        return {'hello': 'world'}

    # restful风格的post方法
    def post(self):
        return {'post': 'world'}

    # restful风格的post方法
    def put(self):
        return {'put': 'world'}

    # restful风格的post方法
    def delete(self):
        return {'delete': 'world'}
#(方式二、api.add_resource)
#api.add_resource(TestCase,'/case')

#这边定义的是路由
api.add_namespace(demo_ns,'/hello')
api.add_namespace(case_ns,'/mjj')
if __name__ == '__main__':
    app.run(debug=True)

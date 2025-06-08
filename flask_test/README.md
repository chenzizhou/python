1、创建虚拟环境
pip install virtualenv 
virtualenv venv 
venv/Script/activate #激活
venv/Script/deactivate #退出
2、安装依赖环境
pip install -r requirements.txt 
3、创建flask应用
app=Flask(__name__)
app.config.from_object(config)
4、路由自上而下匹配
不带/表示唯一，带有/斜杆表示重定向
路由规则
@app.route(url='',method=[])
url格式如下：
/<float:value>
/<int:value>
/<str:value>
/<path:value>
/<uuid:value>  16个字符组成
def func(value)
5、请求对象 request
request.full_path 获取完整路径，包括后面参数 /xx/xx/xx?xx=xx&xx=xx
request.path 获取路径，没有参数 /xx/xx/xx
request.url 获取请求地址
request.heades 获取请求头
request.args 获取路径中的参数值(返回字典）
request.form 获取post请求（返回字典）
5、响应对象 response
response.setcookies
6、jinja2 模板引擎
render_temple
请求》路由》匹配对应函数》模板引擎从template找到对应html文件》转成字符串》return返回给浏览器
模板传参
根据html形参确定传参
render_temple('xxx.html',参数)
7、flask—script
8、flask-sqlalchemy
orm映射
类 表
属性 字段
对象 一条数据
9、flask-migrate 数据迁移
flask --app hello db init 初始化
flask --app hello db migrate 对比初始化生成变更脚本
flask --app hello db upgrade 执行变更脚本，同步当前模型和数据库


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
db.init(app) 数据库关联应用
db.create_all() 创建表
9、flask-migrate 数据迁移
flask --app hello db init 初始化，产生一个文件夹migrations
flask --app hello db migrate 对比初始化生成变更脚本
flask --app hello db upgrade 执行变更脚本，同步当前模型和数据库
flask --app hello db downgrade 数据库降级

查询
model.query.filter_by(col=value) 里面是一个等值         类似where col==value
model.query.filter_by(col=value).first() --对象        类似where col==value limit 1
model.query.filter(model.col==value) 里面是布尔条件     类似where col==value
模糊查询
model.query.filter(model.col.startwith(value)).all()   类似like
model.query.filter(model.col.endwith(value)).all()     类似like
model.query.filter(model.col.contains(value)).all()    类似like
model.query.filter(model.col.like('%value')).all()     类似like
model.query.filter(or_(model.col==value,model.col==value).all()     类似 where col==value or col==value
model.query.filter(and_(model.col==value,model.col==value).all()    类似 where col==value and col==value
model.query.filter(not_(model.col==value,model.col==value).all() 
model.query.filter(and_(model.col==value,model.col.__lt__(value)).all()    类似 where col==value and col<value

model.query.filter(and_(model.col==value,model.col.<value).all()  类似 where col between value1 and value2
model.query.between()/model.query.filter(model.col.be())
__lt__()/__gt__()/__le__()/__gt()__/in_([,,,])/be() 用法类似
or_()/and_()/not_() 用法类似
model.query.all() --列表

排序
model.query.filter_by(col=value).order_by(col1).all() 对所有升序排列
model.query.filter_by(col=value).order_by(col1).order_by(-model.col).all()
order_by(参数)  参数：1、字符串‘字段名’ ，但是不能倒序 order_by('col') 2、填字段名：模型.字段  order_by(-moder.col)

限制：limit
model.query.order_by(col1).limit(2).all()  拿到12
model.query.offset(2).order_by(col1).limit(2).all() 拿到34

9、加密 hashlib
hashlib.md5(vlaue.encode('utf-8')).hexdigest()
md5  32位 16进制
sha1 40位
sha256 64位 
sha512 128位


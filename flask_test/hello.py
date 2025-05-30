import os

from flask import Flask, redirect, request, jsonify, render_template, abort, url_for, make_response, session
from flask_cors import CORS
from flask_mail import Message
from flask_migrate import Migrate
from markupsafe import escape
from werkzeug.utils import secure_filename

from blueprints.platform import bp_platform
from blueprints.register import bp_register
from blueprints.update import bp_update_platform
import config
from exts import db, mail
from blueprints.login import bp_login

app = Flask(__name__)  # 实例化一个Flask对象
CORS(app)  # 解决跨域问题
app.config.from_object(config)
db.init_app(app)  # 初始化数据库
mail.init_app(app)  # 初始化邮件
# 主要逻辑：
# Migrate(app, db)：这是一个构造函数，用于创建一个Migrate对象。其中，app是Flask应用的实例，db是SQLAlchemy数据库的实例。这个构造函数会将Flask应用和数据库实例绑定到一起，以便于后续的数据库迁移操作。
# migrate = Migrate(app, db)：这行代码将创建的Migrate对象赋值给变量migrate，后续的数据库迁移操作可以通过这个变量进行。
migrate = Migrate(app, db)  # 初始化迁移命令
print('实例路径', app.instance_path)  # D:\python-main\flask_test\instance
app.register_blueprint(bp_login, url_prefix='/login')  # 注册蓝图
app.register_blueprint(bp_register, url_prefix='/register')
app.register_blueprint(bp_platform, url_prefix='/platform')
app.register_blueprint(bp_update_platform, url_prefix='/update')


# @app.route('/update/<platform>', methods=['GET', 'POST'])
# def update_account(platform):
#     form = AccountForm()
#     form.platform.validators = [InputRequired("平台不能为空")]
#     form.platform.render_kw = {'readonly': True}
#     try:
#         conn = sqlite3.connect('database.db')
#         cur = conn.cursor()
#         if form.validate_on_submit():
#             print(form.account.data, form.password.data, platform)
#             cur.execute("UPDATE password_manager SET account=?,password=? where platform=?", (form.account.data,
#                                                                                               form.password.data,
#                                                                                               platform))
#             cur.execute('select * from password_manager')
#             data = cur.fetchall()
#             conn.commit()
#             return render_template('platform.html', data=data)
#         else:
#             cur.execute(
#                 'select * from password_manager where platform=?', (platform,))
#             form.platform.data, form.account.data, form.password.data = cur.fetchone()
#             conn.commit()
#     except:
#         conn.rollback()
#     finally:
#         cur.close()
#         conn.close()
#     return render_template('update.html', form=form)
#
#
# @app.route('/delete', methods=['GET', 'POST'])
# def delete_account():
#     form = AccountForm()
#     data = []
#     try:
#         conn = sqlite3.connect('database.db')
#         cur = conn.cursor()
#         platform = request.args.get("platform")
#         cur.execute("delete from password_manager where platform=?", (platform,))
#         cur.execute('select * from password_manager')
#         data = cur.fetchall()
#         conn.commit()
#     except Exception as e:
#         print(e)
#     finally:
#         cur.close()
#         conn.close()
#     return render_template('platform.html', data=data)
#
# '''路由是 URL 到 Python 函数的映射。Flask 允许你定义路由，使得当用户访问特定 URL 时，Flask 会调用对应的视图函数来处理请求'''
@app.route('/')
def index():
    return redirect('/login')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')  # 将文件保存到指定路径


@app.route('/api/axios')
def get_data():
    data = {'message': 'nihao'}
    return jsonify(data)  # 将字典转换为json格式


@app.route('/mail', methods=['GET'])
def send_mail():
    email = request.args.get('email')
    print(email)
    msg = Message('Hello', sender='ohusage@huawei.com', recipients=[email], body='hello')
    mail.connect()
    mail.send(msg)


# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     data = {}
# #     form = LoginForm()
# #     # 判断点击提交,提取表单数据
# #     if form.validate_on_submit():
# #         try:
# #             data['name'] = form.name.data
# #             data['password'] = form.password.data
# #             # 验证用户名是否存在数据
# #             # 验证密码是否正确
# #             conn = sqlite3.connect('database.db')
# #             cur = conn.cursor()
# #             cur.execute('select * from password_manager')
# #             data = cur.fetchall()
# #             print(data)
# #         except:
# #             conn.rollback()
# #         finally:
# #             cur.close()
# #             cur.close()
# #         return render_template('platform.html', data=data)
# #     return render_template('index.html', form=form, data=data)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return 'hello world'

# 视图函数是处理请求并返回响应的 Python 函数。它们通常接收请求对象作为参数，并返回响应对象，或者直接返回字符串、HTML 等内容。
@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', name=username)


# '''限制请求传参类型'''
@app.route('/post/<int:post_id>')
def show_post(post_id):
    if post_id == 10:
        content = '1234'
    else:
        content = '5678'
    return 'id {} 内容为：{}'.format(post_id, content)


# '''通过函数名及函数参数来确定访问url'''
@app.route('/url')
def get_url():
    return url_for('show_post', post_id=10)


# '''重定向访问地址'''
@app.route('/redirect_url')
def redirect_url():
    return redirect(url_for('show_post', post_id=10))


# 响应对象包含了发送给客户端的响应信息，包括状态码、响应头和响应体。Flask 默认会将字符串、HTML 直接作为响应体。
# make_response：创建一个自定义响应对象，并设置响应头 X-Custom-Header。
@app.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response!')
    response.headers['X-Custom-Header'] = 'Value'
    return response
# Flask 使用客户端会话来存储用户信息，以便在用户浏览应用时记住他们的状态。会话数据存储在客户端的 cookie 中，并在服务器端进行签名和加密。
@app.route('/set_session/<username>')
def set_session(username):
    session['username'] = username
    return f'Session set for {username}'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    return f'Hello, {username}!' if username else 'No session data'

@app.route('/test')
def test():
    value = '<script>alert("bad!")</script>'
    return f'{escape(value)}'


with app.test_request_context():
    # print(url_for('index'))
    # print(url_for('test'))
    db.create_all()  # 创建所有在当前上下文中定义的模型对应的表

# @app.route('/401')
# def login():
#     abort(401)
#     this_is_never_executed()


if __name__ == "__main__":
    # 参数说明
    # host：设置监听地址，默认为127.0.0.1（只能本机访问），设置为0.0.0.0后，可以被其它机器访问
    # port：设置监听端口，默认为5000
    # debug：是否开启调试模式，True表示开启，开启后，修改代码后，不需要重启服务器，服务器会自动重启
    # load_dotenv：是否加载环境变量，True表示加载，加载后，可以在代码中使用os.environ获取环境变量
    # use_reloader：是否使用重载器，True表示使用，使用后，修改代码后，不需要重启服务器，服务器会自动重启（和debug类似，但use_reloader更通用）
    # threaded：是否开启线程，True
    # processes：设置进程数，默认为1，设置为0时，会根据CPU核心数自动设置
    app.run(debug=True, use_reloader=True)

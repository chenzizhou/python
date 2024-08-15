import os

from flask import Flask, redirect, request, jsonify, render_template
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

app = Flask(__name__)
CORS(app)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)
print(app.instance_path)
app.register_blueprint(bp_login, url_prefix='/login')
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
        return render_template('upload.html')


@app.route('/api/axios')
def get_data():
    data = {'message': 'nihao'}
    return jsonify(data)


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
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return render_template('user.html', name=username)
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     if post_id == 10:
#         content = '1234'
#     else:
#         content = '5678'
#     return 'id {} 内容为：{}'.format(post_id, content)
#
#
# @app.route('/url')
# def get_url():
#     return url_for('show_post', post_id=10)
#
#

#
#
# @app.route('/test')
# def test():
#     value = '<script>alert("bad!")</script>'
#     return f'{escape(value)}'


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('test'))


# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

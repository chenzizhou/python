import sqlite3

from flask import Blueprint, render_template, Flask, session, request, redirect, url_for, app
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from models import UserModel


def check_login(form, field):
    print(field.data, form.password.data)
    # 验证用户名是否存在数据
    user = UserModel.query.filter_by(username=form.username.data).all()
    print(user, '------------------')
    if field.name == 'username':
        if len(user):
            print('用户名存在')
            print('字段名称为:{}'.format(field.name))
        else:
            raise ValidationError('用户名不存在')
    if field.name == 'password':
        print('字段名称为:{}'.format(field.name))
        if len(user) == 0:
            pass
        else:
            print('用户信息为：{}'.format(user))
            print('用户信息为：{}'.format(user[0].password))
            if check_password_hash(form.password.data, user[0].password):
                raise ValidationError('密码错误')
            else:
                print('用户ID为：{}'.format(user[0].id))
                session['user_id'] = user[0].id


class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[InputRequired("用户名不能为空"), check_login])
    password = PasswordField(label='密　码', validators=[InputRequired("密码不能为空"), check_login])
    submit = SubmitField(label="提交", render_kw={'style': 'background:green;'})


bp_login = Blueprint('login', __name__)


# @bp_login.route('/')
# def hello():
#     return 'Hello, World!'
@bp_login.route('/', methods=['GET', 'POST'])
def login():
    platforms = {}
    form = LoginForm()
    # 判断点击提交,提取表单数据
    if form.validate_on_submit():
        return redirect(url_for('platform.platform_page'))
    return render_template('user/index.html', form=form, data=platforms)

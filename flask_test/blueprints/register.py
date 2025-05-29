from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash
from wtforms import ValidationError, StringField, PasswordField, SubmitField, DateField, DateTimeField
from wtforms.validators import InputRequired
from exts import db
from models import UserModel


def check_login(form, field):
    print(field.data, form.password.data)
    if field.name == 'username':
        # 验证用户名是否存在数据
        user = UserModel.query.filter_by(username=form.username.data).all()
        print(user, '------------')
        if len(user) == 0:
            print('用户名不存在')
            if field.name == 'password':
                user = UserModel.query.filter_by(username=field.data).filter_by(password=form.password.data).all()
                if user is None:
                    raise ValidationError('密码错误')
        else:
            raise ValidationError('用户名已存在')


class Register(FlaskForm):
    username = StringField(label='用户名', validators=[InputRequired("用户名不能为空"), check_login],
                           render_kw={'placeholder': '输入用户名'})
    password = PasswordField(label='密　码', validators=[InputRequired("密码不能为空"), check_login],
                             render_kw={'placeholder': '输入密码'})
    email = StringField(label='邮 箱', validators=[InputRequired("邮箱不能为空")],
                        render_kw={'placeholder': '输入邮箱'})  # , Email('邮箱格式错误')
    # join_time = DateTimeField(label="添加时间", default=datetime.now())
    submit = SubmitField(label="提交")


bp_register = Blueprint('register', __name__)


@bp_register.route('/', methods=['GET', 'POST'])
def register_page():
    data = {}
    form = Register()
    if form.validate_on_submit():
        print([i for i in request.form.values()])
        print('添加用户')
        user1 = UserModel(username=form.username.data, password=generate_password_hash(form.password.data),
                          email=form.email.data)
        # 增加用户到数据库
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login.login'))
    return render_template('user/register.html', form=form)

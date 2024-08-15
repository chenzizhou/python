from flask import Blueprint, session, request, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

from exts import db
from models import PlatformModel, UserModel


def check_platform(form, field):
    platforms = PlatformModel.query.filter_by(platform=field.data,user_id=session.get('user_id')).all()
    print(platforms, '----------------------')

    if platforms:
        raise ValidationError('平台已存在')


class PlatformForm(FlaskForm):
    platform = StringField(label='平台', validators=[InputRequired("平台不能为空"), check_platform])
    account = StringField(label='账号', validators=[InputRequired("账号不能为空")])
    password = PasswordField(label='密码', validators=[InputRequired("密码不能为空")])
    submit = SubmitField(label="提交",render_kw={'style':'background:green;'})


bp_platform = Blueprint('platform', __name__)


@bp_platform.before_request
def check_auth():
    if session.get('user_id', None) is not None:
        print('success')
    else:
        return redirect(url_for('login.login'))


@bp_platform.route('/', methods=['GET', 'POST'])
def platform_page():
    try:
        platforms = sorted(UserModel.query.get(session.get('user_id')).platforms,key=lambda x:x.platform)
        print(platforms, '---------------------------')
    except Exception as e:
        print(e)
    return render_template('platform/platform.html', platforms=platforms)


@bp_platform.route('/delete', methods=['GET', 'POST'])
def delete_platform():
    print('删除{}'.format(request.args.get('id')))
    # 删除 id 为1的平台记录
    platform = PlatformModel.query.get(request.args.get('id'))
    db.session.delete(platform)
    db.session.commit()
    return redirect(url_for('platform.platform_page'))


@bp_platform.route('/add', methods=['GET', 'POST'])
def add_platform():
    form = PlatformForm()
    # form.account.data=''
    # form.password.data=''
    # 验证平台是否存在数据库
    if form.validate_on_submit():
        platform = PlatformModel(platform=form.platform.data, account=form.account.data, password=form.password.data,
                                 user_id=session.get('user_id'))
        db.session.add(platform)
        platforms = PlatformModel.query.filter_by(user_id=session.get('user_id')).all()
        db.session.commit()
        return redirect(url_for('platform.platform_page'))
    else:
        return render_template('user/add.html', form=form)

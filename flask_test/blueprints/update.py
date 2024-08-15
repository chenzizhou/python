from flask import render_template, Blueprint, session, request

from blueprints.platform import PlatformForm
from exts import db
from models import PlatformModel

bp_update_platform = Blueprint('update_platform', __name__)


@bp_update_platform.route('/', methods=['GET', 'POST'])
def update_platform():
    form = PlatformForm()
    platform = PlatformModel.query.get(request.args.get('id'))
    form.platform.data = platform.platform
    form.account.data = platform.account
    form.password.data = platform.password
    return render_template('platform/update.html', form=form, platform=platform)

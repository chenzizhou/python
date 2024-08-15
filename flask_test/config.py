from datetime import timedelta

SECRET_KEY = 'nature'
DB_URI = 'sqlite:///database.db'
# 数据库连接信息
# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'TEST'
# USERNAME = 'root'
# PASSWORD = '123456'
# # DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACE_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SECRET_KEY = '123456'
PERMANENT_SESSION_LIFETIME = timedelta(hours=1)

# 邮箱配置
MAIL_SERVER = "smtp.huawei.com"
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'p_OHUsage'
MAIL_PASSWORD = 'Changeme_123'

# 平台配置
DEBUG = True

UPLOAD_FOLDER = 'upload/'
MAX_CONTENT_LENGTH = 1024000

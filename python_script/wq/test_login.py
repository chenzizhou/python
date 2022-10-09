from wq_user import User
from time import sleep

u = User()
u.login('admin', '123456')
sleep(5)
u.teardown_method()

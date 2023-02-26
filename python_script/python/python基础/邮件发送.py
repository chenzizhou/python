# 作者
# NATURE
# 日期
# 2023/2/19 11:54
# 功能
#
# 邮箱账号
import uuid as uuid
import zmail
username = '417753633@qq.com'
# 邮箱授权码，此处一定要注意，授权码不是邮箱密码，是要申请开通SMTP服务，官方给你的授权码
authorization_code = 'jdpdvalctttxbhdh'
# 构建一个邮箱服务对象
server = zmail.server(username, authorization_code)
# 邮件主体
# subject：是邮件的主题，此处一定要注意，主题每次发送邮件要不一致，不然邮件显示发送成功，
# 但是你是收不到邮件的，当初被坑了好久才解决，此处我用生成uuid来解决
uuid= uuid.uuid4()
message='你好'
mail_body = {
    'subject': f'(编号)',
    'content_text': message,  # 纯文本或者HTML内容,发送邮件的内容
    'attachments':['文件.py']
}
# 收件人
mail_to = '1096059759@qq.com'
try:
    # 发送邮件
    server.send_mail(mail_to, mail_body)
    print("发送成功")
except Exception as e:
    print(e)
    print("发送失败")


mail_all={
    'from_username':username,
    'authorization_code':'jdpdvalctttxbhdh',
    'send_to_username':'1096059759@qq.com',
    'subject': f'(编号)',
    'content_text': message,  # 纯文本或者HTML内容,发送邮件的内容 context_html
    'attachments':['文件.py']
 }
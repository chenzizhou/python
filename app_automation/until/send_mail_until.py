# 作者
# NATURE
# 日期
# 2023/2/19 12:43
# 功能
#

import uuid as uuid
import zmail


# #send_mail参数格式
# report_file=''#报告名称
# with open(report_file,'r',encoding='utf-8') as f:
#     message=f.read()
# mail_all={
#     'from_username':'417753633@qq.com',#发送人
#     'authorization_code':'jdpdvalctttxbhdh',#授权码
#     'send_to_username':['1096059759@qq.com'],#收件人
#     'subject': 'XX报告',#主题
#     'content_html':message,  # 纯文本或者HTML内容,发送邮件的内容 context_html
#     'attachments':['2022-12-21 14_06_52 result.html']# 附件,多个附件，以列表的形式存储
#  }
def send_mail(**kwargs):
    username = kwargs['from_username']
    # 邮箱授权码，此处一定要注意，授权码不是邮箱密码，是要申请开通SMTP服务，官方给你的授权码
    authorization_code = kwargs['authorization_code']
    # 构建一个邮箱服务对象
    server = zmail.server(username, authorization_code)
    # 邮件主体
    # subject：是邮件的主题，此处一定要注意，主题每次发送邮件要不一致，不然邮件显示发送成功，
    # 但是你是收不到邮件的，当初被坑了好久才解决，此处我用生成uuid来解决
    # uuid = uuid.uuid4()
    mail_body = {
        'subject': kwargs['subject'],
        'attachments': kwargs['attachments']
    }
    # 纯文本或者HTML内容,发送邮件的内容
    if 'content_html' in kwargs.keys():
        mail_body['content_html'] = kwargs['content_html']
    else:
        mail_body['content_text'] = kwargs['content_text']
    # 收件人
    mail_to = kwargs['send_to_username']
    try:
        # 发送邮件
        # recipients:收件人
        # mail：邮件内容
        # cc:抄送人
        server.send_mail(recipients=mail_to, mail=mail_body, cc='404830168@qq.com')
        print("发送成功")
    except Exception as e:
        print(e)
        print("发送失败")

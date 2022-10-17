# 作者
# NATURE
# 日期
# 2022/10/17 11:57
# 功能
#
#发送邮箱服务器
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    smtpserver='smtp.qq.com'
    #发送邮箱用户/密码
    user = '1096059759@qq.com'
    password = 'jjrrbaoauhpejcgf'
    #发送邮箱
    sender = '1096059759@qq.com'
    #接收邮箱
    receiver = '1096059759@qq.com'
    #发送邮件主题
    subject= '外勤登录'
    #编写HTML类型的邮件正文
    msg = MIMEText(mail_body,'html','utf-8 ')
    msg['Subject'] = Header (subject,'utf-8 ')
    #连接发送邮件
    smtp =smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import smtplib
from email.header import Header


def send_mail():
    send_from = '15309215554@163.com'
    send_to = '616387521@qq.com'
    subject = 'this is a python email'
    smtp_server = "smtp.163.com"
    username = "15309215554@163.com"
    passwd = "616387521"
    body = u'我就是想看看乱码'
    msg = MIMEText(body,'plain','utf-8')
    msg['from'] = send_from
    msg['to'] = send_to
    msg['subject'] = Header(subject,'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(username,passwd)
    smtp.sendmail(send_from,send_to,msg.as_string())
    smtp.quit()
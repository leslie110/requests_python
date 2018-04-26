# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
#发送邮箱
send_from = '15309215554@163.com'
#接收邮箱
send_to = '616387521@qq.com'
#邮箱服务器
send_server = 'smtp.163.com'
#邮箱登录账号密码
username = '15309215554@163.com'
password = '616387521'

#读取文件
file_name = r'C:\Users\Admin\Desktop\1111.py'
mail_body = open(file_name,'rb').read()

#编写邮箱
msgRoot = MIMEMultipart()
msgRoot['from'] = send_from
msgRoot['to'] = send_to
msgRoot['subject'] = "this is test email!"
#添加正文
body = MIMEText('<html><h1>这是一条带附件的邮件</h1></html>','html','utf-8')
msgRoot.attach(body)

#d读取附件
msg = MIMEText(mail_body,'base64','utf-8')
msg['Countent-Type'] = 'application/octet-stream'
msg['Countent-Disposition'] =  'attachment; filename="1111.py"'
msgRoot.attach(msg)

#发送邮件
smtp = smtplib.SMTP()
smtp.connect(send_server)
smtp.login(username,password)
smtp.sendmail(send_from,send_to,msgRoot.as_string())
smtp.quit()

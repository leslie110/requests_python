# -*- coding:utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

#定义邮箱
send_from = '15309215554@163.com'
send_to = '616387521@qq.com'
send_server = 'smtp.163.com'
#登录账号密码
username = '15309215554@163.com'
passwd = "616387521"
#定义附件
msgRoot = MIMEMultipart()
subject = u'附件发送'
msgRoot['Subject'] = Header(subject,'utf-8')
msgRoot['From'] = Header(send_from,'utf-8')
msgRoot['To'] = Header(send_to,'utf-8')
#这里是邮件正文
body = MIMEText(u'我才是最后重要的正文啊','plain','utf-8')
msgRoot.attach(body)
#这里是附件
dir = r"F:\download\requests_python\shaotest\report\result.html"
acc = MIMEText(open(dir,'rb').read(),'base64','utf-8')
acc.add_header('Content-Disposition','attachment',filename='result.html')
msgRoot.attach(acc)
#发送邮件
smtp = smtplib.SMTP()
smtp.connect(send_server)
smtp.login(username,passwd)
smtp.sendmail(send_from,send_to,msgRoot.as_string())
smtp.quit()

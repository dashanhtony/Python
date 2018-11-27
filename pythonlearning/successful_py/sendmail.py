
# -*- coding: utf-8 -*-
import smtplib
import time
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

timenow=time.strftime('%Y%m%d',time.localtime(time.time()))
filepath1='/home/bestpay/shellorder/'+str(timenow)+'_bak_success_179.23.txt'
filepath2='/home/bestpay/shellorder/'+str(timenow)+'_bak_success_179.24.txt'
filepath3='/home/bestpay/shellorder/'+str(timenow)+'_bak_success_179.25.txt'
filepath4='/home/bestpay/shellorder/'+str(timenow)+'_bak_success_164.2.txt'
with open(filepath1, 'r') as f1:
    message1=str(f1.read())
with open(filepath2, 'r') as f2:
    message2=str(f2.read())
with open(filepath3, 'r') as f3:
    message3=str(f3.read())
with open(filepath4, 'r') as f4:
    message4=str(f4.read())
message=message1+'\n'+message2+'\n'+message3+'\n'+message4
# 输入Email地址和口令:
from_addr = 'dashanthony@163.com' #input('From: ')
password = 'xxx' #input('Password: ')
# 输入收件人地址:
to_addr = ['yuning.syn@antfin.com'] #input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.163.com'

msg = MIMEText(message, 'plain', 'utf-8')
#发送邮箱地址
msg['From'] = from_addr
#收件箱地址
msg['To'] = ','.join(to_addr) #此处传入的参数为字符串
#主题
msg['Subject'] = 'database bak success'
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

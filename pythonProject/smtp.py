# for i in range(1,10):
#     for j in range(1,i+1 ):
#         print("{}*{}={} ".format(i,j,i*j),end='')
#     print()
import sys
import smtplib
from email.mime.text import MIMEText

# 设置默认编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')

msg_from = 'panjian1105@163.com'
pwd = 'ORPHGFCQHGCKEYCI'    #授权码
to = '3133695439@qq.com'
subject = '这是python发送的'     #电子邮件的主题
content = 'hell0 world'     #电子邮件的内容

#构造邮件
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = 'Anonymous <panjian1105@163.com>'
msg['To'] = to
#发送邮件
try:
    ss = smtplib.SMTP_SSL('smtp.163.com', 465)
    ss.login(msg_from, pwd)
    ss.sendmail(msg_from, to, msg.as_string())
    print('发送成功')
except Exception as e:
    print('发送失败', e)

# from smtplib import SMTP
# from poplib import POP3
# from time import sleep

# SMTPSVR = 'smtp.qq.com'
# POP3SVR = 'pop.qq.com'

# origHdrs = ['From:panjian1105@163.com',
#             'To:3133695439@qq.com',
#             'Subject:这是python发送的']
# origBody = ['xxx', 'yyy', 'zzz']
# origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),
#                            '\r\n'.join(origBody)])

# sendSvr = SMTP(SMTPSVR)
# sendSvr.set_debuglevel(1)
# sendSvr.login("panjian1105", "ORPHGFCQHGCKEYCI")
# errs = sendSvr.sendmail('panjian1105@163.com',
#                         ('3133695439@qq.com',), origMsg)
# sendSvr.quit()
# assert len(errs) == 0, errs
# sleep(5)

# recvSvr = POP3(POP3SVR)
# recvSvr.user('3133695439')
# recvSvr.pass_('13037191340p')
# rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# sep = msg.index('')
# recvBody = msg[sep + 1:]
# assert origBody==recvBody
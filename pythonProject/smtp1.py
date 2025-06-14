from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello world!\r\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Failure is always a constant in life.</h4></body></html>', 'html'
    )
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()
    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"'% fn)
    return email

def sendMsg(fr, to, msg):
    s = smtplib.SMTP_SSL('smtp.163.com', 465)
    s.login(msg_from, pwd)
    errs = s.sendmail(fr, to, msg)
    s.quit()

if __name__== '__main__':
    msg_from = 'panjian1105@163.com'
    pwd = 'ORPHGFCQHGCKEYCI'  # 授权码
    # to = '3133695439@qq.com'
    to = "874639049@qq.com"
    subject = '您好'  # 电子邮件的主题

    print('sending multipart alternative msg...')
    # msg = make_mpa_msg()
    # msg['From'] = msg_from
    # msg['To'] = to
    # msg['Subject'] = subject
    # sendMsg(msg_from, to, msg.as_string())

    print('sending imag message')
    msg = make_img_msg('1.jpg')
    msg['From'] = 'PJ <panjian1105@163.com>'
    msg['To'] = to
    msg['Subject'] = '老板玩五子棋吗'
    sendMsg(msg_from, to, msg.as_string())


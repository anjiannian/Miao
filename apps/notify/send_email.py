# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText


SMTP_SERVER = 'smtp.aliyun.com'

_user = "wentao1988@aliyun.com"
# _user = "416936177@qq.com"
# _user = "yanwentao@viewayintl.com"
_pwd = "Yan28566477"
# _pwd = "ZhiMaKaiMeng2011"
_to = "416936177@qq.com"

# 使用MIMEText构造符合smtp协议的header及body
msg = MIMEText("乔装打扮，不择手段", )
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to


def send_email_txt(to_list, sub, content):
    msg = MIMEText(content, "pain", "utf-8")
    msg["Subject"] = sub
    msg["From"] = _user
    msg["To"] = ";".join(to_list)
    print "send email to: ", to_list
    try:
        server = smtplib.SMTP(timeout=45)
        server.connect(SMTP_SERVER)
        server.login(_user, _pwd)
        server.sendmail(_user, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print e.args,
        return  False
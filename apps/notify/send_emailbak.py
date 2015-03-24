# -*- coding: utf-8 -*-
import email, sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import logging

pemail = sys.argv[1]
ptext = sys.argv[2]
mailmap = {}
mailmap['server'] = 'smtp.263.net'
mailmap['user'] = 'zhangguodan@viewayintl.com'
mailmap['password'] = 'ZGD1234,.'
mailmap["from"] = 'zhangguodan@viewayintl.com'
mailmap["to"] = pemail
mailmap["subject"] = '标题'
mailmap["text"] = ptext


def sendmail(paramMap):
    smtp = smtplib.SMTP()
    msgRoot = MIMEMultipart(' related ')
    msgAlternative = MIMEMultipart(' alternative ')
    if paramMap.has_key("server") and paramMap.has_key("user") and paramMap.has_key("password"):
        try:
            smtp.connect(paramMap["server"])
            smtp.login(paramMap["user"], paramMap["password"])
        except:
            logging.error(" smtp login exception! ")
            return False

    else:
        logging.error(" Parameters incomplete! ")
        return False  # 测试发现 邮件其头部信息 比如标题 发送地址 还有抄送之类 和stmp发送的具体信息脱离。
    if (paramMap.has_key("subject") and paramMap.has_key("from") and paramMap.has_key("to")) == False:
        logging.error(" Parameters incomplete! ")
        return False

    msgRoot['subject'] = paramMap["subject"]
    msgRoot['from'] = paramMap["from"]
    if paramMap.has_key("cc"):
        msgRoot['cc'] = paramMap["cc"]

    msgRoot['to'] = paramMap["to"]
    msgRoot.preamble = ' This is a multi-part message in MIME format. '
    msgRoot.attach(msgAlternative)
    TempAddTo = paramMap["to"]

    if paramMap.has_key("text"):
        msgText = MIMEText(paramMap["text"], 'plain', 'utf-8')
        msgAlternative.attach(msgText)

    if TempAddTo.find(",") != -1:
        FinallyAdd = TempAddTo.split(",")
    else:
        FinallyAdd = TempAddTo

    smtp.sendmail(paramMap['from'], FinallyAdd, msgRoot.as_string())
    smtp.quit()
    return True


if __name__ == '__main__':
    sendmail(mailmap)
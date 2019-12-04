# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from lxml import etree


def sendemail():
    smtpserver = 'smtp.mxhichina.com'     #阿里邮箱的SMTP服务器地址
    username = 'lizhe@deallinker.com'
    password = 'leeLZLZ1104'
    sender = 'lizhe@deallinker.com'    #发送者
    receiver = ['lizhe@deallinker.com']    #接收者[xxx, xxx, xxx……]

    #读取html并判断测试结果是否正常
    url = r'C:\Users\ly\PycharmProjects\log\result.html'
    page = open(url, 'rb')
    html = page.read()
    parseHTML = etree.HTML(html)
    pass_num = parseHTML.xpath('//*[@class="failClass"]/td[2]/text()')
    count = parseHTML.xpath('//*[@class="failClass"]/td[3]/text()')
    print(pass_num, count)
    n = '正常'
    if count != pass_num:
        n = '异常'

    # 构建email
    tm = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    subject = tm + '费耘测试用例执行' + n
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = '缔联科技测试组'
    msg['To'] = ";".join(receiver)

    # 构造文字内容
    text = "本次API测试报告已出，下方附有测试报告附件。。。"
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    #构造HTML附件
    text_html = MIMEText(html, 'html', 'utf-8')
    text_html["Content-Disposition"] = 'attachment; filename="result.html"'
    msg.attach(text_html)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
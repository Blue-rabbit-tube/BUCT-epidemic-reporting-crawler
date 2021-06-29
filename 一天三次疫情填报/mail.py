# coding=gbk
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def diy_mail(s):                                    #懒得封库了，以后再来    s指传入文件内容           
    sender = '201802xxxx@mail.buct.edu.cn'          #猜猜我是哪个学院的
    passWord = ''                                   #填入自己的邮箱用户名
    receivers = ['@qq.com']                         #需要接收邮件的邮箱列表
    msg = MIMEMultipart()
    msg['Subject'] ="疫情填报"
    msg['From'] = "Router"
    msg_content = s
    msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))




    try:
        s = smtplib.SMTP_SSL("smtp.mail.buct.edu.cn", 465)
        s.set_debuglevel(1)
        s.login(sender,passWord)
        for item in receivers:
            msg['To'] = to = item
            s.sendmail(sender,to,msg.as_string())
            print('Success!')
        s.quit()
        print ("All emails have been sent over!")
    except smtplib.SMTPException as e:
        print ("Falied,%s",e)

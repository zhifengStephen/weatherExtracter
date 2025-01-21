'''
#天气预报：
import schedule

#引入schedule和time

def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)    
#15-17都是检查部署的情况，如果任务准备就绪，就开始执行任务。   
'''

import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = '1933262583@qq.com' #input('请输入你的邮箱：')
password = 'fmcydcjcioiifjii' #input('请输入你的密码：')
#receiver = 'ZXC979@student.bham.ac.uk' #input('请输入收件人的邮箱：')
receiver = '158994970@qq.com'

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    tem=tem1.text
    weather=weather1.text
    return tem,weather

def send_email(tem,weather):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

schedule.every().day.at("08:00").do(job) 
while True:
    schedule.run_pending()
    time.sleep(1)



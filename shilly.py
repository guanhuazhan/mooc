# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time




url_now = 'http://www.icourse163.org/learn/HDU-1002598057?tid=1003257006#/learn/forumindex'
receiver = '1577016476@qq.com'
  
    
def get_webInfo(url):
    broswer = webdriver.Chrome(executable_path = "./drive/chromedriver.exe")
    broswer.get(url)
    html_text = broswer.page_source
    broswer.quit()
    soup = BeautifulSoup(html_text,'html.parser')
    div = soup.find('div',class_= 'm-data-lists f-cb f-pr j-data-list')
    for link in div.find_all('li',limit = 1):
        link2 = link.find('a')
        info_link = link2.get('href')
        info_text = link2.get_text(strip = True)
#        print(info_text)
#        print(url[:-18]+info_link)
#        print('\n')
    return info_text+'\n'+url[:-18]+info_link+'\n'
        
tmp = {'history':None}
def check():
    if(tmp['history']):
        history = tmp['history']
        now = get_webInfo(url_now)
        tmp[history] = now
    else:
        tmp['history'] = get_webInfo(url_now)
        history = tmp['history']
        now = tmp['history']
    if len(history) == len(now):
        result = ''
        for a,b in zip(history,now):
            if a==b:
                print('未发现更新！')
            else:
                print('发现更新')
                result+='--------------------------------------\n'
                result+=b
                result+='--------------------------------------\n'
        if result !='':
            print('更新内容如下：'+result)
            send_mail('你关注的网站有更新',result,receiver)
    else:
        print('数据错误！')
        
def send_email(title,article,receiver):
    host = 'smtp.zdq.space'
    user = 'xxx@zdq.space'
    password = 'xxx123#@$'
    sender = user
    coding = 'utf8'
    
    message = MIMEText(article,'plain',coding)
    message['From'] = Header(sender,coding)
    message['To'] = Header(receiver,coding)
    message['subject'] = Header(title,coding)
    
    try:
        mail_client = smtplib.SMTP_SSL(host,465)
        mail_client.connect(host)
        mail_client.login(user,password)
        mail_client.sendmail(sender,receiver,massage.as_string())
        mail_client.close()
        print('邮件已成功发送给：'+receiver)
    except:
        print('发送失败!')
        
        
#title = input(str('输入邮件标题：'))
#article = input(str('输入邮件内容：'))
#receiver = input(str('输入接收人：'))
#send_mail(title,article,receiver)
while True:
    check()
    print('\n休息30秒继续运行！')
    time.sleep(30)
    print('继续工作。。。')

    
        
    
        
            
        
            
            
            
    
        
        

    
    
    
import os
import time
import unittest
from email.mime.text import MIMEText
from smtplib import SMTP

from Lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
#     1.打开文件
    file = open(path, 'rb')
    mail_message = file.read()
    file.close()
#      2.把邮件正文转成MIME格式
#   MIME是多用途互联网邮件扩展类型，是互联网传输的一种非常常见的数据格式
# plain纯文本邮件
# html html格式的邮件
# 混合型的，可以在邮件中添加附件
    mime = MIMEText(mail_message, _subtype='html', _charset='utf-8')
    mime['Subject'] = '51Testing测试报告'
    mime['From'] = 'bwftest126@126.com'
    mime['To'] = 'changchengxc@126.com'

#     发送邮件
#     1.链接126邮箱服务器，打开126邮箱登录页
    smtp = SMTP()
    smtp.connect("smtp.126.com")
#     2.输入用户名和密码，点击登录
    smtp.login('bwftest126@126.com','abc123asd654')
#     3.发送邮件
    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='changchengxc@126.com')
#     4.断开连接
    smtp.quit()
    print("邮件已经发送成功！")



if __name__ == '__main__':
    # 1.找出所有的测试用例
    # TestLoader测试用例的加载器
    # 比如说，我们要加载哪些测试用例？
    suite = unittest.defaultTestLoader.discover(".", pattern='*Test.py')
    # 2.通过unittest执行测试用例集
    # unittest.TextTestRunner().run(suite)
    # 2.通过HtmlTestRunner文件执行测试用例集
    # stream=sys.stdout 生成好的测试报告保存到哪个文件?
    # strftime()方法用于格式化时间
    # %Y 表示year
    # %m 表示month
    # %d 表示day
    # %H 表示hour
    # %M 表示minute
    # %S 表示seconds
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    base_path = os.path.dirname(__file__)
    path = base_path + "/reporter/" + "test_reporter" + timestamp + ".html"
    # 以写的方式打开文件
    with open(path, 'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1,title="51Testing测试报告",description="测试环境：Window 10 + Chrome", tester = "常城").run(suite)
    send_mail(path)
#     邮件的主要作用是，提醒测试执行完毕
#     每次运行程序，会覆盖原来的测试报告，有时需要看历史数据，所以我们不希望被覆盖
#     解决方法是，让每次生成的测试报告名字不一样，避免重名覆盖
#     在文件名中，增加一个时间戳







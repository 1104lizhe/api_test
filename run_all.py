import unittest
import HTMLTestRunner
import send_email


if __name__ == '__main__':
    test_dir = './TEST'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_ETC.py')
    filename = 'C:\\Users\\ly\\PycharmProjects\\log\\result.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告')
    # runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()
    send_email.sendemail()

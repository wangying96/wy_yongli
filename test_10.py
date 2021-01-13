from selenium import webdriver
import time
import unittest
class D(unittest.TestCase):
    def setUp(self):
        self.huohu=webdriver.Firefox()
        self.huohu.get("http://123.57.140.190/manage/")

    def text_007yulan(self):
        try:
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            self.huohu.find_element_by_class_name("icon-eye-open").click()
            self.huohu.find_element_by_xpath("/html/body/div[4]/span[1]/a").click()
            yuqi = self.huohu.find_element_by_xpath("/html/body/div[4]/div[1]").text
            self.assertEqual(yuqi, "预览", msg="预览成功")
            time.sleep(1)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    # unittest.main()
    #实例化对象，创建测试集
    suite=unittest.TestSuite()
    suite.addTest(D("text_007yulan"))
    run=unittest.TextTestRunner()
    run.run(suite)

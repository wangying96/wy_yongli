from selenium import webdriver
import time
import unittest
class D(unittest.TestCase):
    def setUp(self):
        self.huohu=webdriver.Firefox()
        self.huohu.get("http://123.57.140.190/manage/")

    def text_006shanchu(self):
        self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
        self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
        self.huohu.find_element_by_xpath(
            "/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span").click()
        self.huohu.find_element_by_xpath("/html/body/div[4]/div[3]/a[1]").click()
        yuqi = self.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
        time.sleep(1)
        self.assertEqual(yuqi, "产品删除成功！", msg="删除成功")
        time.sleep(1)
if __name__ == '__main__':
    # unittest.main()
    #实例化对象，创建测试集
    suite=unittest.TestSuite()
    suite.addTest(D("text_006shanchu"))
    run=unittest.TextTestRunner()
    run.run(suite)

from selenium import webdriver
import time
import unittest
class D(unittest.TestCase):
    def setUp(self):
        self.huohu=webdriver.Firefox()
        self.huohu.get("http://123.57.140.190/manage/")

    def test_005bianji(self):
        try:
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()

            self.huohu.find_element_by_css_selector(
                ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)").click()
            self.huohu.find_element_by_name("pro_name").clear()
            self.huohu.find_element_by_name("cpbh").send_keys("N000匹配07998")
            self.huohu.find_element_by_name("cptxm").send_keys("AAe76g9gjhbp284")
            self.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("bbb头oo大pp，水分足")
            self.huohu.find_element_by_xpath(
                "/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()

            yuqi = self.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
            time.sleep(1)
            self.assertEqual(yuqi, "产品名称没有填写！", msg="断言成功")
            time.sleep(1)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    # unittest.main()
    #实例化对象，创建测试集
    suite=unittest.TestSuite()
    suite.addTest(D("test_005bianji"))
    run=unittest.TextTestRunner()
    run.run(suite)

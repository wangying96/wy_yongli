import unittest
from selenium import webdriver
import time
class D(unittest.TestCase):
    def setUp(self):
        self.huohu=webdriver.Firefox()
        self.huohu.get("http://123.57.140.190/manage/")
    def tearDown(self):
        self.huohu.close()
        self.huohu.quit()

    def test_03xinzeng(self):
        try:
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            self.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
            self.huohu.find_element_by_name("pro_name").send_keys("陕西蒲城酥梨")
            self.huohu.find_element_by_name("cpbh").send_keys("N00112")
            self.huohu.find_element_by_name("cptxm").send_keys("HU7689H3284")
            self.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("个头大，水分足")
            self.huohu.find_element_by_css_selector(".btn.btn-danger").click()

            yuqi = self.huohu.find_element_by_css_selector(".layui-layer-content").text
            time.sleep(1)
            self.assertEqual(yuqi, "产品条码有重复!", msg="条码有重复")
            time.sleep(1)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    # unittest.main()
    #实例化对象，创建测试集
    suite=unittest.TestSuite()
    suite.addTest(D("test_03xinzeng"))
    run=unittest.TextTestRunner()
    run.run(suite)

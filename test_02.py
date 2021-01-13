import unittest
import requests
class Sou(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_002soubf(self):
        url = "http://123.57.140.190/manage/list_cp.php"

        payload = 'cpbh=222555777'
        headers = {
            'Cookie': 'PHPSESSID=cfgm985ppq80d0jr4vmnpq1ol7',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        a = response.text
        self.assertNotIn("222555777", a, msg="查询成功2")
if __name__ == '__main__':

    # unittest.main()
    stiue=unittest.TestSuite()
    # stiue.addTest(Sou("001souqb"))
    stiue.addTest(Sou("002soubf"))
    # stiue.addTest(Sou("003soubf"))
    run=unittest.TextTestRunner()
    run.run(stiue)

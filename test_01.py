import requests
import unittest

url = "http://123.57.140.190/manage/add_cp.php?act=save_cp"

payload={'pro_name': '王莹1',
'cpbh': 'wy003',
'cptxm': 'wy003',
'cpms': '真好a'}
files=[

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=---------------------------96711835827378414952031371884',
  'Cookie': 'PHPSESSID=pvmp96u90p6nmc2u2rbce94hi0'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)



if __name__ == '__main__':

    unittest.main()
    # stiue=unittest.TestSuite()
    # stiue.addTest(Sou("001souqb"))
    # # stiue.addTest(Sou("002soubf"))
    # # stiue.addTest(Sou("003soubf"))
    # run=unittest.TextTestRunner()
    # run.run(stiue)
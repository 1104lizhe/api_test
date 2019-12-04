from hashlib import md5
import unittest
import requests
import random
import json

class testdedu(unittest.TestCase):
    def setUp(self):
        self.company_key = 'af6bce91-0eec-409b-9627-754d23dd087c'
        self.c_secret = 'b04be205-3953-4e9c-b037-1fae320c33ca'
        self.url = 'https://www.feeclouds.com'

        #v3/ocr

    def picture(self, path):
        path = [r'C:\Users\ly\Desktop\微信图片_20191031211542.png']
        r = ''
        for pic in path:
            with open(pic, 'rb') as f:
                res = base64.encodestring(f.read())
                res = res.decode()
            r = r + ',' + res
        return r[1:]

    def get_nonce_str(self):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.sample(chars, 6))

    def sign_action(self, key, parameters):
        sortedParameters = sorted(
            parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k, v) in sortedParameters:
            if v or v == 0:
                canonicalizedQueryString += '&' + str(k).strip() + '=' + str(v).strip()
        tempstring = canonicalizedQueryString[1:] + '&' + 'company_secret=' + str(key)
        signature = md5(tempstring.strip().encode()).hexdigest().upper()
        return signature

    def check(self, department_id, is_check, path):
        data = {}
        api = '/api/v3/ocr/check'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['department_id'] = department_id
        data['is_check'] = is_check
        data['sign'] = self.sign_action(company_secret, data)
        data['file_data'] = self.picture(path)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        return r, a


    # def test_zp_0(self):    #专票
    #     department_id = '11'
    #     is_check = '0'
    #     path = [r'C:\Users\ly\Desktop\微信图片_20191031211542.png']
    #     r, a = self.check(department_id, is_check, path)



























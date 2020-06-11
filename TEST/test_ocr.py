from hashlib import md5
import unittest
import requests
import random
import base64
from PIL import Image
import json
import random

class TestOCR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.company_key = 'af6bce91-0eec-409b-9627-754d23dd087c'   #生产124
        cls.c_secret = 'b04be205-3953-4e9c-b037-1fae320c33ca'

        cls.company_key_2 = 'c58fafe5-9092-41ed-9276-120b962f65cc'   #api测试集团
        cls.c_secret_2 = '2f12bc36-b8d0-4298-99c2-dbcefac1ba0d'

        cls.url = 'https://www.feeclouds.com'
        #图片路径
        cls.image_path = r'C:\Users\ly\Desktop\ocr_image'

        #v3/ocr
        #is_check=2
        #专票，普票
        cls.zp_2 = ['msg', 'data', 'code']
        cls.zp_data_2 = ['msg', 'code', 'fpzl', 'invoiceid', 'forbidens', 'orientation', 'region', 'region_path',
                        'invoice', 'invoice_detail', 'ocr_result']
        cls.zp_invoice_2 = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc','bswj','bswj_match']
        cls.zp_invoice_2_dup = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc','bswj','bswj_match','img_url']
        cls.zp_detail_2 = ['dj', 'ggxh', 'hwmc', 'tszcbs', 'slv', 'sl', 'sjsl', 'dw', 'je', 'se', 'sjse']
        cls.ocr_2 = ['fpdm', 'fphm', 'kprq', 'jym', 'je', 'jshj']
        #电票
        cls.dp_invoice_2 = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'dedu_se','bswj','bswj_match']
        cls.dp_invoice_2_dup = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'dedu_se','bswj','bswj_match','img_url']

        #卷票
        cls.jp_invoice_2 = ['cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'jym', 'se', 'memo', 'fplc','lc','bswj','bswj_match']
        cls.jp_invoice_2_dup = ['cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'jym', 'se', 'memo', 'fplc','lc','img_url','bswj','bswj_match']
        cls.jp_detail_2 = ['dj', 'tszcbs', 'hwmc', 'sjsl', 'sl', 'je', 'se', 'sjse']
        #通行费
        cls.txf_invoice_2 = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'txfbz','bswj','bswj_match']
        cls.txf_invoice_2_dup = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'txfbz','bswj','bswj_match','img_url']
        cls.txf_detail_2 = [u"cph", u"hwmc", u"slv", u"txrqq", u"txrqz", u"je", u"lx", u"se", u"tszcbs", u"sjsl", u"sjse"]
        #机动车
        cls.jdc_invoice_2 = ['zh', 'xfsbh', 'xcrs', 'fpdm', 'zfbz', 'kprq', 'gfsbh', 'fdjhm', 'swjg_dm', 'cjhm',
                            'skph', 'content', 'dkbz', 'lc', 'title', 'wspzhm', 'cjfy', 'cd', 'sjse', 'file_path',
                            'jqbh', 'hgzs', 'jshj', 'dh', 'memo', 'fplc', 'cycs', 'xhdwmc', 'dz', 'cllx', 'sjsl',
                            'tszcbs', 'sjdh', 'fpzl', 'sfzhm', 'swjg_mc', 'fphm', 'jkzmsh', 'khyh', 'dw', 'zfbz_new',
                            'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'ghdw','bswj','bswj_match']
        cls.jdc_invoice_2_dup = ['zh', 'xfsbh', 'xcrs', 'fpdm', 'zfbz', 'kprq', 'gfsbh', 'fdjhm', 'swjg_dm', 'cjhm',
                            'skph', 'content', 'dkbz', 'lc', 'title', 'wspzhm', 'cjfy', 'cd', 'sjse', 'file_path',
                            'jqbh', 'hgzs', 'jshj', 'dh', 'memo', 'fplc', 'cycs', 'xhdwmc', 'dz', 'cllx', 'sjsl',
                            'tszcbs', 'sjdh', 'fpzl', 'sfzhm', 'swjg_mc', 'fphm', 'jkzmsh', 'khyh', 'dw', 'zfbz_new',
                            'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'ghdw','bswj','bswj_match','img_url']
        #二手车
        cls.erp_invoice_2 = ['sjsl', 'xfdh', 'fpdm', 'zfbz', 'cgsmc', 'kprq', 'gfsbh', 'xfdw', 'gfhm', 'jysbh', 'skph',
                            'tszcbs', 'title', 'scdh', 'scmc', 'xfhm', 'content', 'sjse', 'file_path', 'jqbh', 'jyyhzh',
                            'memo', 'cjhm', 'cjhj', 'cycs', 'cllx', 'xfsbh', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'lc',
                            'jydw', 'fphm', 'gfdw', 'gfdz', 'xfdz', 'jydz', 'zfbz_new', 'scsbh', 'fplc', 'cpxh', 'jydh',
                            'djzh', 'gfdh', 'scdz', 'cpzh','bswj','bswj_match']
        cls.erp_invoice_2_dup = ['sjsl', 'xfdh', 'fpdm', 'zfbz', 'cgsmc', 'kprq', 'gfsbh', 'xfdw', 'gfhm', 'jysbh', 'skph',
                            'tszcbs', 'title', 'scdh', 'scmc', 'xfhm', 'content', 'sjse', 'file_path', 'jqbh', 'jyyhzh',
                            'memo', 'cjhm', 'cjhj', 'cycs', 'cllx', 'xfsbh', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'lc',
                            'jydw', 'fphm', 'gfdw', 'gfdz', 'xfdz', 'jydz', 'zfbz_new', 'scsbh', 'fplc', 'cpxh', 'jydh',
                            'djzh', 'gfdh', 'scdz', 'cpzh','bswj','bswj_match','img_url']

        #四项不一致，白名单，重复录入
        cls.fun1_invoice_2 = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh',
                          'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                          'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc', 'lc', 'create_time','bswj','bswj_match']
        cls.fun1_detail_2 = ['dj', 'dw', 'ggxh', 'hwmc', 'je', 'se', 'sl', 'slv']

        #is_check=1
        #专票、普票
        cls.zp = ['msg', 'data', 'code']
        cls.zp_data = ['msg', 'code', 'fpzl', 'invoiceid', 'forbidens', 'orientation', 'region', 'region_path',
                        'invoice', 'invoice_detail', 'ocr_result']
        cls.zp_invoice = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc','bswj','bswj_match']
        cls.zp_detail = ['dj', 'ggxh', 'hwmc', 'tszcbs', 'slv', 'sl', 'sjsl', 'dw', 'je', 'se', 'sjse']
        cls.ocr = ['fpdm', 'fphm', 'kprq', 'jym', 'je', 'jshj']
        #电票
        cls.dp_invoice = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'dedu_se','bswj','bswj_match']
        #卷票
        cls.jp_invoice = ['cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'jym', 'se', 'memo', 'fplc','lc','bswj','bswj_match']
        cls.jp_detail = ['dj', 'tszcbs', 'hwmc', 'sjsl', 'sl', 'je', 'se', 'sjse']
        #通行费
        cls.txf_invoice = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz',
                           'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                           'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc','lc', 'txfbz','bswj','bswj_match']
        cls.txf_detail = [u"cph", u"hwmc", u"slv", u"txrqq", u"txrqz", u"je", u"lx", u"se", u"tszcbs", u"sjsl", u"sjse"]
        #机动车
        cls.jdc_invoice = ['zh', 'xfsbh', 'xcrs', 'fpdm', 'zfbz', 'kprq', 'gfsbh', 'fdjhm', 'swjg_dm', 'cjhm',
                            'skph', 'content', 'dkbz', 'lc', 'title', 'wspzhm', 'cjfy', 'cd', 'sjse', 'file_path',
                            'jqbh', 'hgzs', 'jshj', 'dh', 'memo', 'fplc', 'cycs', 'xhdwmc', 'dz', 'cllx', 'sjsl',
                            'tszcbs', 'sjdh', 'fpzl', 'sfzhm', 'swjg_mc', 'fphm', 'jkzmsh', 'khyh', 'dw', 'zfbz_new',
                            'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'ghdw','bswj','bswj_match']
        #二手车
        cls.erp_invoice = ['sjsl', 'xfdh', 'fpdm', 'zfbz', 'cgsmc', 'kprq', 'gfsbh', 'xfdw', 'gfhm', 'jysbh', 'skph',
                            'tszcbs', 'title', 'scdh', 'scmc', 'xfhm', 'content', 'sjse', 'file_path', 'jqbh', 'jyyhzh',
                            'memo', 'cjhm', 'cjhj', 'cycs', 'cllx', 'xfsbh', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'lc',
                            'jydw', 'fphm', 'gfdw', 'gfdz', 'xfdz', 'jydz', 'zfbz_new', 'scsbh', 'fplc', 'cpxh', 'jydh',
                            'djzh', 'gfdh', 'scdz', 'cpzh','bswj','bswj_match']

        #四项不一致，白名单，重复录入
        cls.fun1_invoice = ['gfdzdh', 'cpybz', 'fpdm', 'zfbz', 'zfbz_new', 'xfdzdh', 'kprq', 'gfsbh',
                          'title', 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'cycs', 'xfsbh', 'je', 'gfmc',
                          'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'memo', 'fplc', 'lc', 'create_time','bswj','bswj_match']
        cls.fun1_detail = ['dj', 'dw', 'ggxh', 'hwmc', 'je', 'se', 'sl', 'slv']

        #is_check=0
        cls.data = ['orientation', 'ocr_result', 'region', 'region_path', 'invoice', 'fpzl']
        cls.ocr_result = ['jshj', 'fpdm', 'fphm', 'kprq', 'je', 'jym']
        cls.invoice = ['fplc', 'memo', 'file_path', 'lc']

        #其他发票
        cls.other_data = ['invoiceid', 'orientation', 'ocr_result', 'region', 'code', 'region_path', 'invoice', 'msg', 'fpzl']
        # fpzl=101
        cls.other_ocr_result_101 = ['fpdm', 'fphm', 'total']
        cls.other_invoice_101 = ['memo', 'file_path']
        # fpzl=104
        cls.other_ocr_result_104 = ['name', 'seat', 'number', 'train_number', 'station_geton', 'station_getoff', 'time', 'date', 'total']
        cls.other_invoice_104 = ['dedu_se', 'memo', 'file_path']
        # fpzl=103
        cls.other_ocr_result_103 = ['time_getoff', 'fphm', 'time_geton', 'fpdm', 'mileage', 'place', 'date', 'total']
        cls.other_invoice_103 = ['memo', 'file_path']


    def picture(self, path):
        path = path
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

    def check_2(self, department_id, is_check, path):
        data = {}
        api = '/api/v3/ocr/check'
        data['company_key'] = self.company_key_2
        company_secret = self.c_secret_2
        data['nonce_str'] = self.get_nonce_str()
        data['department_id'] = department_id
        data['is_check'] = is_check
        data['sign'] = self.sign_action(company_secret, data)
        data['file_data'] = self.picture(path)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        return r, a


    def test_zp_0(self):    #专票，code=0
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\微信图片_20190710155620.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_dp_0(self):   #电票
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\滴滴电子发票 (16).pdf']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.dp_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jp_0(self):  #卷票
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\A73C33C9-9D9B-4BCC-ACF8-AAEE81943405.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_txf_0(self):  #通行费
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\000c8f6a6874423ba81c88fc311bdfdd.pdf']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.txf_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.txf_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jdc_0(self):  #机动车票
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\ZmDbeTCWTE.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jdc_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_erp_0(self):   #二手车
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\mfdQFsGE88.png']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.erp_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_zp_20509_dup(self):   #专票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\8772b528-7ab3-4901-979c-73bc374dbe01_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_pp_20509_dup(self):   #普票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\58AF02D8-19EB-4F6A-A77F-F916A5ACFD4D.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_dp_20509_dup(self):   #电票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\e0d004c48e8740b0bd691cfd82cc8afb.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.dp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jp_20509_dup(self):   #卷票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\d2063766-148b-4101-8d01-3592e937b296_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.jp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_txf_20509_dup(self):   #通行费，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\0c075c54-7342-4f7f-8f34-cfa0bace8b72_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.txf_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.txf_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jdc_20509_dup(self):  #机动车，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\y3nkiSxCbn.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jdc_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_erp_20509_dup(self):   #二手车，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '1'
        path = [self.image_path + '\\H7R74AtRG2.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.erp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_tax(self):    #抬头税号校验      124的北京缔联科技有限公司9
        department_id = '481d2d5cc79e4029a3eae78216908304'
        is_check = '1'
        path = [self.image_path + '\\02552d92e4464bb69a14f48bb05735a1.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][0], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_h_b(self):    #货物黑名单
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\0f99dbe604184072b04ed790c677ca87.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][2], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_c_b(self):   #企业黑名单
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '1'
        path = [self.image_path + '\\9bb4717cd11d47978a10c92e0e223968.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][3], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_sx(self):   #四项信息校验  124的456公司
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '1'
        path = [self.image_path + '\\a0210d72b8ef4c53963f4b6f9d72a056.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun1(self):    #四项不一致，白名单，重复录入
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '1'
        path = [self.image_path + '\\10c08f336a8146e1a9c573f44e19c8dc.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.fun1_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.fun1_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun2(self):   #四项不一致，白名单，企业黑名单
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '1'
        path = [self.image_path + '\\d9c3eb4509c4480bb2bf964e6058902b.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun3(self):    #四项不一致，白名单
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '1'
        path = [self.image_path + '\\59d22d9133324265ac5fdfef60691935.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_0_zp(self):   #is_check=0,专票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\1a086112510f4e3ca79a7e372011143d.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_pp(self):    #is_check=0,普票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\22b25cf104974e039693e32aedef9f04.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_dp(self):    #is_check=0,电票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\89579e1088764b4099cbb7333627d166.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_jp(self):   #is_check=0,卷票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\E79486B8-8AB0-4901-B68E-EB342517334B.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertEqual(a['data'][0]['fpzl'], '11', '发票种类错误，图为卷票11')
        self.assertIsNotNone(a['data'][0]['ocr_result']['jshj'], '卷票jshj字段应有值,目前没有')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_txf(self):   #is_check=0,通行费
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\通行费.pdf']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_esc(self):   #is_check=0,二手车
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\ECaY6fteii.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_jdc(self):    #is_check=0,机动车
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\mEyrjs4Qea.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.ocr_result), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    #其他发票
    def test_0_101(self):    #is_check=0,定额发票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\101.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.other_data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.other_ocr_result_101), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.other_invoice_101), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_104(self):    #is_check=0,火车票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\104.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.other_data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.other_ocr_result_104), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.other_invoice_104), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_0_103(self):    #is_check=0,出租车票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = 0
        path = [self.image_path + '\\103.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.other_data), sorted(a['data'][0]), 'data中字段有误')
        self.assertListEqual(sorted(self.other_ocr_result_103), sorted(a['data'][0]['ocr_result']), 'ocr_result中字段有误')
        self.assertListEqual(sorted(self.other_invoice_103), sorted(a['data'][0]['invoice']), 'invoice中字段有误')

    def test_2_zp(self):
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = 2
        path = [self.image_path + '\\2EiN47QN3t.jpg']
        r,a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_2_dp(self):   #电票
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = '2'
        path = [self.image_path + '\\滴滴电子发票 (5).pdf']   
        r, a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.dp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_2_jp(self):  #卷票
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = '2'
        path = [self.image_path + '\\2.jpg']
        r, a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_2_txf(self):  #通行费
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = '2'
        path = [self.image_path + '\\3f080191b8154dc9836016a34a21ffa8.pdf']
        r, a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.txf_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.txf_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_2_jdc(self):  #机动车票
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = '2'
        path = [self.image_path + '\\03机动车.jpg']
        r, a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jdc_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_2_erp(self):   #二手车
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        is_check = '2'
        path = [self.image_path + '\\mfdQFsGE88.png']
        r, a = self.check_2(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.erp_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_zp_20509_dup_2(self):   #专票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\8772b528-7ab3-4901-979c-73bc374dbe01_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_pp_20509_dup_2(self):   #普票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\58AF02D8-19EB-4F6A-A77F-F916A5ACFD4D.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_dp_20509_dup_2(self):   #电票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\e0d004c48e8740b0bd691cfd82cc8afb.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.dp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jp_20509_dup_2(self):   #卷票，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\d2063766-148b-4101-8d01-3592e937b296_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.jp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_txf_20509_dup_2(self):   #通行费，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\0c075c54-7342-4f7f-8f34-cfa0bace8b72_invoice.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, '外层code不为0')
        self.assertEqual(a['data'][0]['code'], 20509, '里层code不为20509')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.txf_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.txf_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_jdc_20509_dup_2(self):  #机动车，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\y3nkiSxCbn.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.jdc_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_erp_20509_dup_2(self):   #二手车，重复录入
        department_id = 'e2f12b4430b645ba82ebb6beb6d641ff'
        is_check = '2'
        path = [self.image_path + '\\H7R74AtRG2.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.erp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_tax_2(self):    #抬头税号校验      124的北京缔联科技有限公司9
        department_id = '481d2d5cc79e4029a3eae78216908304'
        is_check = '2'
        path = [self.image_path + '\\02552d92e4464bb69a14f48bb05735a1.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][0], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2_dup), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_h_b_2(self):    #货物黑名单
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '2'
        path = [self.image_path + '\\0f99dbe604184072b04ed790c677ca87.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][2], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_c_b_2(self):   #企业黑名单
        department_id = '363a2d4bb727489981a4e4571b6d1359'
        is_check = '2'
        path = [self.image_path + '\\9bb4717cd11d47978a10c92e0e223968.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][3], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_20509_sx_2(self):   #四项信息校验  124的456公司
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '2'
        path = [self.image_path + '\\a0210d72b8ef4c53963f4b6f9d72a056.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='foebidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun1_2(self):    #四项不一致，白名单，重复录入
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '2'
        path = [self.image_path + '\\10c08f336a8146e1a9c573f44e19c8dc.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.fun1_invoice), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.fun1_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun2_2(self):   #四项不一致，白名单，企业黑名单
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '2'
        path = [self.image_path + '\\d9c3eb4509c4480bb2bf964e6058902b.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertTrue(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

    def test_fun3_2(self):    #四项不一致，白名单   124的456公司，每次执行完删一下发票
        department_id = '1be05d4daecb40f49e29a13997efaa59'
        is_check = '2'
        path = [self.image_path + '\\59d22d9133324265ac5fdfef60691935.jpg']
        r, a = self.check(department_id, is_check, path)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertFalse(a['data'][0]['forbidens'][3], msg='forbidens有误')
        self.assertTrue(a['data'][0]['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data'][0]['forbidens'][1], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_data), sorted(a['data'][0]), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice_2), sorted(a['data'][0]['invoice']), 'invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(a['data'][0]['invoice_detail'][0]), 'detail中字段有误')
        self.assertListEqual(sorted(self.ocr), sorted(a['data'][0]['ocr_result']))

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(TestOCR('test_fun1_2'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()




























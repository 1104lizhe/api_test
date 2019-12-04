#-*-coding:utf-8-*-
from hashlib import md5
import requests
import json
import base64
import random
import unittest


class testFC(unittest.TestCase):

    def setUp(self):
        self.url = 'https://www.feeclouds.com'
        # url = 'http://192.168.1.69:8008'
        # url = 'http://192.168.1.106:8005'

        #api测试集团
        self.company_key = 'c58fafe5-9092-41ed-9276-120b962f65cc'
        self.c_secret = '2f12bc36-b8d0-4298-99c2-dbcefac1ba0d'

        #专票/普票/电票
        self.zp_1 = ['msg', 'code', 'data']
        self.zp_2 = ['invoice_detail', 'forbidens', 'invoice', 'invoice_id']
        self.zp_invoice = ['gfdzdh', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'gfmc', 'title', 'gfyhzh', 'content',
                           'company_fake', 'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'cpybz', 'xfsbh', 'je', 'dkbz',
                           'fpzl', 'bz', 'fphm', 'zfbz_new', 'xfmc', 'xfyhzh', 'jym', 'se']
        self.zp_detail = ['dj', 'tszcbs', 'ggxh', 'hwmc', 'slv', 'sjsl', 'sl', 'dw', 'je', 'se', 'sjse']

        #卷票
        self.jp_1 = ['msg', 'code', 'data']
        self.jp_2 = ['invoice_detail', 'forbidens', 'invoice', 'invoice_id']
        self.jp_invoice = ['fpdm', 'zfbz', 'kprq', 'gfsbh', 'gfmc', 'title', 'content', 'company_fake', 'file_path', 'jqbh',
                           'jshj', 'memo', 'cycs', 'cpybz', 'xfsbh', 'je', 'dkbz', 'fpzl', 'bz', 'fphm', 'zfbz_new', 'xfmc',
                           'jym', 'se']
        self.jp_detail = ['dj', 'tszcbs', 'hwmc', 'sjsl', 'sl', 'je', 'se', 'sjse']

        #通行费
        self.tp_1 = ['msg', 'code', 'data']
        self.tp_2 = ['invoice_detail', 'forbidens', 'invoice', 'invoice_id']
        self.tp_invoice = ['gfdzdh', 'txfbz', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'gfmc', 'title', 'gfyhzh', 'content',
                           'company_fake', 'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'cpybz', 'xfsbh', 'je', 'dkbz', 'fpzl',
                           'bz', 'fphm', 'zfbz_new', 'xfmc', 'xfyhzh', 'jym', 'se']
        self.tp_detail = ['cph', 'tszcbs', 'hwmc', 'slv', 'txrqz', 'txrqq', 'sjsl', 'je', 'lx', 'se', 'sjse']

        #机动车
        self.jdc_1 = ['msg', 'code', 'data']
        self.jdc_2 = ['invoice_detail', 'forbidens', 'invoice', 'invoice_id']
        self.jdc_invoice = ['swjg_dm', 'sjsl', 'xcrs', 'fpdm', 'zfbz', 'fdjhm', 'kprq', 'cd', 'gfsbh', 'zh', 'skph', 'cjfy',
                            'sjdh', 'tszcbs', 'title', 'wspzhm', 'content', 'sfzhm', 'file_path', 'jqbh', 'hgzs', 'jshj',
                            'dh', 'cjhm', 'khyh', 'cycs', 'xhdwmc', 'dz', 'cllx', 'xfsbh', 'dw', 'dkbz', 'fpzl', 'sjse', 'fphm',
                            'jkzmsh', 'ghdw', 'zfbz_new', 'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'swjg_mc']

        #二手车
        self.erp_1 = ['msg', 'code', 'data']
        self.erp_2 = ['invoice_detail', 'forbidens', 'invoice', 'invoice_id']
        self.erp_invoice = ['xfsbh', 'xfdh', 'memo', 'fpdm', 'zfbz', 'cgsmc', 'djzh', 'kprq', 'gfsbh', 'xfdw', 'gfhm', 'jysbh',
                            'skph', 'tszcbs', 'title', 'scsbh', 'scmc', 'xfhm', 'content', 'company_fake', 'jydw', 'file_path', 'jqbh',
                            'cjhm', 'cjhj', 'cycs', 'cllx', 'sjsl', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'sjse', 'scdz', 'cpzh', 'fphm',
                            'gfdw', 'gfdz', 'xfdz', 'jydz', 'zfbz_new', 'scdh', 'cpxh', 'jyyhzh', 'gfdh', 'jydh']

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
        # print('tempstring:',tempstring)
        # print('sign:', signature)
        return signature

    def check(self, content, fpzl):
        api = '/api/v1/invoice/check'
        data = {}
        data['company_key'] = self.company_key
        data['nonce_str'] = self.get_nonce_str()
        data['content'] = content
        data['sign'] = self.sign_action(self.c_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = ['01', '04', '10', '11', '14']
        b = ['03', '15']
        dic_data = json.loads(r.text)
        if fpzl in a:
            lis10 = list(dic_data.keys())
            lis11 = dic_data.get('data')
            lis12 = dic_data.get('data').get('invoice')
            lis13 = dic_data.get('data').get('invoice_detail')[0]
            lis_f = dic_data.get('data').get('forbidens')
        elif fpzl in b:
            lis10 = list(dic_data.keys())
            lis11 = dic_data.get('data')
            lis12 = dic_data.get('data').get('invoice')
            lis13 = None
            lis_f = dic_data.get('data').get('forbidens')
        else:
            raise "发票种类输入有误"
        return r, lis10, lis11, lis12, lis13, dic_data, lis_f

    def test_v1_zp(self):  # code=0,01专票
        content = ',,3700192130,04604478,45667.26,20191018,,'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.zp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_2), sorted(lis11), '第二层字段有误')
        self.assertListEqual(sorted(self.zp_invoice), sorted(lis12), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(lis13), '第三层detail中字段有误')

    def test_v1_pp(self):    #code=20509, 04普票
        content = ',,033021900104,14362622,,20190919,732317'
        fpzl = '04'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.zp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp_invoice), sorted(lis12), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(lis13), '第三层detail中字段有误')

    def test_v1_dp(self):   #code=20509, 10电票
        content = ',,044001900211,48863815,25.84,20191106,297054,'
        fpzl = '10'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.zp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.zp_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.zp_invoice), sorted(lis12), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.zp_detail), sorted(lis13), '第三层detail中字段有误')

    def test_v1_jp(self):    #code=20509, 11卷票
        content = ',,034001800107,11504521,,20191105,830588,'
        fpzl = '11'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.jp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.jp_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.jp_invoice), sorted(lis12), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.jp_detail), sorted(lis13), '第三层detail中字段有误')

    def test_v1_tp(self):    #code=20509, 14通行费
        content = ',,023001700112,00607398,,20191111,285914,'
        fpzl = '14'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.tp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.tp_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.tp_invoice), sorted(lis12), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.tp_detail), sorted(lis13), '第三层detail中字段有误')

    def test_v1_jdc(self):   #code=20510, 03机动车
        content = ',,134021922204,00041913,62654.87,20190606,,,'
        fpzl = '03'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20510)
        self.assertEqual(dic_data['msg'], '禁止在集团模式时录入机动车销售统一发票')
        self.assertListEqual(sorted(self.jdc_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.jdc_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.jdc_invoice), sorted(lis12), '第三层invoice中字段有误')

    def test_v1_erp(self):   #code=20509, 15二手车
        content = ',,045001800417,00068266,30000.00,20190401,,'
        fpzl = '15'
        r, lis10, lis11, lis12, lis13, dic_data, lis_f = self.check(content, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.erp_1), sorted(lis10), '第一层字段有误')
        self.assertListEqual(sorted(self.erp_2), sorted(lis11), '第二层字段有误')
        self.assertTrue(lis_f[0], msg='forbidens有误')
        self.assertFalse(lis_f[1], msg='forbidens有误')
        self.assertFalse(lis_f[2], msg='forbidens有误')
        self.assertFalse(lis_f[3], msg='forbidens有误')
        self.assertFalse(lis_f[4], msg='forbidens有误')
        self.assertListEqual(sorted(self.erp_invoice), sorted(lis12), '第三层invoice中字段有误')



















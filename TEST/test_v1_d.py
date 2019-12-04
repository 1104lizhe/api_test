#-*-coding:utf-8-*-
from hashlib import md5
import requests
import json
import base64
import random
import unittest


class testFC(unittest.TestCase):

    def setUp(self):
        self.data = {}
        self.url = 'https://www.feeclouds.com'
        # url = 'http://192.168.1.69:8008'
        # url = 'http://192.168.1.106:8005'
        # self.url = 'http://182.92.1.42:8081'

        #api测试集团
        self.company_key = 'c58fafe5-9092-41ed-9276-120b962f65cc'
        self.c_secret = '2f12bc36-b8d0-4298-99c2-dbcefac1ba0d'
        # 集团测试生产-110
        # company_key = 'af6bce91-0eec-409b-9627-754d23dd087c'
        # c_secret = 'b04be205-3953-4e9c-b037-1fae320c33ca'

        # 集团测试生产-zhanglu
        # self.company_key = '87a7da63-0515-4c36-b198-aec8de94d80c'
        # self.c_secret = '5923a209-93b1-4288-98e5-35a908cba33f'

        # 非集团-maohuade@deallinker.cn
        # company_key = 'c36918bf-61c9-4002-b455-36327887eb8c'
        # c_secret = 'c7ef8334-a4c7-4536-a1c9-acab12714a04'


        self.lis00 = ['msg', 'code', 'data']
        self.lis01 = ['msg', 'invoiceid', 'code', 'data', 'forbidens']
        self.lis02 = ['status_code', 'reason', 'invoice', 'invoice_detail']
        self.lis02_dup = ['status_code', 'reason', 'invoice', 'invoice_detail', 'department_id']

        # v1check
        # 专01/普04/电10 invoice
        self.lis03 = ['gfdzdh', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz', 'title',
                 'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'xfsbh',
                 'je', 'gfmc', 'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'cpybz', 'zfbz_new']
        self.lis03_dup = ['gfdzdh', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'create_time', 'title',
                     'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'xfsbh',
                     'je', 'gfmc', 'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'cpybz', 'zfbz_new']
        # 专01/普04/电10 detail
        self.lis04 = ['dj', 'tszcbs', 'ggxh', 'hwmc', 'slv', 'sjsl', 'sl', 'dw', 'je', 'se', 'sjse']
        self.lis04_dup = ['dj', 'ggxh', 'hwmc', 'slv', 'sl', 'dw', 'je', 'se']

        self.lis05 = ['reason', 'fphm', 'kprq', 'title', 'fpzl', 'fpdm']

        # 卷票11 invoice
        self.lis_jsi = ['jqbh', 'jshj', 'kprq', 'dkbz', 'title', 'jym', 'memo', 'cycs', 'fpdm', 'zfbz',
                   'xfmc', 'fphm', 'bz', 'xfsbh', 'je', 'content', 'gfsbh', 'gfmc', 'fpzl', 'file_path', 'se',
                   'gfdzdh', 'xfdzdh', 'gfyhzh', 'cpybz', 'xfyhzh', 'zfbz_new']
        self.lis_jsi_dup = ['jqbh', 'jshj', 'kprq', 'create_time', 'title', 'jym', 'memo', 'cycs', 'fpdm', 'zfbz',
                       'xfmc', 'fphm', 'bz', 'xfsbh', 'je', 'content', 'gfsbh', 'gfmc', 'fpzl', 'file_path', 'se',
                       'gfdzdh', 'xfdzdh', 'gfyhzh', 'cpybz', 'xfyhzh', 'zfbz_new']
        # 卷票11 detail
        self.lis_jsd = ['dj', 'tszcbs', 'hwmc', 'sjsl', 'sl', 'je', 'se', 'sjse', 'ggxh', 'slv', 'dw']
        self.lis_jsd_dup = ['dj', 'hwmc', 'sl', 'je', 'se', 'ggxh', 'slv', 'dw']

        # 通行费14 invoice
        self.lis_txfi = ['gfdzdh', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'dkbz', 'title',
                    'gfyhzh', 'content', 'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'xfsbh', 'je', 'gfmc',
                    'fpzl', 'bz', 'fphm', 'xfmc', 'xfyhzh', 'jym', 'se', 'txfbz', 'cpybz', 'zfbz_new']
        self.lis_txfi_dup = ['gfdzdh', 'fpdm', 'zfbz', 'xfdzdh', 'kprq', 'gfsbh', 'title', 'gfyhzh', 'content',
                        'file_path', 'jqbh', 'jshj', 'memo', 'cycs', 'xfsbh', 'je', 'gfmc', 'fpzl', 'bz', 'fphm',
                        'xfmc', 'xfyhzh', 'jym', 'se', 'txfbz', 'create_time', 'cpybz', 'zfbz_new']
        # 通行费14 detail
        self.lis_txfd = ['tszcbs', 'hwmc', 'slv', 'sjsl', 'je', 'se', 'sjse', 'cph', 'txrqq', 'lx', 'txrqz']
        self.lis_txfd_dup = ['hwmc', 'slv', 'je', 'se', 'cph', 'txrqq', 'lx', 'txrqz']

        # 机动车03 invoice
        self.lis_jdci = ['zh', 'sjsl', 'memo', 'xcrs', 'fpdm', 'zfbz', 'sjdh', 'kprq', 'gfsbh', 'fdjhm', 'swjg_dm',
                    'skph', 'content', 'dkbz', 'tszcbs', 'title', 'wspzhm', 'cjfy', 'sjse', 'file_path', 'jqbh',
                    'hgzs', 'jshj', 'dh', 'cjhm', 'cycs', 'xhdwmc', 'dz', 'cllx', 'xfsbh', 'dw', 'cd', 'fpzl',
                    'sfzhm', 'fphm', 'jkzmsh', 'khyh', 'swjg_mc', 'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'ghdw', 'zfbz_new']
        self.lis_jdci_dup = ['zh', 'sjsl', 'memo', 'xcrs', 'fpdm', 'zfbz', 'sjdh', 'kprq', 'gfsbh', 'fdjhm', 'swjg_dm',
                        'skph', 'content', 'dkbz', 'tszcbs', 'title', 'wspzhm', 'cjfy', 'sjse', 'file_path', 'jqbh',
                        'hgzs', 'jshj', 'dh', 'cjhm', 'cycs', 'xhdwmc', 'dz', 'cllx', 'xfsbh', 'dw', 'cd', 'fpzl',
                        'sfzhm', 'fphm', 'jkzmsh', 'khyh', 'swjg_mc', 'nsrsbh', 'zzssl', 'cpxh', 'zzsse', 'ghdw',
                        'create_time', 'zfbz_new']

        # 二手车15 invoice
        self.lis_esci = ['xfsbh', 'xfdh', 'memo', 'fpdm', 'zfbz', 'jyyhzh', 'kprq', 'xfdw', 'gfsbh', 'gfhm', 'jysbh',
                    'skph', 'tszcbs', 'title', 'scdh', 'scmc', 'xfhm', 'content', 'cgsmc', 'file_path', 'jqbh',
                    'cjhm', 'cjhj', 'cycs', 'cllx', 'sjsl', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'sjse', 'jydw', 'fphm',
                    'gfdw', 'gfdz', 'xfdz', 'jydz', 'scsbh', 'cpxh', 'jydh', 'djzh', 'gfdh', 'scdz', 'cpzh', 'zfbz_new']
        self.lis_esci_dup = ['xfsbh', 'xfdh', 'memo', 'fpdm', 'zfbz', 'jyyhzh', 'kprq', 'xfdw', 'gfsbh', 'gfhm', 'jysbh',
                        'skph', 'tszcbs', 'title', 'scdh', 'scmc', 'xfhm', 'content', 'cgsmc', 'file_path', 'jqbh',
                        'cjhm', 'cjhj', 'cycs', 'cllx', 'sjsl', 'scyhzh', 'dkbz', 'fpzl', 'bz', 'sjse', 'jydw', 'fphm',
                        'gfdw', 'gfdz', 'xfdz', 'jydz', 'scsbh', 'cpxh', 'jydh', 'djzh', 'gfdh', 'scdz', 'cpzh',
                        'create_time', 'zfbz_new']

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

    def check(self, content, department_id, fpzl):
        api = '/api/v1/invoice/check'
        data = {}
        data['company_key'] = self.company_key
        data['nonce_str'] = self.get_nonce_str()
        data['content'] = content
        data['department_id'] = department_id
        data['sign'] = self.sign_action(self.c_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = ['01', '04', '10', '11', '14']
        b = ['03', '15']
        dic_data = json.loads(r.text)
        if fpzl in a:
            if dic_data['code'] == 0:
                lis10 = list(dic_data.keys())
                lis11 = dic_data.get('data')
                lis12 = dic_data.get('data').get('data')
                lis13 = dic_data.get('data').get('data').get('invoice')
                lis14 = dic_data.get('data').get('data').get('invoice_detail')[0]
                lis_f = None
            elif dic_data['code'] == 20509:
                lis10 = list(dic_data.keys())
                lis11 = dic_data.get('data')
                lis_f = dic_data.get('data').get('forbidens')
                lis12 = dic_data.get('data').get('data')
                lis13 = dic_data.get('data').get('data').get('invoice')
                lis14 = dic_data.get('data').get('data').get('invoice_detail')[0]
            else:
                raise 'code={}'.format(dic_data['code'])

        elif fpzl in b:
            if dic_data['code'] == 0:
                lis10 = list(dic_data.keys())
                lis11 = dic_data.get('data')
                lis12 = dic_data.get('data').get('data')
                lis13 = dic_data.get('data').get('data').get('invoice')
                lis14 = None
                lis_f = None
            elif dic_data['code'] == 20509:
                lis10 = list(dic_data.keys())
                lis11 = dic_data.get('data')
                lis_f = dic_data.get('data').get('forbidens')
                lis12 = dic_data.get('data').get('data')
                lis13 = dic_data.get('data').get('data').get('invoice')
                lis14 = None
            else:
                raise 'code={}'.format(dic_data['code'])
        else:
            raise "发票种类输入有误"
        return r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f

    def test_v1_zyfp(self):  # code=0,01专票
        content = ',,6100193130,05996229,130.19,20191016,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='专票Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='专票data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='专票data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='专票invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='专票detail differ')

    def test_v1_ptfp(self):  # code=0,04普票
        content = ',,033001800204,67078756,,20191008,149182,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '04'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='普票Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='普票data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='普票data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='普票invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='普票detail differ')

    def test_v1_dzfp(self):  # code=0,10电票
        content = ',,011001900211,96042929,,20191011,386840,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '10'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='电票Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='电票data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='电票data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='电票invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='电票detail differ')

    def test_v1_jsfp(self):  # code=0,11卷票
        content = ',,032001800107,10086247,,20190924,10207336584494920023,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '11'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='卷票Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='卷票data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='卷票data_data differ')
        self.assertListEqual(sorted(self.lis_jsi), sorted(list(lis13.keys())), msg='卷票invoice differ')
        self.assertListEqual(sorted(self.lis_jsd), sorted(list(lis14.keys())), msg='卷票detail differ')

    def test_v1_txfp(self):  # code=0,14通行费
        content = ',,041001800112,61621475,52.57,20191003,612228,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '14'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='通行费Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='通行费data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='通行费data_data differ')
        self.assertListEqual(sorted(self.lis_txfi), sorted(list(lis13.keys())), msg='通行费invoice differ')
        self.assertListEqual(sorted(self.lis_txfd), sorted(list(lis14.keys())), msg='通行费detail differ')

    def test_v1_jdcp(self):  # code=0,03机动车
        content = ',,121001821071,00379350,82300.88,20191010,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '03'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='机动车Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='机动车data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='机动车data_data differ')
        self.assertListEqual(sorted(self.lis_jdci), sorted(list(lis13.keys())), msg='机动车invoice differ')

    def test_v1_escp(self):  # code=0,15二手车
        content = ',,044001900517,00142576,10000.00,20190909,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '15'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 0)
        self.assertEqual(dic_data['msg'], '成功')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='二手车Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='二手车data differ')
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='二手车data_data differ')
        self.assertListEqual(sorted(self.lis_esci), sorted(list(lis13.keys())), msg='二手车invoice differ')

    def test_v1_zyfp_dup(self):  # code=20509_重复录入,01专票
        content = ',,2300191130,02508400,772.82,20191012,772.82,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='专票重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='专票重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='专票重复录入data_data differ')
        self.assertListEqual(sorted(self.lis03_dup), sorted(list(lis13.keys())), msg='专票重复录入invoice differ')
        self.assertListEqual(sorted(self.lis04_dup), sorted(list(lis14.keys())), msg='专票重复录入detail differ')

    def test_v1_ptfp_dup(self):  # code=20509_重复录入,04普票
        content = ',,045001900104,05805040,,20190403,116862,,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '04'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='普票重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='普票重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='普票重复录入data_data differ')
        self.assertListEqual(sorted(self.lis03_dup), sorted(list(lis13.keys())), msg='普票重复录入invoice differ')
        self.assertListEqual(sorted(self.lis04_dup), sorted(list(lis14.keys())), msg='普票重复录入detail differ')

    def test_v1_dzfp_dup(self):  # code=20509_重复录入,10电票
        content = '01,10,011001900311,86771359,244.50,20191015,09410951332856553793,483C,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '10'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='电票重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='电票重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='电票重复录入data_data differ')
        self.assertListEqual(sorted(self.lis03_dup), sorted(list(lis13.keys())), msg='电票重复录入invoice differ')
        self.assertListEqual(sorted(self.lis04_dup), sorted(list(lis14.keys())), msg='电票重复录入detail differ')

    def test_v1_jsfp_dup(self):  # code=20509_重复录入,11卷票
        content = ',,034001800107,28860153,,20190831,869966,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '11'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='卷票重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='卷票重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='卷票重复录入data_data differ')
        self.assertListEqual(sorted(self.lis_jsi_dup), sorted(list(lis13.keys())), msg='卷票重复录入invoice differ')
        self.assertListEqual(sorted(self.lis_jsd_dup), sorted(list(lis14.keys())), msg='卷票重复录入detail differ')

    def test_v1_txfp_dup(self):  # code=20509_重复录入,14通行费
        content = ',,044001700112,74191042,38.83,20190308,966016,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '14'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='通行费重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='通行费重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='通行费重复录入data_data differ')
        self.assertListEqual(sorted(self.lis_txfi_dup), sorted(list(lis13.keys())), msg='通行费重复录入invoice differ')
        self.assertListEqual(sorted(self.lis_txfd_dup), sorted(list(lis14.keys())), msg='通行费重复录入detail differ')

    def test_v1_jdcp_dup(self):  # code=20509_重复录入,03机动车
        content = ',,143001820660,00713846,32300.88,20191015,,,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        fpzl = '03'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='机动车重复录入Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='机动车重复录入data differ')
        self.assertFalse(lis_f[0], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='机动车重复录入data_data differ')
        self.assertListEqual(sorted(self.lis_jdci_dup), sorted(list(lis13.keys())), msg='机动车重复录入invoice differ')

    # v1/check 查验重复录入二手车有问题
    # def test_v1_escp_dup(self):  # code=20509_重复录入,15二手车   有问题
    #     content = ',,037021900117,00100675,91600,20190606,,'
    #     department_id = '834e1268b41143c78070331d6da23c1b'
    #     fpzl = '15'
    #     r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
    #     print(r.text)
    #     self.assertIs(r.status_code, 200)
    #     self.assertEqual(dic_data['code'], 20509)
    #     self.assertEqual(dic_data['msg'], '禁止录入')
    #     self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='二手车重复录入Obj differ')
    #     self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='二手车重复录入data differ')
    #     self.assertFalse(lis_f[0], msg=None)
    #     self.assertTrue(lis_f[1], msg=None)
    #     self.assertFalse(lis_f[2], msg=None)
    #     self.assertFalse(lis_f[3], msg=None)
    #     self.assertFalse(lis_f[4], msg=None)
    #     self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='二手车重复录入data_data differ')
    #     self.assertListEqual(sorted(self.lis_esci_dup), sorted(list(lis13.keys())), msg='二手车重复录入invoice differ')

    def test_v1_zpjy(self):  # code=20509  税号校验
        content = ',,3200191130,45090173,183874.79,20191015,,'
        department_id = '316ceafee65f40a39adbde80f25ac8c3'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='税号校验Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='税号校验data differ')
        self.assertTrue(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='税号校验data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='税号校验invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='税号校验detail differ')

    def test_v1_zp_g_black(self):   #code=20509   货物黑名单
        content = ',,3200191130,45090174,1814.24,20191015,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='货物黑名单Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='货物黑名单data differ')
        self.assertTrue(lis_f[2], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='货物黑名单data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='货物黑名单invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='货物黑名单detail differ')

    def test_v1_zp_c_black(self):   #code=20509   企业黑名单
        content = ',,4403191130,01796072,452.83,20191015,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='企业黑名单Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='企业黑名单data differ')
        self.assertTrue(lis_f[3], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[4], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='企业黑名单data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='企业黑名单invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='企业黑名单detail differ')

    def test_v1_zp_sxjy(self):   #code=20509  四项校验
        content = ',,4300181160,00351585,1407.77,20191014,,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='企业黑名单Obj differ')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='企业黑名单data differ')
        self.assertTrue(lis_f[4], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='企业黑名单data_data differ')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='企业黑名单invoice differ')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='企业黑名单detail differ')

    def test_v1_zp_c_black_w(self):    #开启四项校验，企业黑名单，白名单
        content = ',,3200191130,45090095,107658.72,20191012,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='第一层字段有误')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='第二层字段有误')
        self.assertTrue(lis_f[4], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertTrue(lis_f[3], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='第三层字段有误')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='第四层字段有误')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='第五层字段有误')

    def test_v1_zp_w_dup(self):   #四项校验，白名单  重复录入
        content = ',,1300191130,02313838,815.09,20191011,,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='第一层字段有误')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='第二层字段有误')
        self.assertTrue(lis_f[4], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertTrue(lis_f[1], msg=None)
        self.assertListEqual(sorted(self.lis02_dup), sorted(list(lis12.keys())), msg='第三层字段有误')
        self.assertListEqual(sorted(self.lis03_dup), sorted(list(lis13.keys())), msg='第四层字段有误')
        self.assertListEqual(sorted(self.lis04_dup), sorted(list(lis14.keys())), msg='第五层字段有误')

    def test_v1_zp_w(self):   #四项校验  白名单
        content = ',,3702191130,07232088,504.85,20191013,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        fpzl = '01'
        r, lis10, lis11, lis12, lis13, lis14, dic_data, lis_f = self.check(content, department_id, fpzl)
        print(r.text)
        self.assertIs(r.status_code, 200)
        self.assertEqual(dic_data['code'], 20509)
        self.assertEqual(dic_data['msg'], '禁止录入')
        self.assertListEqual(sorted(self.lis00), sorted(lis10), msg='第一层字段有误')
        self.assertListEqual(sorted(self.lis01), sorted(list(lis11.keys())), msg='第二层字段有误')
        self.assertTrue(lis_f[4], msg=None)
        self.assertFalse(lis_f[0], msg=None)
        self.assertFalse(lis_f[1], msg=None)
        self.assertFalse(lis_f[2], msg=None)
        self.assertFalse(lis_f[3], msg=None)
        self.assertListEqual(sorted(self.lis02), sorted(list(lis12.keys())), msg='第三层字段有误')
        self.assertListEqual(sorted(self.lis03), sorted(list(lis13.keys())), msg='第四层字段有误')
        self.assertListEqual(sorted(self.lis04), sorted(list(lis14.keys())), msg='第五层字段有误')

    def tearDown(self):
        self.data.clear()

























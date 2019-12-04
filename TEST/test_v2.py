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

        # 集团测试生产-110
        # company_key = 'af6bce91-0eec-409b-9627-754d23dd087c'
        # c_secret = 'b04be205-3953-4e9c-b037-1fae320c33ca'

        # 集团测试生产-zhanglu
        # self.company_key = '87a7da63-0515-4c36-b198-aec8de94d80c'
        # self.c_secret = '5923a209-93b1-4288-98e5-35a908cba33f'

        #api测试集团
        self.company_key = 'c58fafe5-9092-41ed-9276-120b962f65cc'
        self.c_secret = '2f12bc36-b8d0-4298-99c2-dbcefac1ba0d'

        # 非集团-maohuade@deallinker.cn
        # self.company_key = 'c36918bf-61c9-4002-b455-36327887eb8c'
        # self.c_secret = 'c7ef8334-a4c7-4536-a1c9-acab12714a04'

        #v2check
        #专票/普票/电票
        self.list_zp_1 = ['msg', 'code', 'data']
        self.list_zp_2 = ['invoiceid', 'forbidens', 'invoice', 'invoice_detail']
        self.list_zp_3_invoice =  [u"gfdzdh", u"txfbz", u"cpybz", u"fpdm", u"zfbz", u"zfbz_new", u"xfdzdh", u"kprq", u"gfsbh",
                            u"title", u"gfyhzh", u"jqbh", u"jshj", u"memo", u"tags", u"cycs", u"xfsbh", u"je", u"gfmc",
                            u"fpzl", u"bz", u"fphm", u"xfmc", u"xfyhzh", u"jym", u"se", u"dkbz", u"file_path", u"content"]
        self. list_zp_3_invoice_dup = [u"gfdzdh", u"txfbz", u"cpybz", u"fpdm", u"zfbz", u"zfbz_new", u"xfdzdh", u"kprq", u"gfsbh",
                            u"title", u"gfyhzh", u"jqbh", u"jshj", u"memo", u"tags", u"cycs", u"xfsbh", u"je", u"gfmc",
                            u"fpzl", u"bz", u"fphm", u"xfmc", u"xfyhzh", u"jym", u"se", u"dkbz", u"file_path", u"content"]
        self.list_zp_3_invoice_detail = [u"dj", u"ggxh", u"hwmc", u"slv", u"dw", u"sl", u"je", u"se", u"tszcbs", u"sjsl", u"sjse"]
        self.list_zp_3_invoice_detail_dup = [u"dj", u"ggxh", u"hwmc", u"slv", u"dw", u"sl", u"je", u"se", u"tszcbs", u"sjsl", u"sjse"]

        #通行费
        self.list_tp_1 = ['msg', 'code', 'data']
        self.list_tp_2 = ['invoiceid', 'forbidens', 'invoice', 'invoice_detail']
        self.list_tp_3_invoice = [u"gfdzdh", u"txfbz", u"cpybz", u"fpdm", u"zfbz", u"zfbz_new", u"xfdzdh", u"kprq", u"gfsbh",
                            u"title", u"gfyhzh", u"jqbh", u"jshj", u"memo", u"tags", u"cycs", u"xfsbh", u"je", u"gfmc",
                            u"fpzl", u"bz", u"fphm", u"xfmc", u"xfyhzh", u"jym", u"se", u"dkbz", u"file_path", u"content"]
        self.list_tp_3_invoice_detail = [u"cph", u"hwmc", u"slv", u"txrqq", u"txrqz", u"je", u"lx", u"se", u"tszcbs", u"sjsl", u"sjse"]

        #机动车票
        self.list_jip_1 = ['msg', 'code', 'data']
        self.list_jip_2 = ['invoiceid', 'forbidens', 'invoice', 'invoice_detail']
        self.list_jip_3_invoice =  [u"swjg_dm", u"memo", u"tags", u"xcrs", u"fpdm", u"zfbz", u"kprq", u"fdjhm", u"gfsbh",
                               u"zh", u"skph", u"sjdh", u"title", u"wspzhm", u"cjfy", u"jqbh", u"hgzs", u"jshj", u"dh",
                               u"cjhm", u"khyh", u"cycs", u"jkzmsh", u"dz", u"cllx", u"xfsbh", u"dw", u"cd", u"fpzl",
                               u"sfzhm", u"fphm", u"xhdwmc", u"ghdw", u"nsrsbh", u"zzssl", u"cpxh", u"zzsse", u"swjg_mc",
                               u"dkbz", u"tszcbs", u"sjsl", u"sjse", u"file_path", u"content"]
        self.list_jip_3_invoice_dup = [u"swjg_dm", u"memo", u"tags", u"xcrs", u"fpdm", u"zfbz", u"kprq", u"fdjhm", u"gfsbh",
                               u"zh", u"skph", u"sjdh", u"title", u"wspzhm", u"cjfy", u"jqbh", u"hgzs", u"jshj", u"dh",
                               u"cjhm", u"khyh", u"cycs", u"jkzmsh", u"dz", u"cllx", u"xfsbh", u"dw", u"cd", u"fpzl",
                               u"sfzhm", u"fphm", u"xhdwmc", u"ghdw", u"nsrsbh", u"zzssl", u"cpxh", u"zzsse", u"swjg_mc",
                               u"dkbz", u"tszcbs", u"sjsl", u"sjse", u"file_path", u"content"]

        #二手车票
        self.list_erp_1 = ['msg', 'code', 'data']
        self.list_erp_2 = ['invoiceid', 'forbidens', 'invoice', 'invoice_detail']
        self.list_erp_3_invoice = [u"xfdh", u"fpdm", u"cgsmc", u"kprq", u"xfdw", u"gfhm", u"jysbh", u"djzh", u"title",
                               u"scsbh", u"scmc", u"xfhm", u"memo", u"tags", u"jydw", u"cjhm", u"cjhj", u"cycs", u"cllx",
                               u"scyhzh", u"cpzh", u"fpzl", u"scdz", u"fphm", u"gfdw", u"gfdz", u"jydz", u"scdh", u"cpxh",
                               u"xfdz", u"gfdh", u"jydh", u"dkbz", u"tszcbs",  u"sjsl", u"sjse", u"file_path", u"content"]

        #通行费20509重复录入
        self.list_tp_dup_1 = ['msg', 'code', 'data']
        self.list_tp_dup_2 = ['invoiceid', 'forbidens', 'invoice', 'invoice_detail']
        self.list_tp_dup_3_invoice = [u"gfdzdh", u"txfbz", u"cpybz", u"fpdm", u"zfbz", u"zfbz_new", u"xfdzdh", u"kprq", u"gfsbh",
                            u"title", u"gfyhzh", u"jqbh", u"jshj", u"memo", u"tags", u"cycs", u"xfsbh", u"je", u"gfmc",
                            u"fpzl", u"bz", u"fphm", u"xfmc", u"xfyhzh", u"jym", u"se", u"dkbz", u"file_path", u"content"]
        self.list_tp_dup_3_invoice_detail = [u"cph", u"hwmc", u"slv", u"txrqq", u"txrqz", u"je", u"lx", u"se", u"tszcbs", u"sjsl", u"sjse"]

        #专票20509 四项不一致，白名单，重复录入
        self.list_zp_3_invoice_dup = [u"gfdzdh", u"txfbz", u"cpybz", u"fpdm", u"zfbz", u"zfbz_new", u"xfdzdh", u"kprq", u"gfsbh",
                            u"title", u"gfyhzh", u"jqbh", u"jshj", u"memo", u"tags", u"cycs", u"xfsbh", u"je", u"gfmc",
                            u"fpzl", u"bz", u"fphm", u"xfmc", u"xfyhzh", u"jym", u"se", u"dkbz", u"file_path", u"content"]

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

    def check(self, content, department_id):
        api = '/api/v2/invoice/check'
        data = {}
        data['company_key'] = self.company_key
        data['nonce_str'] = self.get_nonce_str()
        data['content'] = content
        data['department_id'] = department_id
        data['check_only'] = '1'
        data['sign'] = self.sign_action(self.c_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        return r, a, list_

    def test_v2_zp_0(self):      #code=0,专票
        content = ',,4400192130,36041942,3805.31,20191019,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_pp_0(self):
        content = ',,033001800204,84937622,,20191018,020788'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]),
                             '第三层detail中字段有误')


    def test_v2_dp_0(self):
        content = ',,044031900111,85349950,,20191020,809202,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]),
                             '第三层detail中字段有误')

    def test_v2_jp_0(self):
        content = ',,033001951407,00410671,,20191006,140923,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_tp_0(self):
        content = ',,013001800112,07370857,16.17,20190308,010658,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_tp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_tp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_tp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_tp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]),
                             '第三层detail中字段有误')

    def test_v2_jip_0(self):
        content = ',,144031924160,00074593,55237.07,20181211,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_jip_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_jip_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_jip_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')


    def test_v2_erp_0(self):
        content = ',,045001800417,00068266,30000.00,20190401,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.list_erp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_erp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_erp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')

    def test_v2_zp_20509_tax(self):    # 抬头税号校验
        content = ',,012001900111,77689129,71.74,20191026,945340,'
        department_id = '316ceafee65f40a39adbde80f25ac8c3'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][0], msg='foebidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_zp_20509_dup(self):   #专票，重复录入
        content = '01,01,6100191130,14471383,89939.81,20190919,,CC37,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail_dup), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_pp_20509_dup(self):    # 普票，重复录入
        content = ',,4400174320,77073703,92511.03,20190916,811521,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail_dup), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_dp_20509_dup(self):   #电票，重复录入
        content = '01,10,012001900111,61445317,38.87,20191019,17649403362759500970,C375,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail_dup), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_jp_20509_dup(self):   #卷票，重复录入
        content = ',,050001800107,19834357,2742,20191022,865434,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail_dup), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_tp_20509_dup(self):   #通行费   重复录入
        content = ',,042001700112,21902566,24.87,20190308,224526,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_tp_dup_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_tp_dup_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_tp_dup_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_tp_dup_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层invoice_detail中字段有误')

    def test_v2_jip_20509_dup(self):   #机动车   重复录入
        content = ',,144001924160,00808958,36244.25,20190925,,,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_jip_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_jip_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_jip_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice中字段有误')

    def test_v2_erp_20509_dup(self):  # 二手车  重复录入
        content = ',,061001900117,00044936,73500.00,20190906,,'
        department_id = '834e1268b41143c78070331d6da23c1b'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_erp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_erp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_erp_3_invoice), sorted(a['data']['invoice']), '第三层字段有误')

    def test_v2_20509_g_black(self):    #货物黑名单
        content = ',,4100192130,07552855,291.07,20191011,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice字段中有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail字段中有误')

    def test_v2_20509_c_black(self):    #企业黑名单
        content = ',,1500191130,00572093,2405.66,20190816,,,'
        department_id = '95ee64d986fa404894574a00c00dd4a7'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_20509_sxjy(self):    #四项校验
        content = ',,4403191130,29935648,33982.30,20191013,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_v2_c_w_black(self):   #开启四项不一致，企业黑名单，白名单
        content = ',,4200192130,06139348,1631.07,20191017,,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertTrue(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice中字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')


    def test_v2_write_list(self):    #四项不一致，白名单  重复录入
        content = ',,4300192130,05246633,466.02,20190920,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertTrue(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertTrue(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_dup), sorted(a['data']['invoice']), '第三层invoice字段中有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail_dup), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def test_sx_write_list(self):   #四项不一致，白名单
        content = ',,033021900104,12130854,,20190911,455018,,'
        department_id = '846d0d323c184655918e89bb3a014abd'
        r, a, list_ = self.check(content, department_id)
        print(r.text)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20509, 'code不为20509')
        self.assertEqual(a['msg'], '禁止录入', 'msg信息不一致')
        self.assertFalse(a['data']['forbidens'][0], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][1], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][2], msg='forbidens有误')
        self.assertFalse(a['data']['forbidens'][3], msg='forbidens有误')
        self.assertTrue(a['data']['forbidens'][4], msg='forbidens有误')
        self.assertListEqual(sorted(self.list_zp_1), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.list_zp_2), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice), sorted(a['data']['invoice']), '第三层invoice字段中有误')
        self.assertListEqual(sorted(self.list_zp_3_invoice_detail), sorted(a['data']['invoice_detail'][0]), '第三层detail中字段有误')

    def tearDown(self):
        self.data.clear()






















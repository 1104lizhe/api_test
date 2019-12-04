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

        #批量签收,单张签收
        self.receive = ['code', 'data', 'msg']

        #返回进项发票信息
        self.dedu_invoice_1 = ['code', 'data', 'msg']
        self.dedu_invoice_2 = ['invoices', 'total_count', 'total_page']
        self.dedu_invoice_3 = ['jshj', 'fpzt', 'xfsbh', 'tax_period', 'fpdm', 'reason', 'deduction_state', 'kprq', 'gfsbh',
                               'je', 'gfmc', 'fpzl', 'fphm', 'deduction_date', 'deduction_result', 'received_user_id', 'xfmc',
                               'received_date', 'deduction_user_id', 'received_state', 'se']


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

    def test_receive_0(self):
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"},{"fpdm":"3200191130","fphm":"62468288"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '1ce5301ee2f542ca9ec2c510fdef5a72'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url+api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_(self):
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = '1ce5301ee2f542ca9ec2c510fdef5a72'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_reveice_21002_fphm(self):
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"},{"fpdm":"1100192130","fphm":""}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = '1ce5301ee2f542ca9ec2c510fdef5a72'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21002, 'code有误')
        self.assertEqual(a['msg'], 'fpdm或fphm参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_21002_state(self):
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '2'
        data['user_id'] = '1ce5301ee2f542ca9ec2c510fdef5a72'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21002, 'code有误')
        self.assertEqual(a['msg'], 'state参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_21004(self):
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '1ce5301ee2f542ca9ec2c510fdef5a71'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21004, 'code有误')
        self.assertEqual(a['msg'], '成员不存在', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_0_g(self):   #管理员角色
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389d'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_0_c(self):   #财务角色
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '834a0533a86e4696b838153c2dffee2b'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_20004(self):   #员工角色
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '1a32d22ec2ee431da373f9272556b536'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20004, 'code有误')
        self.assertEqual(a['msg'], '您无权限执行此操作', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_21004_d(self):   #错误的department_id
        data = {}
        api = '/api/v1/invoice/receive'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm_fphm'] = '[{"fpdm":"1100192130","fphm":"05379771"}]'
        data['department_id'] = '111'
        data['receive_state'] = '1'
        data['user_id'] = '1a32d22ec2ee431da373f9272556b536'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21004, 'code有误')
        self.assertEqual(a['msg'], '成员不存在', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_0(self):
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389d'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url+api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_0_state(self):
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389d'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_21004(self):
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc1'
        data['receive_state'] = '1'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389d'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21004, 'code有误')
        self.assertEqual(a['msg'], '成员不存在', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_21002(self):
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '2'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389d'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21002, 'code有误')
        self.assertEqual(a['msg'], 'state参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_21004_user(self):
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '1'
        data['user_id'] = '7d5afe2eddae4e94b37161ad8891389'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21004, 'code有误')
        self.assertEqual(a['msg'], '成员不存在', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_0_g(self):    #管理员角色
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = 'bba931d878fb4686a17a0d76973c3fbf'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_0_c(self):     #财务角色
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = '834a0533a86e4696b838153c2dffee2b'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    def test_receive_single_20004_y(self):    #员工角色
        data = {}
        api = '/api/v1/invoice/receive/single'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['fpdm'] = '1100192130'
        data['fphm'] = '05379771'
        data['department_id'] = '69cfcabcb6774ff6ac70c87bcade2fc6'
        data['receive_state'] = '0'
        data['user_id'] = 'b7517812324649aaa2b7746cdb104ed3'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20004, 'code有误')
        self.assertEqual(a['msg'], '您无权限执行此操作', 'msg不一致')
        self.assertListEqual(sorted(self.receive), sorted(a.keys()), '第一层字段有误')

    # def test_dedu_result_0(self):
    #     data = {}
    #     api = '/api/v2/deduction/result'
    #     data['company_key'] = self.company_key
    #     company_secret = self.c_secret
    #     data['nonce_str'] = self.get_nonce_str()
    #     data['tax_no'] = ''
    #     data['fpdm'] = ''
    #     data['fphm'] = ''
    #     data['fpzt'] = ''
    #     data['inv_start_date'] = ''
    #     data['inv_end_date'] = ''
    #     data['tax_period'] = ''
    #     data['received_start_date'] = ''
    #     data['received_end_date'] = ''
    #     data['deduction_start_date'] = ''
    #     data['deduction_end_date'] = ''
    #     data['received_user_id'] = ''
    #     data['received_state'] = ''
    #     data['deduction_state'] = ''
    #     data['page_num'] = ''
    #     data['page_size'] = ''
    #     data['sign'] = self.sign_action(company_secret, data)
    #     r = requests.post(url=self.url+api, data=data)
    #     a = r.json()
    #     print(a)





















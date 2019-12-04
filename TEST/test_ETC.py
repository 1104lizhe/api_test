from hashlib import md5
import requests
import json
import random
import unittest

class testETC(unittest.TestCase):
    def setUp(self):
        self.company_key = '87a7da63-0515-4c36-b198-aec8de94d80c'  # 集团333
        self.c_secret = '5923a209-93b1-4288-98e5-35a908cba33f'
        self.url = 'http://182.92.1.42:8081'

        #车辆备案
        self.list_car = ['msg', 'code', 'data']

        #运单开始
        self.order_start = ['code', 'data', 'msg']

        #运单结束
        self.order_end = ['code', 'data', 'msg']

        #查询数据
        self.invoice_1 = ['code', 'data', 'msg']
        self.invoice_2 = ['result', 'waybillEndTime', 'waybillStartTime', 'waybillNum', 'vehicleType', 'plateNum', 'waybillStatus',
                          'receiveTime', 'info']
        self.invoice_3 = ['sellerTaxpayerCode', 'invoiceType', 'plateNum', 'waybillNum', 'amount', 'invoiceMakeTime',
                          'invoiceHtmlUrl', 'waybillStatus', 'waybillStartTime', 'enStation', 'exTime', 'sellerName',
                          'transactionId', 'vehicleType', 'exStation', 'invoiceNum', 'invoiceUrl', 'invoiceCode', 'waybillEndTime',
                          'totalTaxAmount', 'fee', 'totalAmount', 'taxRate']

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

    def test_ETC_register_201(self):
        data = {}
        api = '/api/v1/vehicle/order/register'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['taxno'] = '91510104MA6C9DJN27'
        data['plate_number'] = '浙B1C6G9'
        data['plate_color'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 201, 'code有误')
        self.assertEqual(a['msg'], '该车牌不存在!', 'msg不一致')
        self.assertListEqual(sorted(self.list_car), sorted(a.keys()), '字段有误')

    def test_ETC_register_10030(self):
        data = {}
        api = '/api/v1/vehicle/order/register'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['taxno'] = '91510104MA6C9DJN27'
        data['plate_number'] = '沪D44558'
        data['plate_color'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10030, 'code有误')
        self.assertEqual(a['msg'], '车辆已备案!', 'msg不一致')
        self.assertListEqual(sorted(self.list_car), sorted(a.keys()), '字段有误')

    def test_ETC_register_10041(self):
        data = {}
        api = '/api/v1/vehicle/order/register'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['taxno'] = '91510104MA6C9DJN27'
        data['plate_number'] = '沪D44558'
        data['plate_color'] = '2'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10041, 'code有误')
        self.assertEqual(a['msg'], '仅支持黄色车牌!', 'msg不一致')
        self.assertListEqual(sorted(self.list_car), sorted(a.keys()), '字段有误')

    def test_ETC__register_10036(self):
        data = {}
        api = '/api/v1/vehicle/order/register'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['taxno'] = '9111010830656251681'
        # data['taxno'] = '91510104MA6C9DJN271'
        data['plate_number'] = '沪D44558'
        data['plate_color'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10036, 'code有误')
        self.assertEqual(a['msg'], '税号不存在!', 'msg不一致')
        self.assertListEqual(sorted(self.list_car), sorted(a.keys()), '字段有误')

    # def test_ETC__register_0(self):
    #     data = {}
    #     api = '/api/v1/vehicle/order/register'
    #     data['company_key'] = self.company_key
    #     company_secret = self.c_secret
    #     data['nonce_str'] = self.get_nonce_str()
    #     data['taxno'] = '91510104MA6C9DJN27'
    #     data['plate_number'] = '沪DP9769'
    #     data['plate_color'] = '1'
    #     data['sign'] = self.sign_action(company_secret, data)
    #     r = requests.post(url=self.url + api, data=data)
    #     a = r.json()
    #     print(a)
    #     self.assertEqual(r.status_code, 200, '返回response有误')
    #     self.assertEqual(a['code'], 0, 'code有误')
    #     self.assertEqual(a['msg'], '成功', 'msg不一致')
    #     self.assertListEqual(sorted(self.list_car), sorted(a.keys()), '字段有误')

    def test_ETC_order_start_0(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        n = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019' + n
        data['plate_number'] = '沪DP9769'
        data['plate_color'] = '1'
        data['start_time'] = '2019-11-22T12:58:10'
        data['source_addr'] = 'test1地方'
        data['predict_end_time'] = '2019-11-22T17:58:12'
        data['dest_addr'] = 'test2地方'
        data['fee'] = '100'
        data['taxno'] = '91510104MA6C9DJN27'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')
        print('运单结束接口开始调用')
        self.ETC_order_end_0(n)
        print('运单结束接口调用完毕')

    def test_ETC_order_start_10031(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019gCTopj'
        data['plate_number'] = '冀B0U9Y51'
        data['plate_color'] = '1'
        data['start_time'] = '2019-11-05T12:58:10'
        data['source_addr'] = 'test1'
        data['predict_end_time'] = '2019-11-06T17:58:12'
        data['dest_addr'] = 'test2'
        data['fee'] = '100'
        data['taxno'] = '91510104MA6C9DJN27'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10031, 'code有误')
        self.assertEqual(a['msg'], '车辆未备案!', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')

    def test_ETC_order_start_10036(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019'
        data['plate_number'] = '冀B0U9Y5'
        data['plate_color'] = '1'
        data['start_time'] = '2019-11-05T12:58:10'
        data['source_addr'] = 'test1'
        data['predict_end_time'] = '2019-11-06T17:58:12'
        data['dest_addr'] = 'test2'
        data['fee'] = '100'
        data['taxno'] = '9111010830656251681'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10036, 'code有误')
        self.assertEqual(a['msg'], '税号不存在!', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')

    def test_ETC_order_start_(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019'
        data['plate_number'] = '沪DP9769'
        data['plate_color'] = '1'
        data['start_time'] = '2022-11-05T12:58:10'
        data['source_addr'] = 'test1'
        data['predict_end_time'] = '2022-11-06T17:58:12'
        data['dest_addr'] = 'test2'
        data['fee'] = '100'
        data['taxno'] = '91510104MA6C9DJN27'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 201, 'code有误')
        self.assertEqual(a['msg'], '开始时间不能晚于当前时间!', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')

    def test_ETC_order_start_201(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019'
        data['plate_number'] = '沪DP9769'
        data['plate_color'] = '1'
        data['start_time'] = '2019-11-03T12:58:10'
        data['source_addr'] = 'test1'
        data['predict_end_time'] = '2018-11-06T17:58:12'
        data['dest_addr'] = 'test2'
        data['fee'] = '100'
        data['taxno'] = '91510104MA6C9DJN27'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 201, 'code有误')
        self.assertEqual(a['msg'], '结束不能早于开始时间!', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')

    def test_ETC_order_start_10037(self):
        data = {}
        api = '/api/v1/vehicle/order/start'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019gCTopj'
        data['plate_number'] = '沪DP9769'
        data['plate_color'] = '1'
        data['start_time'] = '2019-11-03T12:58:10'
        data['source_addr'] = 'test1'
        data['predict_end_time'] = '2019-11-03T17:58:12'
        data['dest_addr'] = 'test2'
        data['fee'] = '100'
        data['taxno'] = '91510104MA6C9DJN27'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10037, 'code有误')
        self.assertEqual(a['msg'], '运单编号已存在!', 'msg不一致')
        self.assertListEqual(sorted(self.order_start), sorted(a.keys()), '字段有误')

    def test_ETC_order_end_10033(self):
        data = {}
        api = '/api/v1/vehicle/order/end'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = '2365765'
        data['real_dest_addr'] = 'home'
        data['end_time'] = '2019-11-22T18:58:12'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10033, 'code有误')
        self.assertEqual(a['msg'], '运单已完成!', 'msg不一致')
        self.assertListEqual(sorted(self.order_end), sorted(a.keys()), '字段有误')

    def test_ETC_order_end_10032(self):
        data = {}
        api = '/api/v1/vehicle/order/end'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019110119170038'
        data['real_dest_addr'] = 'home'
        data['end_time'] = '2019-11-03T18:58:12'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10032, 'code有误')
        self.assertEqual(a['msg'], '运单不存在!', 'msg不一致')
        self.assertListEqual(sorted(self.order_end), sorted(a.keys()), '字段有误')

    def test_ETC_order_end_(self):
        data = {}
        api = '/api/v1/vehicle/order/end'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = '434ydfdfh'
        data['real_dest_addr'] = 'home'
        data['end_time'] = '2022-11-05T18:58:12'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 201, 'code有误')
        self.assertEqual(a['msg'], '结束不能晚于当前时间!', 'msg不一致')
        self.assertListEqual(sorted(self.order_end), sorted(a.keys()), '字段有误')

    def test_ETC_order_end_201(self):
        data = {}
        api = '/api/v1/vehicle/order/end'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = '434ydfdfh'
        data['real_dest_addr'] = 'home'
        data['end_time'] = '2019-10-01T18:58:12'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 201, 'code有误')
        self.assertEqual(a['msg'], '结束不能早于开始时间!', 'msg不一致')
        self.assertListEqual(sorted(self.order_end), sorted(a.keys()), '字段有误')

    def ETC_order_end_0(self, n):
        data = {}
        api = '/api/v1/vehicle/order/end'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_2019' + n
        data['real_dest_addr'] = 'home'
        data['end_time'] = '2019-11-22T18:58:12'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code有误')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.order_end), sorted(a.keys()), '字段有误')

    def test_ETC_invoice_0(self):
        data = {}
        api = '/api/v1/vehicle/order/invoice'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = '0'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.invoice_1), sorted(a.keys()), '第一层字段有误')
        self.assertListEqual(sorted(self.invoice_2), sorted(a['data']), '第二层字段有误')
        # self.assertListEqual(sorted(self.invoice_3), sorted(a['data']['result'][0]), '第三层字段有误')

    def test_ETC_invoice_10032(self):
        data = {}
        api = '/api/v1/vehicle/order/invoice'
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['num'] = 'YFXCYB_333_1614_29_20192'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10032, 'code不为10032')
        self.assertEqual(a['msg'], '运单不存在!', 'msg不一致')




















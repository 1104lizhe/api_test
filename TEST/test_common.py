import unittest
from hashlib import md5
import requests
import json
import base64
import random
import time
import datetime

class Integration(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.feeclouds.com'
        # self.data = {}
        self.company_key = 'af6bce91-0eec-409b-9627-754d23dd087c'  # af6bce91-0eec-409b-9627-754d23dd087c生产
        self.c_secret = 'b04be205-3953-4e9c-b037-1fae320c33ca'  # b04be205-3953-4e9c-b037-1fae320c33ca

        # 获取部门
        self.hqbm01 = ['msg', 'code', 'data']  # 第一层
        self.hqbm02 = ['count', 'rows']  # 第二层
        self.hqbm03 = ['parent_id', 'department_name', 'is_branch', 'department_id', 'tax_no']  # 第三层

        #获取成员
        self.hqcy01 = ['msg', 'code', 'data']  # 第一层
        self.hqcy02 = ['count', 'rows']   #第二层
        self.hqcy03 = ['user_id', 'email', 'realname', 'number']   #第三层

        #新增成员
        self.xzcy01 = ['msg', 'code', 'data']   #第一层
        self.xzcy02 = ['user_id']    #第二层

        #更新成员
        self.gxcy01 = ['msg', 'code', 'data']

        #新增部门
        self.xzbm01 = ['msg', 'code', 'data']
        self.xzbm02 = ['department_id']

        #更新部门
        self.gxbm01 = ['msg', 'code', 'data']

        #服务余额查询
        self.fwye01 = ['msg', 'code', 'data']
        self.fwye02 = ['quota_type', 'quota', 'used', 'expiry_date']

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

    def test_department_0(self):
        api = '/api/v1/department'  # 获取部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['page_num'] = 1
        data['page_size'] = 100
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.hqbm01), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.hqbm02), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.hqbm03), sorted(a['data']['rows'][0]), '第三层字段有误')

    def test_department_21000(self):
        api = '/api/v1/department'  # 获取部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['page_num'] = 0.1
        data['page_size'] = 100
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21000, 'code不为21000')
        self.assertEqual(a['msg'], '签名错误', 'msg不一致')
        self.assertListEqual(sorted(self.hqbm01), sorted(list_), '第一层字段有误')

    def test_user_0(self):
        api = '/api/v1/user'  # 获取成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['department_id'] = '363a2d4bb727489981a4e4571b6d1359'
        data['page_num'] = 1
        data['page_size'] = 100
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.hqcy01), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.hqcy02), sorted(a['data']), '第二层字段有误')
        self.assertListEqual(sorted(self.hqcy03), sorted(a['data']['rows'][0]), '第三层字段有误')


    def test_user_21000(self):
        api = '/api/v1/user'  # 获取成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['department_id'] = '363a2d4bb727489981a4e4571b6d1359'
        data['page_num'] = 0.1
        data['page_size'] = 100
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21000, 'code不为21000')
        self.assertEqual(a['msg'], '签名错误', 'msg不一致')
        self.assertListEqual(sorted(self.hqcy01), sorted(list_), '第一层字段有误')

    def test_user_21003(self):
        api = '/api/v1/user'  # 获取成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['department_id'] = '363a2d4bb727489981a4e4571b6d13590'
        data['page_num'] = 1
        data['page_size'] = 100
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21003, 'code不为21003')
        self.assertEqual(a['msg'], '部门不存在', 'msg不一致')
        self.assertListEqual(sorted(self.hqcy01), sorted(list_), '第一层字段有误')

    def test_user_add_0(self):
        api = '/api/v1/add/user'  # 新增成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['is_login'] = '1'
        name = self.get_nonce_str()
        name += '@qq.com'
        data['username'] = name
        data['realname'] = '李哲'
        data['password'] = '1'
        data['role'] = '1'
        data['target_department_id'] = '363a2d4bb727489981a4e4571b6d1359'
        # data['is_sys_sync'] = '1'
        # data['user_id'] = '23'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.xzcy01), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.xzcy02), sorted(a['data']), '第二层字段有误')

    def test_user_add_21000(self):
        api = '/api/v1/add/user'  # 新增成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['is_login'] = '1'
        data['usernamee'] = 'leelz@qq.com'
        data['realname'] = '李哲'
        data['password'] = '1'
        data['role'] = '1'
        data['target_department_id'] = '363a2d4bb727489981a4e4571b6d1359'
        # data['is_sys_sync'] = '1'
        # data['user_id'] = '23'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21000, 'code不为21000')
        self.assertEqual(a['msg'], '签名错误', 'msg不一致')
        self.assertListEqual(sorted(self.xzcy01), sorted(list_), '第一层字段有误')

    def test_user_add_10002(self):
        api = '/api/v1/add/user'  # 新增成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['is_login'] = '11'
        data['username'] = 'leelz@qq.com'
        data['realname'] = '李哲'
        data['password'] = '1'
        data['role'] = '1'
        data['target_department_id'] = '363a2d4bb727489981a4e4571b6d1359'
        # data['is_sys_sync'] = '1'
        # data['user_id'] = '23'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 10002, 'code不为10002')
        self.assertEqual(a['msg'], 'is_login参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.xzcy01), sorted(list_), '第一层字段有误')


    def test_user_add_20001(self):
        api = '/api/v2/add/user'  # 新增成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['is_login'] = '1'
        data['username'] = 'lzzzz@deallinker.cn'
        data['realname'] = '李哲'
        data['password'] = '1'
        data['role'] = '1'
        data['number'] = 'ddsjs'
        data['target_department_ids'] = '363a2d4bb727489981a4e4571b6d1359'
        # data['is_sys_sync'] = '1'
        # data['user_id'] = '23'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20001, 'code不为20001')
        self.assertEqual(a['msg'], '用户已存在', 'msg不一致')
        self.assertListEqual(sorted(self.xzcy01), sorted(list_), '第一层字段有误')

    def test_user_add_20303(self):
        api = '/api/v1/add/user'  # 新增成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['is_login'] = '1'
        data['username'] = 'lzzzza@deallinker.cn'
        data['realname'] = '李哲'
        data['password'] = '1'
        data['role'] = '1'
        data['target_department_id'] = '363a2d4bb727489981a4e4571b6d13590'
        # data['is_sys_sync'] = '1'
        # data['user_id'] = '23'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20303, 'code不为20303')
        self.assertEqual(a['msg'], '部门不存在', 'msg不一致')
        self.assertListEqual(sorted(self.xzcy01), sorted(list_), '第一层字段有误')

    def test_user_edit_0(self):
        api = '/api/v2/user/edit'  # 更新成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['targets'] = '[{"user_id":"f719d0247a9c444fa0e2d9e7f581d977","department_ids":"363a2d4bb727489981a4e4571b6d1359","username":"lll@deallinker.cn","is_link":0}]'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        print(a)
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.gxcy01), sorted(list_), '第一层字段有误')

    def test_user_edit_21002(self):
        api = '/api/v1/user/edit'  # 更新成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        # data['targets'] = '[{"user_id":"62895f97566a4bd6a8ade3f1025b10be","department_id":"363a2d4bb727489981a4e4571b6d1359","username":"lll@deallinker.cn"}]'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21002, 'code不为21002')
        self.assertEqual(a['msg'], 'target参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.gxcy01), sorted(list_), '第一层字段有误')

    def test_user_edit_20007(self):
        api = '/api/v1/user/edit'  # 更新成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['targets'] = '[{"user_id":"f719d0247a9c444fa0e2d9e7f581d977","department_id":"363a2d4bb727489981a4e4571b6d1359","username":"lll@deallinker.cn"}]'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20007, 'code不为20007')
        self.assertEqual(a['msg'], '登录名已经被占用', 'msg不一致')
        self.assertListEqual(sorted(self.gxcy01), sorted(list_), '第一层字段有误')

    def test_user_edit_21009(self):
        api = '/api/v1/user/edit'  # 更新成员接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['targets'] = '[{"user_id":"62895f97566a4bd6a8ade3f1025b10be","department_id":"343aa7ee6b84484b9353a73e7390604c","username":"lll@deallinker.cn"}]'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21009, 'code不为21009')
        self.assertEqual(a['msg'], 'department_id参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.gxcy01), sorted(list_), '第一层字段有误')

    def test_department_add_0(self):
        api = '/api/v1/department/add'  # 新增部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        name = self.get_nonce_str()
        name = '新增的部门' + name
        data['name'] = name
        data['parent_id'] = 'dea0dd24e606464e8abdf837b64090ff'
        # data['department_id'] = '100'
        # data['is_sys_sync'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'code不为0')
        self.assertListEqual(sorted(self.xzbm01), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.xzbm02), sorted(a['data']), '第二层字段有误')

    def test_department_add_21000(self):
        api = '/api/v1/department/add'  # 新增部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['namew'] = '新增的部门01'
        data['parent_id'] = 'dea0dd24e606464e8abdf837b64090ff'
        # data['department_id'] = '100'
        # data['is_sys_sync'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21000, 'code不为21000')
        self.assertEqual(a['msg'], '签名错误', 'msg不一致')
        self.assertListEqual(sorted(self.xzbm01), sorted(list_), '第一层字段有误')

    def test_department_add_20302(self):
        api = '/api/v1/department/add'  # 新增部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['name'] = '新增的部门01'
        data['parent_id'] = 'dea0dd24e606464e8abdf837b64090ff'
        # data['department_id'] = '100'
        # data['is_sys_sync'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20302, 'code不为20302')
        self.assertEqual(a['msg'], '部门已存在', 'msg不一致')
        self.assertListEqual(sorted(self.xzbm01), sorted(list_), '第一层字段有误')

    def test_department_add_21002(self):
        api = '/api/v1/department/add'  # 新增部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['name'] = '新增的部门01'
        data['parent_id'] = 'dea0dd24e606464e8abdf837b64090ff1'
        # data['department_id'] = '100'
        # data['is_sys_sync'] = '1'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '放回response有误')
        self.assertEqual(a['code'], 21002, 'code不为21002')
        self.assertEqual(a['msg'], 'parent_id参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.xzbm01), sorted(list_), '第一层字段有误')

    def test_department_edit_0(self):
        api = '/api/v1/department/edit'  # 更新部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        name = self.get_nonce_str()
        name = 'edit' + name
        data['name'] = name
        data['target_department_id'] = 'f1c67f5fff1748828177a7c400d825f2'
        # data['is_sys_sync'] = '1'
        # data['action'] = 3   #1缂栬緫锛?2鍒犻櫎锛?3鎭㈠
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.gxbm01), sorted(list_))

    def test_department_edit_21000(self):
        api = '/api/v1/department/edit'  # 更新部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['names'] = 'edit04'
        data['target_department_id'] = 'f1c67f5fff1748828177a7c400d825f21'
        # data['is_sys_sync'] = '1'
        # data['action'] = 3   #1缂栬緫锛?2鍒犻櫎锛?3鎭㈠
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21000, 'code不为21000')
        self.assertEqual(a['msg'], '签名错误', 'msg不一致')
        self.assertListEqual(sorted(self.gxbm01), sorted(list_))

    def test_department_edit_20302(self):
        api = '/api/v1/department/edit'  # 更新部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['name'] = '测试one'
        data['target_department_id'] = '2d5dd1ea5eed4d2a8768a7897e7024b1'
        # data['is_sys_sync'] = '1'
        # data['action'] = 3   #1缂栬緫锛?2鍒犻櫎锛?3鎭㈠
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20302, 'code不为20302')
        self.assertEqual(a['msg'], '部门已存在', 'msg不一致')
        self.assertListEqual(sorted(self.gxbm01), sorted(list_), '第一层字段有误')

    def test_department_edit_20303(self):
        api = '/api/v1/department/edit'  # 更新部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['name'] = 'edit04'
        data['target_department_id'] = 'f1c67f5fff1748828177a7c400d825f21'
        # data['is_sys_sync'] = '1'
        # data['action'] = 3   #1缂栬緫锛?2鍒犻櫎锛?3鎭㈠
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 20303, 'code不为20303')
        self.assertEqual(a['msg'], '部门不存在', 'msg不一致')
        self.assertListEqual(sorted(self.gxbm01), sorted(list_), '第一层字段有误')

    def test_department_edit_21002(self):
        api = '/api/v1/department/edit'  # 更新部门接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        # data['name'] = 'edit04'
        data['target_department_id'] = 'f1c67f5fff1748828177a7c400d825f2'
        # data['is_sys_sync'] = '1'
        # data['action'] = 3   #1缂栬緫锛?2鍒犻櫎锛?3鎭㈠
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.post(url=self.url + api, data=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21002, 'code不为21002')
        self.assertEqual(a['msg'], 'target_department_id或name参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.gxbm01), sorted(list_), '第一层字段有误')

    def test_quota_0(self):
        api = '/api/v1/quota'  # 服务余额获取接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['type'] = '02'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 0, 'code不为0')
        self.assertEqual(a['msg'], '成功', 'msg不一致')
        self.assertListEqual(sorted(self.fwye01), sorted(list_), '第一层字段有误')
        self.assertListEqual(sorted(self.fwye02), sorted(a['data'][0]), '第二层字段有误')

    def test_quota_21002(self):
        api = '/api/v1/quota'  # 服务余额获取接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        # data['nonce_str'] = self.get_nonce_str()
        data['type'] = '02'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '放回response有误')
        self.assertEqual(a['code'], 21002, 'code不为21002')
        self.assertEqual(a['msg'], '参数错误', 'msg不一致')
        self.assertListEqual(sorted(self.fwye01), sorted(list_), '第一层字段有误')

    def test_quota_21039(self):
        api = '/api/v1/quota'  # 服务余额获取接口
        data = {}
        data['company_key'] = self.company_key
        company_secret = self.c_secret
        data['nonce_str'] = self.get_nonce_str()
        data['type'] = '2'
        data['sign'] = self.sign_action(company_secret, data)
        r = requests.get(url=self.url + api, params=data)
        a = r.json()
        list_ = list(a.keys())
        self.assertEqual(r.status_code, 200, '返回response有误')
        self.assertEqual(a['code'], 21039, 'code不为21039')
        self.assertEqual(a['msg'], '获取失败，服务种类未填写', 'msg不一致')
        self.assertListEqual(sorted(self.fwye01), sorted(list_), '第一层字段有误')

    def tearDown(self):
        pass

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest()
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()

import jsonpath
import requests


class TestApi:
    """
    测试类：TestApi，通过类变量保存变量进行实现接口关联
    """
    sso_token = ""
    tenants_id = ""
    organizations_id = ""
    xz_token = ""

    def test_get_token(self):
        """
        通过登录接口获取token
        :return: 需要返回token值给其他接口调用
        """
        url = "https://demo.hailizhiyun.com/api/iam/login"
        datas = {
            "cellphone": "15913139412",
            "password": "",
            "auth_code": "test",
            "Env": "test"
        }
        res = requests.post(url, data=datas)
        # 通过下标提取token值
        # sso_token = res.json()['data']['sso_token']
        result = res.json()
        # 通过jsonpath取token值
        sso_token = jsonpath.jsonpath(result, "$.data.sso_token")
        # 将取到的token值赋值给类变量sso_token
        TestApi.sso_token = sso_token[0]

    def test_get_tenants_id(self):
        """
        获取全部商户的id，从而实现切换不同的商户
        :return: 需要返回具体商户id的token值
        """
        url = "https://demo.hailizhiyun.com/api/iam/user/tenants"
        header = {
            "sso-token": TestApi.sso_token
        }
        res = requests.get(url, headers=header)
        # 获取先知商户的id
        result = res.json()
        tenants_id = jsonpath.jsonpath(result, "$.data.departments[0].id")
        # 获取商户的部门id
        organizations_id = jsonpath.jsonpath(result, "$.data.departments[0].organizations_id")

        TestApi.tenants_id = tenants_id[0]
        TestApi.organizations_id = organizations_id[0]

    def test_get_refresh(self):
        """
        切换先知商户
        :return: 需要返回token值用于进行其他操作
        """
        url = "https://demo.hailizhiyun.com/api/iam/sso_token/refresh"
        datas = {
            "tenant_id": TestApi.tenants_id,
            "organization_id": TestApi.organizations_id
        }
        header = {
            "sso-token": TestApi.sso_token
        }
        res = requests.post(url, data=datas, headers=header)
        result = res.json()
        # 获取先知商户的token
        xz_token = jsonpath.jsonpath(result, "$.data.sso_token")
        TestApi.xz_token = xz_token[0]

    def test_add_inquiry(self):
        """
        货主进行询价
        :return:返回的是询价编号
        """
        url = "https://demo.hailizhiyun.com/api/oms/orderInquiries/add"
        datas = {
            "shipping_terms": 3,   # 运输条款
            "container_type": "2",   # 柜型
            "send_harbor_id": 31,  # 起运港
            "receipt_harbor_id": 34,  # 目的港
            "cargo_id": 4,   # 货物名称
            "cargo_value": "55",   # 单柜货值
            "remark": "test"    # 备注
        }
        header = {
            "sso-token": TestApi.xz_token
        }
        res = requests.post(url, data=datas, headers=header)
        print(res.json())

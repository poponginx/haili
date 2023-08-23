import time

import jsonpath
import pytest

from common.request_tools import RequestTool
from common.yaml_tool import write_yaml


class TestApi:
    """
    测试类：TestApi，通过单独的文件保存中间变量实现接口关联
    """
    file_token = ""
    center_token = ""
    order_no = ""

    # @pytest.mark.smoke
    def test_get_token(self):
        """
        通过登录接口获取到token值
        :return:
        """
        url = "http://demo_center.hailizhiyun.com/api/login"
        datas = {
            "cellphone": "15913139412",
            "password": "admin123"
        }
        res = RequestTool().all_send_request(method="post", url=url, data=datas)
        result = res.json()
        # 通过jsonpath取token值
        file_token = jsonpath.jsonpath(result, "$.data.file_token")
        center_token = jsonpath.jsonpath(result, "$.data.center_token")
        # 将取到的token值赋值给类变量file_token
        TestApi.file_token = file_token[0]
        # 将取到的token值赋值给类变量center_token
        TestApi.center_token = center_token[0]

    # @pytest.mark.smoke
    def test_file_upload(self):
        """
        通过文件上传接口获取到提交客户认证信息参数
        :return:需要返回id
        """
        url = "http://demo_center.hailizhiyun.com/api/fileServer/files/uploadFile"
        # 文件上传接口要将file参数和其他参数分开上传
        files = {
            "file": open("D:\\项目\\证件\\谢茹茹-人像面.jpg", "rb")
        }
        datas = {
            "target": "IdentityCard"
        }
        head = {
            "file-token": TestApi.file_token
        }
        res = RequestTool().all_send_request(method="post", url=url, files=files, data=datas, headers=head)

    # @pytest.mark.smoke
    def test_add_order(self):
        """
        订单成交接口
        :return: 返回的是订单id和订单编号
        """
        url = "http://demo_center.hailizhiyun.com/api/plat_quotes/quotes/deal"
        datas = {
            "container_quantity": 1,
            "weight": "23",
            "cargo_value": "12",
            "shipping_time": "2023-08-19 09:25",
            "discharge_time": "2023-09-01 00:00:00",
            "send_address": "天安门广场-国旗",
            "send_name": "杨桐",
            "send_tel": "18299898236",
            "receipt_address": "秦皇岛市",
            "receipt_name": "宇文化及",
            "receipt_tel": "13790982214",
            "send_remark": "case2",
            "receipt_remark": "test2",
            "order_quotes_id": "532483486984963521",
            "product_id": 219,
            "customer_id": 1854  # 简知科技客户
        }
        headers = {
                "center-token": TestApi.center_token
            }
        res = RequestTool().all_send_request(method="post", url=url, json=datas, headers=headers)
        result = res.json()
        # 通过jsonpath取订单号
        order_no = jsonpath.jsonpath(result, "$.data.order_no")
        # 将订单号赋值给类变量order_no
        TestApi.order_no = order_no[0]
        time.sleep(5)

    def test_del_order(self):
        """
        取消订单
        :return:
        """
        url = "http://demo_center.hailizhiyun.com/api/transOrders/orderCancel"
        datas = {
            "order_no": TestApi.order_no
        }
        headers = {
            "center-token": TestApi.center_token
        }
        res = RequestTool.sess.request(method="post", url=url, json=datas, headers=headers)
        # print(res.json())




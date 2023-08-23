import json
import time
import jsonpath
import pytest
from common.request_tools import RequestTool
from common.yaml_tool import write_yaml, read_yaml, read_testcase


class TestApi:
    """
    测试类：TestApi，通过单独的文件保存中间变量实现接口关联
    """
    @pytest.mark.parametrize("test", read_testcase("./test_data/test_get_request.yaml"))
    def test_get_token(self, test):
        """
        通过登录接口获取到token值
        :return:
        """
        method = test["request"]["method"]
        url = test["request"]["url"]
        datas = test["request"]["data"]
        res = RequestTool().all_send_request(method=method, url=url, data=datas)
        # 通过jsonpath取file_token值,并写入extract.yaml文件中
        tk = res.json()
        value = jsonpath.jsonpath(tk, "$.data.file_token")
        file_token = {"file_token": value[0]}
        write_yaml(file_token)
        # 通过jsonpath取center_token值,并写入extract.yaml文件中
        center_token = jsonpath.jsonpath(tk, "$.data.center_token")
        center_token = {"center_token": center_token[0]}
        write_yaml(center_token)

    # def test_file_upload(self):
    #     """
    #     通过文件上传接口获取到提交客户认证信息参数
    #     :return:需要返回id
    #     """
    #     url = base_url+"/api/fileServer/files/uploadFile"
    #     # 文件上传接口要将file参数和其他参数分开上传
    #     files = {
    #         "file": open("D:\\项目\\证件\\谢茹茹-人像面.jpg", "rb")
    #     }
    #     datas = {
    #         "target": "IdentityCard"
    #     }
    #     head = {
    #         "file-token": read_yaml("file_token")
    #     }
    #     res = RequestTool().all_send_request(method="post", url=url, files=files, data=datas, headers=head)
    #     return res
    #
    # # @pytest.mark.smoke
    # @pytest.mark.parametrize("test", read_testcase("./test_data/test_add_order.yaml"))
    # def test_add_order(self, test):
    #     """
    #     订单成交接口
    #     :return: 返回的是订单id和订单编号
    #     """
    #     method = test["request"]["method"]
    #     url = test["request"]["url"]
    #     datas = test["request"]["data"]
    #     headers = test["request"]["headers"]
    #     for key, value in headers.items():
    #         print(key, value)
    #         headers[key] = read_yaml(key)
    #     print("代码已经将token值赋予")
    #     res = RequestTool().all_send_request(method=method, url=url, json=datas, headers=headers)
    #     print(res.json())
    #     result = res.json()
    #     # 通过jsonpath取订单号
    #     value = jsonpath.jsonpath(result, "$.data.order_no")
    #     order_no = {"order_no": value[0]}
    #     write_yaml(order_no)
    #     time.sleep(3)
    #
    # def test_del_order(self, base_url):
    #     """
    #     取消订单
    #     :return:
    #     """
    #     url = base_url+"/api/transOrders/orderCancel"
    #     datas = {
    #         "order_no": read_yaml("order_no")
    #     }
    #     headers = {
    #         "center-token": read_yaml("center_token")
    #     }
    #     res = RequestTool.sess.request(method="post", url=url, json=datas, headers=headers)
    #     return res
    #
    #
    #

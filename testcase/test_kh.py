import pytest

from common.request_tools import RequestTool
from common.yaml_tool import read_yaml


class TestKh:

    # @pytest.mark.user
    def test_add_kh(self, base_url):
        """
        创建客户接口
        :return:
        """
        url = base_url+"/api/crm/customer"
        datas = {
            "name": "芝麻开门15",
            "source": 2,
            "phone": "18299041295",
            "wx_account_id": "",
            "customer_level": "",
            "remarks": "",
            "clue_type": 2,
            "is_add_wechat": 0,
            "identification_type": 2,
            "gender": 0,
            "delivery_frequency": 0,
            "identity": 0,
            "contact_person": "",
            "contact_phone": "",
            "goods_ids": [],
            "industry_ids": [],
            "province": "",
            "city": "",
            "district": "",
            "street": "",
            "address": ""
        }
        headers = {
            "center-token": read_yaml("center_token")
        }
        res = RequestTool().all_send_request(method="post", url=url, json=datas, headers=headers)
        print(res.json())

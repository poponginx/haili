# _*_ coding:utf-8 _*_
import pytest
from common.yaml_tool import clear_yaml

#
# @pytest.fixture(scope="session", autouse=False)
# def exe_sql():
#     print("查询数据库之前")
#     yield  # 代表唤醒exe_sql后置执行
#     print("请求之后，关闭数据库")


@pytest.fixture(scope="session", autouse=True)
def clears():
    clear_yaml()

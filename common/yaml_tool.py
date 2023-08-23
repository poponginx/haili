# _*_ coding:utf-8 _*_
import os
import yaml


# 写入yaml
def write_yaml(data):
    with open(os.getcwd() + "./extract.yaml", encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取yaml
def read_yaml(key):
    with open(os.getcwd() + "./extract.yaml", encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[key]


# 清空yaml
def clear_yaml():
    with open(os.getcwd() + "./extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


# 读取测试用例
def read_testcase(path):
    with open(path, encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value




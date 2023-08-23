import requests


class RequestTool:
    """
    统一发送请求类：RequestTool
    """
    sess = requests.session()

    def all_send_request(self, **kwargs):
        """
        统一发送请求方法：all_send_request
        :return:
        """
        res = RequestTool.sess.request(**kwargs)
        # print(res.json())
        return res

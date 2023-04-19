# 统一请求封装
import requests


class RequestsUtil:
    """
    使用requests底层代码进行封装
    """

    # 创建请求会话，使其会话保持一致，会自动关联所有请求的cookies信息
    sess = requests.session()

    def send_all_request(self, **kwargs):
        # 发送请求
        res = RequestsUtil.sess.request(**kwargs)
        return res

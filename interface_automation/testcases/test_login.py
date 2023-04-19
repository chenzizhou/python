# coding=utf-8
import pytest

from interface_automation.commons.requests_util import RequestsUtil
from interface_automation.commons.yaml_util import YamlUtil


class TestLogin():
    @pytest.mark.parametrize('login_info', YamlUtil().read_yaml(r'../login.yaml'))
    def test_login(self, login_info):
        # login_info = read_yaml(r'../login.yaml')
        print(login_info)
        # req = session.request(url=login_info['request']['url'], method=login_info['request']['method'],
        #                       headers=login_info['request']['headers'])
        req=RequestsUtil().send_all_request(**login_info['request'])
        assert req.json()['msg'] == login_info['validate']['msg']
        if req.json()['msg'] == login_info['validate']['msg']:
            YamlUtil().write_extract_yaml({'aceess_token': req.json()['token']})
        print(123)

    @pytest.mark.parametrize('add_info', YamlUtil().read_yaml(r'../add.yaml'))
    def test_add(self, add_info):
        print(add_info)
        add_info['request']['url'] = add_info['request']['url'] + '?access_token=' + YamlUtil().read_yaml('../extract.yaml')['aceess_token']
        print(add_info['request']['url'])
        method = add_info['request']['method']
        headers = add_info['request']['headers']
        data = add_info['request']['data']

        req=RequestsUtil().send_all_request(**add_info['request'])
        YamlUtil().write_extract_yaml({'data':req.json()['data']})

    @pytest.mark.parametrize('update_info',YamlUtil().read_yaml(r'../update_info.yaml'))
    def test_updata(self, update_info):
        url = update_info['request']['url'] + '?access_token=' + YamlUtil().read_yaml('../extract.yaml')['aceess_token']
        print(url)
        method = update_info['request']['method']
        headers = update_info['request']['headers']
        data = update_info['request']['data']
        update_info['request']['json'][0]['schemeTypeId'] = YamlUtil().read_yaml('../extract.yaml')['data']
        RequestsUtil().send_all_request(**update_info['request'])

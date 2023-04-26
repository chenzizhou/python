# coding=utf-8
import pytest

from interface_automation.hotloads.debug_talk import DebugTalk
from interface_automation.commons.requests_util import RequestsUtil
from interface_automation.commons.yaml_util import YamlUtil
from interface_automation.commons.logger_handler import logger


class TestLogin():
    @pytest.mark.skipif('1>0')
    def test_login(self, login_info):
        login_info=YamlUtil().read_yaml(r'../login.yaml')
        logger.info(login_info)

        RequestsUtil().standard_yaml(login_info)
        # req = session.request(url=login_info['request']['url'], method=login_info['request']['method'],
        #                       headers=login_info['request']['headers'])
        # req=RequestsUtil().send_request(**login_info['request'])
        # assert req.json()['msg'] == login_info['validate']['msg']
        # if req.json()['msg'] == login_info['validate']['msg']:
        #     YamlUtil().write_extract_yaml({'aceess_token': req.json()['token']})
        # print(123)

    @pytest.mark.skipif('1>0')
    # @pytest.mark.parametrize()
    def test_add(self, add_info):
        # print(jsonpath.jsonpath(add_info['request'],'$..params'))
        # add_info['request']['params']=YamlUtil().read_yaml('../extract.yaml')['aceess_token']
        # print(add_info)
        # add_info['request']['url'] = add_info['request']['url'] + '?access_token=' + YamlUtil().read_yaml('../extract.yaml')['aceess_token']
        # print(add_info['request']['url'])
        # method = add_info['request']['method']
        # headers = add_info['request']['headers']
        # data = add_info['request']['data']
        # req=RequestsUtil().send_request(**add_info['request'])
        # YamlUtil().write_extract_yaml({'data':req.json()['data']})
        add_info = YamlUtil().read_yaml(r'../add.yaml')
        RequestsUtil(obj=DebugTalk()).standard_yaml(add_info)

    # @pytest.mark.skipif('1>0')
    def test_updata(self):
        # update_info['request']['params'] = YamlUtil().read_yaml('../extract.yaml')['aceess_token']
        # update_info['request']['json'][0]['schemeTypeId'] = YamlUtil().read_yaml('../extract.yaml')['data']
        # RequestsUtil().send_request(**update_info['request'])
        login_info = YamlUtil().read_yaml(r'../login.yaml')[0]
        logger.info(login_info)
        RequestsUtil().standard_yaml(login_info)
        add_info=YamlUtil().read_yaml(r'../add.yaml')[0]
        RequestsUtil(obj=DebugTalk()).standard_yaml(add_info)
        update_info=YamlUtil().read_yaml(r'../update_info.yaml')[0]
        RequestsUtil(obj=DebugTalk()).standard_yaml(update_info)
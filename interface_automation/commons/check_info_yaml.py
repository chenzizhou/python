def check_info_yaml(case_info):
    # 获取列表所有的key
    # case_info = case_info[0]
    case_info_keys = case_info.keys()
    # 首先判断caseInfo中是否包含必填的字段
    if 'name' in case_info_keys and 'request' in case_info_keys:
        # 获取request中所有的key
        request_keys = case_info['request'].keys()
        # 判断request中是否包含url、headers、params
        if 'url' in request_keys and 'headers' in request_keys and 'params' in request_keys:
            print("yaml用例标准化格式：校验通过")
        else:
            print("二级关键词必须包含：url,headers,params")
    else:
        print("一级关键词必须包含：name,request,assert")

# 作者
# NATURE
# 日期
# 2023/2/2 14:33
# 功能
#
import json

import requests
import yaml

from interface_automation.commons.yaml_util import YamlUtil
req = requests.session()
url = 'http://10.41.16.20:32091/hbp/userService/login?&type=1&sys=PATROL&sysVersion=&operSys=Windows&client=Chrome%3A%20114.0.0.0&platformType=pc&userAndPwd=LAXnCU%2BPweQ8Z8ryECP0CVw5PwCbnUHwN%2FYhtHctZyMP9Wd%2B2VPO7L4c3v%2Bn62IlKehNPd6kWG2mQmIIwqcUNOtWi71TxyrzQZhWvDlAA1bNXJmF9NiQVqDm9MUqs0zB4tdp8RF%2BduPH3EKSnXcDPtFETySr5Hksmdhkjo5Pius%3D&access_token='
heads = YamlUtil().read_yaml('../heads.yaml')
rep = req.request('get', url=url,headers=heads)
print(rep.json())
token = rep.json()['token']
print(token)
url = 'http://10.41.16.20:32091/patrolServer/bp/configure/api/manager/schemeType/add?access_token=' + token
print(url)
data = {
    "arriveRate": 1,
    "coverRate": 1,
    "areaArriveRate": 1,
    "feedRate": 1,
    "isRegiodGroup": 0,
    "needHandArrive": 0,
    "hasReceive": 1,
    "appTaskStart": 0,
    "taskNeedFeed": 0,
    "isDefaultOrg": 1,
    "executeOrg": "",
    "createTaskDay": 0,
    "taskMoreFeed": 0,
    "isShowNeedSH": 0,
    "isShowDays": 0,
    "appTaskLocation": 1,
    "appOverNeedFeed": 0,
    "appFinishNeedFeed": 0,
    "appGroupLocation": 1,
    "appEquipList": 1,
    "advance": [{
        "taskName": "转单",
        "taskId": "BUTTON_ID_TRANSFORM",
        "needPause": 0,
        "sort": 1
    }, {
        "taskName": "退单",
        "taskId": "BUTTON_ID_BACK",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "延期",
        "taskId": "BUTTON_ID_DELAY",
        "needPause": 0,
        "sort": 3
    }, {
        "taskName": "备注",
        "taskId": "BUTTON_ID_REMARK",
        "needPause": 0,
        "sort": 4
    }],
    "waitdo": [{
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "完工",
        "taskId": "BUTTON_ID_FINISH",
        "needPause": 0,
        "sort": 3
    }, {
        "taskName": "转单",
        "taskId": "BUTTON_ID_TRANSFORM",
        "needPause": 0,
        "sort": 4
    }, {
        "taskName": "退单",
        "taskId": "BUTTON_ID_BACK",
        "needPause": 0,
        "sort": 5
    }, {
        "taskName": "延期",
        "taskId": "BUTTON_ID_DELAY",
        "needPause": 0,
        "sort": 6
    }, {
        "taskName": "备注",
        "taskId": "BUTTON_ID_REMARK",
        "needPause": 0,
        "sort": 7
    }],
    "finish": [{
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "备注",
        "taskId": "BUTTON_ID_REMARK",
        "needPause": 0,
        "sort": 3
    }],
    "over": [{
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "备注",
        "taskId": "BUTTON_ID_REMARK",
        "needPause": 0,
        "sort": 3
    }],
    "group": [{
        "taskName": "反馈",
        "taskId": "BUTTON_ID_FEED_BACK",
        "needPause": 0,
        "sort": 1
    }, {
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 1
    }],
    "map": [{
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 1
    }, {
        "taskName": "工具",
        "taskId": "BUTTON_ID_MAP_TOOL",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "实时",
        "taskId": "BUTTON_ID_REAL_LOCATION",
        "needPause": 0,
        "sort": 3
    }, {
        "taskName": "轨迹",
        "taskId": "BUTTON_ID_TRACE",
        "needPause": 0,
        "sort": 4
    }],
    "equip": [{
        "taskName": "反馈",
        "taskId": "BUTTON_ID_FEED_BACK",
        "needPause": 0,
        "sort": 1
    }, {
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "导航",
        "taskId": "BUTTON_ID_NAVIGATION",
        "needPause": 0,
        "sort": 3
    }, {
        "taskName": "别名",
        "taskId": "BUTTON_ID_ALIAS",
        "needPause": 0,
        "sort": 4
    }, {
        "taskName": "历史记录",
        "taskId": "BUTTON_ID_HISTORY",
        "needPause": 0,
        "sort": 5
    }],
    "mapEquip": [{
        "taskName": "反馈",
        "taskId": "BUTTON_ID_FEED_BACK",
        "needPause": 0,
        "sort": 1
    }, {
        "taskName": "上报",
        "taskId": "BUTTON_ID_EVENT_REPORT",
        "needPause": 0,
        "sort": 3
    }, {
        "taskName": "历史记录",
        "taskId": "BUTTON_ID_HISTORY",
        "needPause": 0,
        "sort": 2
    }, {
        "taskName": "导航",
        "taskId": "BUTTON_ID_NAVIGATION",
        "needPause": 0,
        "sort": 4
    }],
    "appAdvanceBtn": "[{\"taskName\":\"转单\",\"taskId\":\"BUTTON_ID_TRANSFORM\",\"needPause\":0,\"sort\":1},{\"taskName\":\"退单\",\"taskId\":\"BUTTON_ID_BACK\",\"needPause\":0,\"sort\":2},{\"taskName\":\"延期\",\"taskId\":\"BUTTON_ID_DELAY\",\"needPause\":0,\"sort\":3},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":0,\"sort\":4}]",
    "appFinishBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":2},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":0,\"sort\":3}]",
    "appGroupBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":0,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":1}]",
    "appOverBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":2},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":0,\"sort\":3}]",
    "appWaitdoBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":2},{\"taskName\":\"完工\",\"taskId\":\"BUTTON_ID_FINISH\",\"needPause\":0,\"sort\":3},{\"taskName\":\"转单\",\"taskId\":\"BUTTON_ID_TRANSFORM\",\"needPause\":0,\"sort\":4},{\"taskName\":\"退单\",\"taskId\":\"BUTTON_ID_BACK\",\"needPause\":0,\"sort\":5},{\"taskName\":\"延期\",\"taskId\":\"BUTTON_ID_DELAY\",\"needPause\":0,\"sort\":6},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":0,\"sort\":7}]",
    "appMapEquipBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":0,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":3},{\"taskName\":\"历史记录\",\"taskId\":\"BUTTON_ID_HISTORY\",\"needPause\":0,\"sort\":2},{\"taskName\":\"导航\",\"taskId\":\"BUTTON_ID_NAVIGATION\",\"needPause\":0,\"sort\":4}]",
    "appEquipBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":0,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":2},{\"taskName\":\"导航\",\"taskId\":\"BUTTON_ID_NAVIGATION\",\"needPause\":0,\"sort\":3},{\"taskName\":\"别名\",\"taskId\":\"BUTTON_ID_ALIAS\",\"needPause\":0,\"sort\":4},{\"taskName\":\"历史记录\",\"taskId\":\"BUTTON_ID_HISTORY\",\"needPause\":0,\"sort\":5}]",
    "appMapBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":0,\"sort\":1},{\"taskName\":\"工具\",\"taskId\":\"BUTTON_ID_MAP_TOOL\",\"needPause\":0,\"sort\":2},{\"taskName\":\"实时\",\"taskId\":\"BUTTON_ID_REAL_LOCATION\",\"needPause\":0,\"sort\":3},{\"taskName\":\"轨迹\",\"taskId\":\"BUTTON_ID_TRACE\",\"needPause\":0,\"sort\":4}]",
    "type": "XJ",
    "code": "321",
    "name": "321",
    "jobRegiod": "[]",
    "warnConfig": "[]"
}

data = req.request(method='post', url=url, json=data, headers=heads).json()['data']
print(data)
url = 'http://10.41.16.20:32091/patrolServer/configure/api/scheme/equip/batchUpdate?access_token=' + token
data = [{
	"arriveMethod": "gis",
	"buffer": "80",
	"equipCfgId": "193061058461437952",
	"equipFeedbackBpm": "886927892276051968",
	"filterCondition": '',
	"gid": '',
	"historyRecords": "/#/d/list/887379585841233920?NEW_DEVICE_ID=,@deviceCode,&token=@token&account=@account&backApp=true&hideTitle=true",
	"moreFeedback": 0,
	"mustArrive": 0,
	"needArrive": 1,
	"needFeedback": 1,
	"objectName": "防城港标签点",
	"schemeTypeId": data,
	"schemeType": "321"
}]
print(url)
print(req.request(url=url, method='post', json=data, headers=heads).json())

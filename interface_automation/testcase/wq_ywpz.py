# 作者
# NATURE
# 日期
# 2023/2/2 14:33
# 功能
#
import requests
import yaml

rep=requests.session()
url='http://192.168.10.195:7799/patrolServer/bp/configure/api/manager/schemeType/add?' \
    'access_token=fbc1aebc6907d0c15c9cdbc6a9673a735a39caa9717a04f56e213dff7102a492f03e5bfa33ece9c85cd8de7057ec4f1129970b609a6a2d90642a9fb19c79fe4404a9ae29396e9712'
data={
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
    "isShowNeedSH": False,
    "isShowDays": False,
    "appTaskLocation": 1,
    "appOverNeedFeed": 0,
    "appFinishNeedFeed": 0,
    "appGroupLocation": 1,
    "appEquipList": 1,
    "advance": [
        {
            "taskName": "转单",
            "taskId": "BUTTON_ID_TRANSFORM",
            "needPause": False,
            "sort": 1
        },
        {
            "taskName": "退单",
            "taskId": "BUTTON_ID_BACK",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "延期",
            "taskId": "BUTTON_ID_DELAY",
            "needPause": False,
            "sort": 3
        },
        {
            "taskName": "备注",
            "taskId": "BUTTON_ID_REMARK",
            "needPause": False,
            "sort": 4
        }
    ],
    "waitdo": [
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "完工",
            "taskId": "BUTTON_ID_FINISH",
            "needPause": False,
            "sort": 3
        },
        {
            "taskName": "转单",
            "taskId": "BUTTON_ID_TRANSFORM",
            "needPause": False,
            "sort": 4
        },
        {
            "taskName": "退单",
            "taskId": "BUTTON_ID_BACK",
            "needPause": False,
            "sort": 5
        },
        {
            "taskName": "延期",
            "taskId": "BUTTON_ID_DELAY",
            "needPause": False,
            "sort": 6
        },
        {
            "taskName": "备注",
            "taskId": "BUTTON_ID_REMARK",
            "needPause": False,
            "sort": 7
        }
    ],
    "finish": [
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "备注",
            "taskId": "BUTTON_ID_REMARK",
            "needPause": False,
            "sort": 3
        }
    ],
    "over": [
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "备注",
            "taskId": "BUTTON_ID_REMARK",
            "needPause": False,
            "sort": 3
        }
    ],
    "group": [
        {
            "taskName": "反馈",
            "taskId": "BUTTON_ID_FEED_BACK",
            "needPause": False,
            "sort": 1
        },
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 1
        }
    ],
    "map": [
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 1
        },
        {
            "taskName": "工具",
            "taskId": "BUTTON_ID_MAP_TOOL",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "实时",
            "taskId": "BUTTON_ID_REAL_LOCATION",
            "needPause": False,
            "sort": 3
        },
        {
            "taskName": "轨迹",
            "taskId": "BUTTON_ID_TRACE",
            "needPause": False,
            "sort": 4
        }
    ],
    "equip": [
        {
            "taskName": "反馈",
            "taskId": "BUTTON_ID_FEED_BACK",
            "needPause": False,
            "sort": 1
        },
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "导航",
            "taskId": "BUTTON_ID_NAVIGATION",
            "needPause": False,
            "sort": 3
        },
        {
            "taskName": "别名",
            "taskId": "BUTTON_ID_ALIAS",
            "needPause": False,
            "sort": 4
        },
        {
            "taskName": "历史记录",
            "taskId": "BUTTON_ID_HISTORY",
            "needPause": False,
            "sort": 5
        }
    ],
    "mapEquip": [
        {
            "taskName": "反馈",
            "taskId": "BUTTON_ID_FEED_BACK",
            "needPause": False,
            "sort": 1
        },
        {
            "taskName": "上报",
            "taskId": "BUTTON_ID_EVENT_REPORT",
            "needPause": False,
            "sort": 3
        },
        {
            "taskName": "历史记录",
            "taskId": "BUTTON_ID_HISTORY",
            "needPause": False,
            "sort": 2
        },
        {
            "taskName": "导航",
            "taskId": "BUTTON_ID_NAVIGATION",
            "needPause": False,
            "sort": 4
        }
    ],
    "appAdvanceBtn": "[{\"taskName\":\"转单\",\"taskId\":\"BUTTON_ID_TRANSFORM\",\"needPause\":False,\"sort\":1},{\"taskName\":\"退单\",\"taskId\":\"BUTTON_ID_BACK\",\"needPause\":False,\"sort\":2},{\"taskName\":\"延期\",\"taskId\":\"BUTTON_ID_DELAY\",\"needPause\":False,\"sort\":3},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":False,\"sort\":4}]",
    "appFinishBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":2},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":False,\"sort\":3}]",
    "appGroupBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":False,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":1}]",
    "appOverBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":2},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":False,\"sort\":3}]",
    "appWaitdoBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":2},{\"taskName\":\"完工\",\"taskId\":\"BUTTON_ID_FINISH\",\"needPause\":False,\"sort\":3},{\"taskName\":\"转单\",\"taskId\":\"BUTTON_ID_TRANSFORM\",\"needPause\":False,\"sort\":4},{\"taskName\":\"退单\",\"taskId\":\"BUTTON_ID_BACK\",\"needPause\":False,\"sort\":5},{\"taskName\":\"延期\",\"taskId\":\"BUTTON_ID_DELAY\",\"needPause\":False,\"sort\":6},{\"taskName\":\"备注\",\"taskId\":\"BUTTON_ID_REMARK\",\"needPause\":False,\"sort\":7}]",
    "appMapEquipBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":False,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":3},{\"taskName\":\"历史记录\",\"taskId\":\"BUTTON_ID_HISTORY\",\"needPause\":False,\"sort\":2},{\"taskName\":\"导航\",\"taskId\":\"BUTTON_ID_NAVIGATION\",\"needPause\":False,\"sort\":4}]",
    "appEquipBtn": "[{\"taskName\":\"反馈\",\"taskId\":\"BUTTON_ID_FEED_BACK\",\"needPause\":False,\"sort\":1},{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":2},{\"taskName\":\"导航\",\"taskId\":\"BUTTON_ID_NAVIGATION\",\"needPause\":False,\"sort\":3},{\"taskName\":\"别名\",\"taskId\":\"BUTTON_ID_ALIAS\",\"needPause\":False,\"sort\":4},{\"taskName\":\"历史记录\",\"taskId\":\"BUTTON_ID_HISTORY\",\"needPause\":False,\"sort\":5}]",
    "appMapBtn": "[{\"taskName\":\"上报\",\"taskId\":\"BUTTON_ID_EVENT_REPORT\",\"needPause\":False,\"sort\":1},{\"taskName\":\"工具\",\"taskId\":\"BUTTON_ID_MAP_TOOL\",\"needPause\":False,\"sort\":2},{\"taskName\":\"实时\",\"taskId\":\"BUTTON_ID_REAL_LOCATION\",\"needPause\":False,\"sort\":3},{\"taskName\":\"轨迹\",\"taskId\":\"BUTTON_ID_TRACE\",\"needPause\":False,\"sort\":4}]",
    "type": "YH",
    "code": "12345",
    "name": "12345",
    "jobRegiod": "[]",
    "warnConfig": "[]"
}
req=rep.post(url,json=data)
rep.get('http://192.168.10.195:7799/patrolServer/proxy/svr/ServiceEngine/rest/patrolService/refreshConfigCache?access_token=fbc1aebc6907d0c15c9cdbc6a9673a735a39caa9717a04f56e213dff7102a492f03e5bfa33ece9c85cd8de7057ec4f1129970b609a6a2d90642a9fb19c79fe4404a9ae29396e9712')
with open('ywpz.yaml','wt',encoding='utf8') as f:
    yaml.dump(req.json(),f,allow_unicode=True,encoding='utf8')
print(req.json())
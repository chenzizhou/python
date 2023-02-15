# 作者
# NATURE
# 日期
# 2023/2/9 9:59
# 功能
#
import datetime
from time import sleep
import pytest
from app_automation.pageobject.dddk_class import Dd
from chinese_calendar import is_workday


class TestDd:
    def test_dd_dk(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '启动程序')
        desired_caps = Dd.get_dd_control_phone_config()
        # print(desired_caps)
        dk_types = ['上班打卡', '下班打卡', '外勤打卡']
        # print(dk_types)
        peoples = Dd.get_dd_user()
        # print(peoples)
        while True:
            date = datetime.datetime.now()
            h, m = date.time().strftime('%H:%M:%S').split(':')[:2]
            if is_workday(date):
                if h == '08' and m == '40':
                    dd = Dd()
                    for p in peoples:
                        dd.dddk(dk_types[0], p['username'], p['password'])
                    sleep(60 * 60 * 3)
                elif h == '12' and m == '00':
                    dd = Dd()
                    for p in peoples:
                        dd.dddk(dk_types[1], p['username'], p['password'])
                    sleep(60 * 60 * 5.5)
                elif h == '18' and m == '00':
                    dd = Dd()
                    for p in peoples:
                        dd.dddk(dk_types[1], p['username'], p['password'])
                    sleep(60 * 60 * 2)

                # 调试代码段
                # elif h:
                #     dd = Dd()
                #     for p in peoples:
                #         dd.dddk(dk_types[1], p['username'], p['password'])
                #     sleep(60 * 3)

                elif h == '20' and m == '30':
                    dd = Dd()
                    for p in peoples:
                        dd.dddk(dk_types[1], p['username'], p['password'])
                    sleep(60 * 60 * 11)
                else:
                    continue
            else:
                continue

if __name__=='__main__':
    pytest.main()
commons:公共封装文件夹
datas: YAML 数据驱动文件夹
hotloads:热加载文件夹
logs:日志文件夹
reports::定制的allure报告文件夹
temps :临时报告文件夹
testcases :YAML测试用例文件夹
config . yaml:全局配置文件
conftest . py:全局fixture固件
extract.yaml :全局接口关联中间变量提取文件
pytest.ini :全局pytest配置文件
run.py:全局运行文件
readme:接口自动化测试框架说明文件


window获取手机当前界面activity：
adb shell dumpsys window | find "mCurrentFocus"

打开设置界面
adb shell am start -n com.android.settings/.Settings（包名）

滑动
adb shell input swipe <起始X坐标> <起始Y坐标> <结束X坐标> <结束Y坐标> [持续时间]

点击
adb shell input tap x y

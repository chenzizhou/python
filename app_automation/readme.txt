1、原理
通过appium-python-client和appium server进行通信，告诉他我要干什么，通过他来进行翻译成对应设备工具包sdk的识别的指令，然后通过sdk来操控设备终端。
2、jdk环境 android的sdk的环境依赖java环境
3、android sdk  不同系统要下载不同sdk，以便操作不同设备
通过desired_capabilities来设置将要操作的版本
4、appium server 安装  
5、模拟器 夜神、mumu
6、appium-python-client python第三方库
7、desired capabilities
操作系统
版本
设备名称
应用包
入口启动界面
8、常用adb命令
连接
adb connect 127.0.0.1:62001  
其他模拟器：雷神5555 夜神62001 mumu7555 逍遥 
查看
adb devices -l
window获取手机当前界面activity：
pip uiautomation2 ()
impoort uiautomation2 as u2
d = u2.connect(serial) #通过序列号连接设备
d.app_list_running()
d.app_current()

adb shell dumpsys window | find "mCurrentFocus"
adb shell dumpsys window | find "mFocusedActivity"
adb shell dumpsys window top | findstr ACTIVITY
aapt dump badging file.apk    # 是 Android SDK 中 Android Asset Packaging Tool (aapt) 的一个命令，用于提取 Android 应用（APK 文件）的 元数据信息

打开设置界面
adb shell am start -n com.android.settings/.Settings（包名）
滑动
adb shell input swipe <起始X坐标> <起始Y坐标> <结束X坐标> <结束Y坐标> [持续时间]
点击
adb shell input tap x y
恢复出厂设置
adb shell reboot refactory 如果root，恢复后还是root状态






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





定位
无障碍id accessbility_id 
id  resouce-id
在selenium中id具有唯一性（推荐）
appium中的id继承了selenium，不具有唯一性，xpath脆弱、性能低
image
class
custom：使用自己创建的定位策略
ANDROID_UIAUTOMATOR: 'new UiSelector().text('XXX')

定位元素写法
driver.find_element(AppiumBy.ID,'xxxxxxxxxxxxxxxxx')  #appium
driver.find_element(By.ID,'xxxxxxxxxxxxxxxxx')  #selenium

一闪而过的的元素定位,出现时间和消失时间不确定
android.widget.Toast
wait=webDriverWait(driver,5) #显示等待5s

sdk  software development kit 

安装jdk，配置jdk环境配置，adroid环境配置





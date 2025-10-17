开展接口测试：
1、熟悉业务场景，分解每个场景所需要的接口
2、找开发要每个接口的对应接口文档
3、分析每个接口之前的关联性，需保存上一个接口的返回值
4、设计接口测试用例表，利用string.template模块实现动态参数化
5、封装万能接口测试入口
6、利用pytest进行数据驱动，循环获取每个测试接口然后进行串联形成一个业务链

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

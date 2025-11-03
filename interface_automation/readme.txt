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


request参数说明：
heads 请求头：键值对必须是字符串
json  请求体：json。值为字符串、数值、数组、字典。请求头默认添加内容类型为json格式。
data  请求体：默认传递表单。content-type为multi-form，如果要传递json，请求头手动添加content-type:text/json

response 对象包含了许多有用的属性，可以用来获取响应的详细信息：
**response.status_code**：返回 HTTP 状态码，如 200 表示成功。
**response.headers**：返回响应头信息，是一个字典。
**response.content**：返回响应的二进制内容。
**response.text**：返回响应的文本内容。
**response.json()**：如果响应内容是 JSON 格式，可以使用此方法将其解析为 Python 字典或列表。
**response.cookies**：返回响应中的 cookies。
**response.url**：返回请求的 URL，对于重定向请求特别有用。
**response.history**：返回一个包含所有重定向响应的列表。

路径表达式
jsonpath 使用路径表达式来定位 JSON 数据中的元素。以下是一些常用的路径表达式：
$：根对象。
. 或 []：子对象或数组。
*：通配符，匹配所有元素。
..：递归下降，查找所有匹配的元素。
@：在过滤器表达式中引用当前节点。
[index]：数组索引。
[start:end]：数组切片。
[?()]：过滤器表达式。

from jsonpath_ng import jsonpath, parse

jsonpath_expr = parse('$.store.book[*].title')
matches = [match.value for match in jsonpath_expr.find(data)]
print(matches)  # 输出: ['Sayings of the Century', 'The Lord of the Rings']

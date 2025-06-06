1、创建虚拟环境
pip install virtualenv 
virtualenv venv 
venv/Script/activate #激活
venv/Script/deactivate #退出
2、安装依赖环境
pip install -r requirements.txt 
3、路由自上而下匹配
不带/表示唯一，带有/斜杆表示重定向
路由规则
/<float:value>
/<int:value>
/<str:value>
/<path:value>
/<uuid:value>  16个字符组成
def func(value)
4、请求对象 request
request.full_path 获取完整路径，包括后面参数 /xx/xx/xx?xx=xx&xx=xx
request.path 获取路径，没有参数 /xx/xx/xx
request.url 获取请求地址
request.heades 获取请求头
request.args 获取路径中的参数值(返回字典）
request.form 获取post请求（返回字典）

5、响应对象 response
response.setcookies
6、jinja2 模板引擎
render_temple
请求》路由》匹配对应函数》模板引擎从template找到对应html文件》转成字符串》return返回给浏览器
模板传参
根据html形参确定传参
render_temple('xxx.html',参数)


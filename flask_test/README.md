1、创建虚拟环境
pip install virtualenv 
virtualenv venv 
venv/Script/activate #激活
venv/Script/deactivate #退出
2、安装依赖环境
pip install -r requirements.txt 
3、路由自上而下匹配
不带/表示唯一，带有/斜杆表示重定向
uuid
16个字符组成
4、请求对象 request
request.heades
request.args
request.url
5、响应对象 response
response.setcookies
6、jinja2 模板引擎
render_temple
请求》路由》匹配对应函数》模板引擎找到对应html文件》转成字符串》return返回给浏览器


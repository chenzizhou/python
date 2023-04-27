from web_automation.waiqin.util.webkeys import WebKeys

wk = WebKeys(type_='edge')
wk.open('http://www.baidu.com')
d = {'by': 'id', 'value': 'kw','txt':'123'}
wk.send_keys(**d)
wk.pause(3)

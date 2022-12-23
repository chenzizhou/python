import web_automation
import os
urls=('/hello','Index')
app=web_automation.application(urls, globals())
render=web_automation.template.render(os.getcwd() + '/gothonweb/templates')
class Index(object):
    def GET(self):
        return render.hello_form()
    def POST(self):
        form=web_automation.input(name='nobody', greet='hello')
        greeting='%s,%s'%(form.greet,form.name)
        return render.index(greeting=greeting)
if __name__=="__main__":
    app.run()
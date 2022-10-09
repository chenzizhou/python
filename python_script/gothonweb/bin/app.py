import web
import os
urls=('/hello','Index')
app=web.application(urls,globals())
render=web.template.render(os.getcwd()+'/gothonweb/templates')
class Index(object):
    def GET(self):
        return render.hello_form()
    def POST(self):
        form=web.input(name='nobody',greet='hello')
        greeting='%s,%s'%(form.greet,form.name)
        return render.index(greeting=greeting)
if __name__=="__main__":
    app.run()
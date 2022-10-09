from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def add_view(request):
    return HttpResponse('ok')
def addEmployee_view(request):
    if request.method=='GET':
        form=EmployeeForm()
        return render(request,'addEmployee.html',locals())
    else:
        # name=request.POST['name']
        # age=request.POST['age']
        # sal=request.POST['sal']
        # address=request.POST['address']
        # photo=request.POST['photo']
        form=request.POST
        f=EmployeeForm(form)
        if f.is_valid():
            form=f.cleaned_data

        # f=dict(form)
        # f.pop('csrfmiddlewaretoken')
        # print(f)
        # employee.objects.create(name=name,age=age,sal=sal,address=address,photo=photo)
            employee.objects.create(**form)
            return HttpResponse('添加成功！')
def setSession_view(request):
    name='nature'
    request.session['name']=name
    #session失效策略
    # request.session.set_expiry(0)
    #  request.session.set_expiry(value) 
    # 你可以传递四种不同的值给它：
    # * 如果value是个整数，session会在些秒数后失效（适用于整个Django框架，即这个数值时效时整个页面都会session失效）。 
    # * 如果value是个datatime或timedelta，session就会在这个时间后失效。  
    # * 如果value是0,用户关闭浏览器session就会失效。
    # * 如果value是None,session会依赖全局session失效策略。
    return HttpResponse('创建session成功！'+name)
def getSession_view(request):
    name=request.session.get('name')
    return HttpResponse('name:'+name)

from django.shortcuts import render

# Create your views here.
def news_views(request):
    name='nature'
    age=25
    l=['123456789',2]
    return render(request,'myNews.html',locals())
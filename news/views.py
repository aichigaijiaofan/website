from django.shortcuts import render
from news.models import News
# Create your views here.
def new_list(request):
    news_list = News.objects.all()
    return render(request, 'list.html',{'news_list': news_list})


def detail(request, id):
    news = News.objects.get(pk=id)
    return render(request, 'detail.html', {'news': news})
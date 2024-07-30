from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
from team.models import Team
from news.models import News
# Create your views here.
def index(request):
    # 获取slide表数据
    slides = Slide.objects.all()
    # 获取团队成员
    team = Team.objects.all().order_by('-rank')
    # 获取资讯中心新闻数据
    news = News.objects.filter(category_id=1).order_by('-created_at')[:3]
    return render(request, 'index.html',{
        'slides': slides,
        'team': team,
        'news': news,
    })
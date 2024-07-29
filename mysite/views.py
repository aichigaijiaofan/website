from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
from team.models import Team
# Create your views here.
def index(request):
    # 获取slide表数据
    slides = Slide.objects.all()
    # 获取团队成员
    team = Team.objects.all().order_by('-rank')
    return render(request, 'index.html',{
        'slides': slides,
        'team': team,
    })
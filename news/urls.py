from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.new_list),
    path('<int:id>/', views.detail)
]
from django.urls import path
from django.urls.conf import include
from .import views


app_name = 'YouTube_DownApp'


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('down/', views.down_video, name='down_video'),
    
]



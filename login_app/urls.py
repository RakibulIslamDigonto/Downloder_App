from django.urls import include, path
from login_app import views

app_name= 'login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.reg_user, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('update_user/', views.update_user_view, name='update_user'),
    path('signout/', views.reg_user, name='signout'),
]


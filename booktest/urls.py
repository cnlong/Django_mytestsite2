
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('index/', views.index),
    path('showarg<int:bid>/', views.show_arg),
    path('login/', views.login),  # 登录界面
    path('login_ajax', views.login_ajax),  # ajax登录界面
    path('login_check', views.login_check),  # 校验页面
    path('login_ajax_check', views.login_ajax_check),  # ajax校验页面
    path('test_ajax', views.ajax_test),
    path('ajax_handle', views.ajax_handle),
    path('set_cookie', views.set_cookie),  # 设置cookie
    path('get_cookie', views.get_cookie),  # 获取cookie
    path('set_session', views.set_session),  # 设置session
    path('get_session', views.get_session),  # 获取session
    path('clear_session', views.clear_session),  # 清除session
]

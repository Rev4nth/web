from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        path('', views.global_feed, name='global_feed'),
        path('signup/', views.sign_up, name='signup'),
        path('login/', auth_views.login, name='login'),
        path('logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
        path('article/new/', views.article_new, name='article_new'),
        path('user_feed/', views.user_feed, name='user_feed'),
        path('article/<int:article_id>/', views.article_detail, name='article_detail'),
        path('article/like/<int:article_id>/', views.make_favourite, name='make_favourite')
    ]

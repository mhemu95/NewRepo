from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='post_home'),
    path('post/<id>/', views.post_detail, name='post_detail'),
    #crud urls..
    path('panel/', views.post_list, name='post_list'),
    path('panel/create/', views.create_post, name='create_post'),
    path('panel/update/<id>/', views.update_post, name='update_post'),
    path('panel/delete/<id>/', views.delete_post, name='delete_post'),
    #search url...
    path('search/', views.search, name='post_search'),
]

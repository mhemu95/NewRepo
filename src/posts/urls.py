from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('<id>/', views.post_detail, name='post_detail'),
    path('update/<id>/', views.update_post, name='update_post'),
]

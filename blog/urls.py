from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:post_id>/', views.post, name="post"),
    path('example/', views.example, name='example'),
]
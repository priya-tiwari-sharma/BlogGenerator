from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPage, name='blog_page'),
    path('generate_title/', views.GenerateTitles, name='generate_titles'),
    path('generate_content/', views.GenerateContent, name='generate_content'),
    path('generate_image/', views.GenerateImage, name='generate_image'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update_meme, name='update_meme'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),
]
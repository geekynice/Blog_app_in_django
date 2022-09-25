
from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.index),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]

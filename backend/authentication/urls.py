from django.urls import path 

from . import views 

urlpatterns = [
    path('register/', views.Users.as_view(), name='register')
]
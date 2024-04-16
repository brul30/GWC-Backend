from django.urls import path
from . import views

urlpatterns = [
 #   path('',views.get_Data),
    path('api/signup', views.signup),
]
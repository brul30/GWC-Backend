from django.urls import path
from . import views

urlpatterns = [
 #   path('',views.get_Data),
    path('addNotes', views.addNotes),
    path('getNotes', views.getNotes),
    path('getUniqueCourses',views.getUniqueCourses)
]
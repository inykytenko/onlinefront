from django.contrib import admin
from django.urls import path
from students.views import MyView, GetStudents


urlpatterns = [
    path('view1/', MyView.as_view()),
    path('view2/<pk>/', MyView.as_view()),
    path('view2/<pk>/', MyView.as_view()),
    path('view3/<pk>/', GetStudents.as_view()),
]
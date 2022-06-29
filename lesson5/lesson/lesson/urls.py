from django.contrib import admin
from django.urls import path, include
from students.views import my_view, GetStudents

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view/', my_view),
   # path('view/',GetStudents),
    path('students/',include('students.urls')),
    #path('students/',include('subject.urls')),
    
]

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student, Subject

def my_view(request):
    if request.method == 'get':
       return HttpResponse('result')


class MyView(View):
    def get(self, request, pk):
        
        try:
            student = Student.odjects.get(pk=pk)
            students_data = {
                "name":student.name   
        }
        except Student.DoesNotExist:
            students_data = {}   
        
        
        return JsonResponse({"data":students_data})

class GetStudents(View):

    def get(self, request, pk):
        students = []
        try:
            subj = Subject.objects.get(pk=pk)
            groups = subj.groups.all()
            for g in groups:
                st = g.students.all()
                for s in st:
                    students.append({"name": s.name})
        except Subject.DoesNotExist:
            students.append({"Error!": "Subject with such ID does not exists!"})
        return JsonResponse({"data": students})    
    
    
    def post(self, request):
        
        name = request.POST.get('name', '')
        
        print(name)
        return HttpResponse('result11')
        
import io

from django.shortcuts import render
from django.views import View
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# class based view
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class student(View):  # to retrieve the data into the database and changed complex data into python object code
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        stu = JSONParser().parse(stream)
        id = stu.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):  # to changed json data into complex data and save into the database
        json_data = request.body
        stream = io.BytesIO(json_data)
        stu = JSONParser().parse(stream)
        serializer = StudentSerializer(data=stu)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):  # first check the data if data is valid it update
        # the data and save into the database
        json_data = request.body
        stream = io.BytesIO(json_data)
        stu = JSONParser().parse(stream)
        id = stu.get('id')
        stud = Student.objects.get(id=id)
        serializer = StudentSerializer(stud, data=stu, partial=True)  # to update the partial data
        # serializer = StudentSerializer(stud, data=stu) #to update the whole data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "data updated"}
            return JsonResponse(res)

    def delete(self, request, *args, **kwargs):  # delete the data into the system or database
        json_data = request.body
        stream = io.BytesIO(json_data)
        stu = JSONParser().parse(stream)
        id = stu.get('id')
        stud = Student.objects.get(id=id)
        stud.delete()
        res = {'msg': "data deleted"}
        return JsonResponse(res)

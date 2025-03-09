from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins,generics,views,viewsets

# Create your views here.
@api_view(['GET','POST'])
def studentsView(request):
    # studentsResponse={
    #     'id':1,
    #     'name':'Vyshnavi Ravula'
    # }
    # manually serialize
    # student=Student.objects.all()
    # stu_list=list(student.values())
    # return(JsonResponse(stu_list,safe=False))
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return(Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST))

@api_view(['GET','PUT','DELETE'])
def StudentDetailedView(request,pk):
    try:
        stu=Student.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=StudentSerializer(stu)
        return(Response(serializer.data,status=status.HTTP_200_OK))
    elif request.method=='PUT':
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(Response(serializer.data,status=status.HTTP_200_OK))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        stu.delete()
        return(Response(status=status.HTTP_204_NO_CONTENT))

# class Employees(APIView):
#     def get(self,request):
#         emp=Employee.objects.all()
#         empserializer=EmployeeSerializer(emp,many=True)
#         return Response(empserializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         emps=EmployeeSerializer(data=request.data)
#         if emps.is_valid():
#             emps.save()
#             return Response(emps.data,status=status.HTTP_200_OK)
#         return Response(emps.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetail(APIView):
#     def get_object(self,request,pk):
#         try:
#             emp=Employee.objects.get(pk=pk)
#         except:
#             raise Http404
#         return(emp)
#     def get(self,request,pk):
#         emp=self.get_object(request,pk)
#         emps=EmployeeSerializer(emp)
#         return Response(emps.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         emp=self.get_object(request,pk)
#         emps=EmployeeSerializer(emp,data=request.data)
#         if emps.is_valid():
#             emps.save()
#             return Response(emps.data,status=status.HTTP_200_OK)
#         return Response(emps.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         emp=self.get_object(request,pk)
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
#Mixins
class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return(self.destroy(request,pk))
"""
class Employees(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'

# using viewsets
# class EmployeeViewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset=Employee.objects.all()
#         serializer=EmployeeSerializer(queryset,many=True)
#         return(Response(serializer.data))
#     def create(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,request,pk=None):
#         queryset=get_object_or_404(Employee,pk=pk)
#         serializer=EmployeeSerializer(queryset)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def update(self,request,pk):
#         emp=get_object_or_404(Employee,pk=pk)
#         serializer=EmployeeSerializer(emp,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         emp=get_object_or_404(Employee,pk=pk)
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
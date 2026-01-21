"""
Views cho ứng dụng person
Xử lý các yêu cầu HTTP cho quản lý người
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Person, Department
from .serializers import PersonSerializer


class PersonListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới người
    GET: Lấy danh sách tất cả người
    POST: Tạo mới một người
Endpoint: POST /
    Mô tả: Tạo mới một người trong hệ thống
    Input: Dữ liệu danh mục cần tạo (name, email, department)
           Body (raw JSON): {"name": "Hồ Thanh Toan", "email": "hothanhtoan@email.com", "department": id}
    Output: Danh sách danh mục dưới dạng JSON
                [
                {
                "id":1,
                "name":"Hồ Thanh Toan",
                "email":"hothanhtoan@email.com",
                "department":5},
                {"id":12,
                "name":"Hồ Thanh Toan",
                "email":"hothanhtoan1@email.com",
                "department":3},
                {"id":13,
                "name":"Hồ Thanh",
                "email":"hothanh@email.com",
                "department":1
                }
                ]
                


    """
    #Lấy danh sách tất cả người, nếu không có thì tạo mới
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    #permission_classes = [IsAuthenticated]




class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa người
    GET: Lấy thông tin chi tiết một người
    PUT/PATCH: Cập nhật thông tin người
    DELETE: Xóa người
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

@api_view(['GET'])
def person_detail_by_name(request, name):
    """
    API endpoint để lấy thông tin người theo tên
    GET: /person/name/{name}/
    """
    person = get_object_or_404(Person, name__iexact=name)

    #Serialize dữ liệu của danh mục đó
    serializer = PersonSerializer(person)
   #Trả về respone với dữ liệu serialized
    return Response(serializer.data)

@api_view(['GET'])
def person_detail_by_department(request, pk):
    """
    API endpoint để lấy thông tin người theo tên phòng ban
    GET: /person/department/{id}/
    """
    department = get_object_or_404(Department, pk=pk)

    persons = Person.objects.filter(department_id=pk).select_related('department')
    #department = get_object_or_404(Person, department=pk)

    #Serialize dữ liệu của danh mục đó
    serializer = PersonSerializer(persons, many = True)
    #Trả về respone với dữ liệu serialized
    return Response(serializer.data)
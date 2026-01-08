"""
Views cho ứng dụng person
Xử lý các yêu cầu HTTP cho quản lý người
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Person
from .serializers import PersonSerializer


class PersonListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới người
    GET: Lấy danh sách tất cả người
    POST: Tạo mới một người
    """


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa người
    GET: Lấy thông tin chi tiết một người
    PUT/PATCH: Cập nhật thông tin người
    DELETE: Xóa người
    """


@api_view(['GET'])
def person_detail_by_name(request, name):
    """
    API endpoint để lấy thông tin người theo tên
    GET: /person/name/{name}/
    """
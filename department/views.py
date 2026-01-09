"""
Views cho ứng dụng department
Xử lý các yêu cầu HTTP cho quản lý phòng ban
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Department
from .serializers import DepartmentSerializer


class DepartmentListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới phòng ban
    GET: Lấy danh sách tất cả phòng ban
    POST: Tạo mới một phòng ban
    """
    pass


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa phòng ban
    GET: Lấy thông tin chi tiết một phòng ban
    PUT/PATCH: Cập nhật thông tin phòng ban
    DELETE: Xóa phòng ban
    """
    pass


@api_view(['GET'])
def department_detail_by_name(request, name):
    """
    API endpoint để lấy thông tin phòng ban theo tên
    GET: /department/name/{name}/
    """
    pass
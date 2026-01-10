"""
Views cho ứng dụng location
Xử lý các yêu cầu HTTP cho quản lý vị trí lắp đặt
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Location
from .serializers import LocationSerializer


class LocationListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới vị trí lắp đặt
    GET: Lấy danh sách tất cả vị trí lắp đặt
    POST: Tạo mới một vị trí lắp đặt
    """
    pass


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa vị trí lắp đặt
    GET: Lấy thông tin chi tiết một vị trí lắp đặt
    PUT/PATCH: Cập nhật thông tin vị trí lắp đặt
    DELETE: Xóa vị trí lắp đặt
    """
    pass


@api_view(['GET'])
def location_detail_by_name(request, name):
    """
    API endpoint để lấy thông tin vị trí lắp đặt theo tên
    GET: /location/name/{name}/
    """
    pass

###test123

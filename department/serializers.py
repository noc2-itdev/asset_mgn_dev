"""
Serializers cho ứng dụng department
Xử lý chuyển đổi dữ liệu giữa model và JSON
"""
from rest_framework import serializers
from main.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Department
    Chuyển đổi dữ liệu giữa model và JSON format
    """
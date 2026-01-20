"""
Serializers cho ứng dụng location
Xử lý chuyển đổi dữ liệu giữa model và JSON
"""
from rest_framework import serializers
from main.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Location
    Chuyển đổi dữ liệu giữa model và JSON format
    """


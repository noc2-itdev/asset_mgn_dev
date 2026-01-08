"""
Serializers cho ứng dụng person
Xử lý chuyển đổi dữ liệu giữa model và JSON
"""
from rest_framework import serializers
from main.models import Person


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Person
    Chuyển đổi dữ liệu giữa model và JSON format
    """
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
    class Meta:
        model = Location
        fields = '__all__'
    def validate_name(self, value):
        """
        Kiểm tra địa điểm lắp đặt tài sản có tồn tại chưa

        Trường hợp CREATE:

        
        :param self: Description
        :param value: Description
        """
        # Lấy instance hiện tại
        instance = self.instance
        # Kiểm tra có địa điểm lắp đặt có tồn tại chưa
        # Nếu đang cập nhật, bỏ qua chính instance hiện tại
        queryset = Location.objects.filter(name__iexact=value)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(f"Địa điểm với tên '{value}' đã tồn tại.")
        
        return value
     
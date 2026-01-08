"""
Serializers cho ứng dụng main
Xử lý chuyển đổi dữ liệu giữa model và JSON
"""
from rest_framework import serializers
from .models import Department, Person, Location, AssetCategory, Asset, AssetAttachment, AssetHistory, TicketRequest, AuditSession, AuditItem, AuditAction


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Department
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = Department
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Person
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = Person
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Location
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    # Thêm trường assets_count để hiển thị số lượng tài sản tại vị trí
    assets_count = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('id',)

    def get_assets_count(self, obj):
        """
        Lấy số lượng tài sản tại vị trí này
        """
        # Nếu có liên kết với model Asset, sẽ trả về số lượng
        if hasattr(obj, 'asset_set'):
            return obj.asset_set.count()
        return 0

    def validate_name(self, value):
        """
        Xác thực tên vị trí
        """
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Tên vị trí phải có ít nhất 2 ký tự.")
        return value


class AssetCategorySerializer(serializers.ModelSerializer):
    """
    Serializer cho model AssetCategory
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AssetCategory
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Asset
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = Asset
        fields = '__all__'


class AssetAttachmentSerializer(serializers.ModelSerializer):
    """
    Serializer cho model AssetAttachment
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AssetAttachment
        fields = '__all__'


class AssetHistorySerializer(serializers.ModelSerializer):
    """
    Serializer cho model AssetHistory
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AssetHistory
        fields = '__all__'


class TicketRequestSerializer(serializers.ModelSerializer):
    """
    Serializer cho model TicketRequest
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = TicketRequest
        fields = '__all__'


class AuditSessionSerializer(serializers.ModelSerializer):
    """
    Serializer cho model AuditSession
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AuditSession
        fields = '__all__'


class AuditItemSerializer(serializers.ModelSerializer):
    """
    Serializer cho model AuditItem
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AuditItem
        fields = '__all__'


class AuditActionSerializer(serializers.ModelSerializer):
    """
    Serializer cho model AuditAction
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = AuditAction
        fields = '__all__'
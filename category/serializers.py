"""
Serializers cho ứng dụng category
Xử lý chuyển đổi dữ liệu giữa model và JSON
Dưới đây là khung cho các action cần triển khai:
- Tạo mới danh mục tài sản
- Cập nhật danh mục tài sản
- Xóa danh mục tài sản
- Lấy danh sách danh mục tài sản
- Lấy chi tiết danh mục tài sản theo ID
- Lấy danh mục tài sản theo tên
"""
from rest_framework import serializers
from main.models import AssetCategory


class AssetCategorySerializer(serializers.ModelSerializer):
    """
    Serializer cho model AssetCategory
    Chưa triển khai đầy đủ - dành cho developer tiếp tục phát triển
    """
    class Meta:
        model = AssetCategory
        fields = '__all__'
        # TODO: Triển khai các phương thức xác thực dữ liệu
        # TODO: Thêm phương thức validate_name để xác thực tên danh mục
        # TODO: Thêm phương thức để xử lý tài sản liên quan trong danh mục
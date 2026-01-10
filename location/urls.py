"""
URL patterns cho ứng dụng location
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
"""

from django.urls import path
from . import views

# Tên namespace cho ứng dụng location
app_name = "location"

urlpatterns = [
    # liệt kê tất cả location trong database
    path("", views.location_list, name="location-list"),
    path("create/", views.location_create, name="location-create"),
    # Đường dẫn cho danh sách vị trí lắp đặt và tạo mới
    # Đường dẫn cho chi tiết, cập nhật, xóa vị trí lắp đặt theo ID
    # Đường dẫn cho chi tiết vị trí lắp đặt theo tên
]

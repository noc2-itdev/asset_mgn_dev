"""
URL patterns cho ứng dụng person
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
"""
from django.urls import path
from . import views

# Tên không gian tên (namespace) cho ứng dụng person
app_name = 'person'

urlpatterns = [
    # Đường dẫn cho danh sách người và tạo mới
    
    # Đường dẫn cho chi tiết, cập nhật, xóa người theo ID
    
    # Đường dẫn cho chi tiết người theo tên
]
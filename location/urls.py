"""
URL patterns cho ứng dụng location
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
"""
from django.urls import path
from . import views

# Tên namespace cho ứng dụng location
app_name = 'location'

urlpatterns = [
    # Đường dẫn cho danh sách vị trí lắp đặt và tạo mới
    #path('',views.location_detail_by_name, name='location-list'),
    path('create/', views.location_create, name='location-create'),
    
    # Đường dẫn cho chi tiết, cập nhật, xóa vị trí lắp đặt theo ID
    path('<int:pk>/', views.location_detail, name='location-detail'),
    
    # Đường dẫn cho chi tiết vị trí lắp đặt theo tên
    #path('name/<str:name>/',views.location_detail_by_name, name='location_detail_by_name')
]

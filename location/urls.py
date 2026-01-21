"""
URL patterns cho ứng dụng location
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
"""
from django.urls import path
from . import views

# Tên namespace cho ứng dụng location
app_name = 'location'

urlpatterns = [
    # Danh sách và tạo mới: GET /location/ và POST /location/
    path('', views.LocationListView.as_view(), name='location_list'),
    
    # Chi tiết, sửa, xóa theo ID: /location/1/
    path('<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    
    # Chi tiết theo tên: /location/name/Kho-A/
    path('name/<str:name>/', views.location_detail_by_name, name='location_detail_by_name'),
]

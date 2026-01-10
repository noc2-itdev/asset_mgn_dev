"""
URL patterns cho ứng dụng department
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
"""
from django.urls import path
from . import views

# Tên namespace cho ứng dụng department
app_name = 'department'

urlpatterns = [
    # Đường dẫn cho danh sách phòng ban và tạo mới
    path('', views.department_list, name='department-list'),
    path('create/', views.department_create, name='department-create'),

    # Đường dẫn cho chi tiết, cập nhật, xóa phòng ban theo ID
    path('<int:pk>/', views.department_detail, name='department-detail'),
    path('<int:pk>/update/', views.department_update, name='department-update'),
    path('<int:pk>/partial-update/', views.department_partial_update, name='department-partial-update'),
    path('<int:pk>/delete/', views.department_delete, name='department-delete'),

    # Đường dẫn cho chi tiết phòng ban theo tên
    path('name/<str:name>/', views.department_detail_by_name, name='department-detail-by-name'),
]
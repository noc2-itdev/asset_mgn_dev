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
    path('', views.PersonListView.as_view(), name='person-list'),
    # Đường dẫn cho chi tiết, cập nhật, xóa người theo ID
    path('<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),

    # Đường dẫn cho chi tiết người theo tên
    path('name/<str:name>/', views.person_detail_by_name, name='person-by-name'),
    # Đường dẫn cho chi tiết người theo phòng ban
    path('department/<int:pk>/', views.person_detail_by_department, name='person-by-department'),
]
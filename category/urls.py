"""
URL patterns cho ứng dụng category
Định nghĩa các đường dẫn URL cho các view trong ứng dụng
Dưới đây là khung cho các action cần triển khai:
- Tạo mới danh mục tài sản
- Cập nhật danh mục tài sản
- Xóa danh mục tài sản
- Lấy danh sách danh mục tài sản
- Lấy chi tiết danh mục tài sản theo ID
- Lấy danh mục tài sản theo tên
"""
from django.urls import path
from . import views

# Tên không gian tên (namespace) cho ứng dụng category
app_name = 'category'

urlpatterns = [
    # Đường dẫn cho danh sách danh mục và tạo mới
    # Action cần triển khai:
    # - GET: Lấy danh sách tất cả danh mục tài sản
    # - POST: Tạo mới một danh mục tài sản
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    
    # Đường dẫn cho chi tiết, cập nhật, xóa danh mục theo ID
    # Action cần triển khai:
    # - GET: Lấy thông tin chi tiết một danh mục tài sản
    # - PUT/PATCH: Cập nhật thông tin danh mục tài sản
    # - DELETE: Xóa danh mục tài sản
    # path('<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
    # TODO: Thêm đường dẫn cho chi tiết danh mục theo tên
    # Ví dụ: path('name/<str:name>/', views.category_detail_by_name, name='category-by-name'),
    
    # TODO: Thêm các endpoint khác như:
    # - Endpoint để lấy danh sách tài sản theo danh mục
    # - Endpoint để kiểm tra sự tồn tại của danh mục
    # - Endpoint để tìm kiếm danh mục

]
"""
Views cho ứng dụng category
Xử lý các yêu cầu HTTP cho quản lý danh mục tài sản
Dưới đây là khung cho các action cần triển khai:
- Tạo mới danh mục tài sản
- Cập nhật danh mục tài sản
- Xóa danh mục tài sản
- Lấy danh sách danh mục tài sản
- Lấy chi tiết danh mục tài sản theo ID
- Lấy danh mục tài sản theo tên
"""
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import AssetCategory
from .serializers import AssetCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



class CategoryListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới danh mục tài sản
    Chưa triển khai đầy đủ - dành cho developer tiếp tục phát triển
    Action cần triển khai:
    - GET: Lấy danh sách tất cả danh mục tài sản
    - POST: Tạo mới một danh mục tài sản 
    Tạo mới một danh mục

    Endpoint: POST /categories/
    Mô tả: Tạo mới một danh mục trong hệ thống
    Input: Dữ liệu danh mục cần tạo (name, is_component)
           Body (raw JSON): {"name": "Linh kiện máy tính", "is_component": True}


    """
    # lấy toàn bộ danh sách danh mục tài sản GET, nếu chưa có thì tạo mới POST
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
    permission_classes = [IsAuthenticated]

    


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa danh mục tài sản
    Chưa triển khai đầy đủ - dành cho developer tiếp tục phát triển
    Action cần triển khai:
    - GET: Lấy thông tin chi tiết một danh mục tài sản
    - PUT/PATCH: Cập nhật thông tin danh mục tài sản
    - DELETE: Xóa danh mục tài sản
    """
    pass
""" @api_view(['GET'])
def assetcategory_list(request):

    # lấy tất cả đối tượng AssetCategory
    assetcategorys = AssetCategory.objects.all()
    # chuyển dữ liệu sang JSON
    serializer = AssetCategorySerializer(assetcategorys, many=True)
    # Trả về respone với dữ liệu serializer
    return Response(serializer.data) """

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
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from main.models import AssetCategory
from .serializers import AssetCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



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
           Body (raw JSON): {"name": "Linh kiện máy tính", "is_component": true}
    Output: Danh sách danh mục dưới dạng JSON
                [
                    {
                        "id": 1,
                        "name": "Linh Kien",
                        "is_component": true
                    },
                    {
                        "id": 3,
                        "name": "Tài sản chính",
                        "is_component": false
                    }
                ]

    """
    # lấy toàn bộ danh sách danh mục tài sản GET, nếu chưa có thì tạo mới POST
    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer
    #permission_classes = [IsAuthenticated]

    

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa danh mục tài sản
    Chưa triển khai đầy đủ - dành cho developer tiếp tục phát triển
    Action cần triển khai:
    - GET: Lấy thông tin chi tiết một danh mục tài sản

    - PUT/PATCH: Cập nhật thông tin danh mục tài sản
    - DELETE: Xóa danh mục tài sản
    """


    queryset = AssetCategory.objects.all()
    serializer_class = AssetCategorySerializer

"""
    Xóa một phòng ban

    Endpoint: DELETE /category/{id}/delete/
    Mô tả: Xóa một danh mục tài sản khỏi hệ thống
    Input: ID của danh mục tài sản cần xóa (pk) - thay thế {id} bằng ID thực tế
    Output: Response với status code 204

    Ví dụ: curl -X DELETE http://localhost:8000/category/1/delete/
    """

@api_view(['DELETE'])
def category_delete(request, pk):
    # Lấy đối tượng danh mục tài sản theo ID, nếu không có thì trả về 404
    assetcategory = get_object_or_404(AssetCategory, pk=pk)
    #Xóa đối tưởng khỏi Database
    assetcategory.delete()
    # Trả về response rỗng với status code 204 (NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)

"""
API endpoint để lấy thông tin danh mục tài sản bằng tên
Endpoint: GET /category/name/{name}/
Input: Tên danh mục tài sản cần tìm kiếm (name) - thay thế {name} bằng tên thực tế
Output: Thông tin danh mục dưới dạng JSON
            {
            "id": 6,
            "name": "Tai san chinh",
            "is_component": false
            }

"""

@api_view(['GET'])
def category_detail_by_name(request, name):
    #Lấy đối tượng theo têm, nếu không tồn tại thì trả vê 404
   """  try:
        assetcategory = AssetCategory.objects.get(name=name)
    except AssetCategory.DoesNotExist:
        from django.http.import """
   assetcategory = get_object_or_404(AssetCategory, name=name)

    #Serialize dữ liệu của danh mục đó
   serializer = AssetCategorySerializer(assetcategory)
   #Trả về respone với dữ liệu serialized
   return Response(serializer.data)





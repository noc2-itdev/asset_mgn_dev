from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import DepartmentSerializer


# @Todo: Class-based View (CBV) hoạt động không theo tuần tự, sử dụng cơ chế kế thừa (ListCreateAPIView) và khai báo thuộc tính (permission_classes, queryset, serializer_class) để DRF tự động xử lý
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

# @Todo: Function-based View (FBV) được gọi là lập trình hướng thủ tục (viết từng bước logic xử lý theo tuần tự), cần định nghĩa rõ ràng logic xử lý cho từng phương thức HTTP (GET, POST)
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def department_list_create_fbv(request):
#     """
#     Xử lý hành động LIST (GET) và CREATE (POST) cho đối tượng Department.
#     Chỉ cho phép người dùng đã xác thực truy cập.
#     """
#
#     # --- LIST LOGIC (GET request) ---
#     if request.method == 'GET':
#         # 1. Truy cập Queryset: Lấy tất cả các đối tượng (matching queryset = Department.objects.all())
#         departments = Department.objects.all()
#
#         # 2. Serialize dữ liệu: Chuyển đổi từ Python sang định dạng Response (matching serializer_class)
#         serializer = DepartmentSerializer(departments, many=True)
#
#         # 3. Trả về Response
#         return Response(serializer.data)
#
#     # --- CREATE LOGIC (POST request) ---
#     elif request.method == 'POST':
#         # 1. Deserialize/Validate dữ liệu: Khởi tạo Serializer với dữ liệu gửi đến
#         serializer = DepartmentSerializer(data=request.data)
#
#         # 2. Xác thực dữ liệu
#         if serializer.is_valid():
#             # 3. Lưu đối tượng mới (Tương đương với logic .save() trong ListCreateAPIView)
#             serializer.save()
#
#             # 4. Trả về phản hồi thành công (HTTP 201 Created)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         # 5. Trả về lỗi nếu dữ liệu không hợp lệ
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

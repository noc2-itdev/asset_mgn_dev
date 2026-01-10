"""
Views cho ứng dụng department
Xử lý các yêu cầu HTTP cho quản lý phòng ban
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Department
from .serializers import DepartmentSerializer


@api_view(['GET'])
def department_list(request):
    """
    Lấy danh sách tất cả phòng ban

    Endpoint: GET /department/
    Mô tả: Trả về toàn bộ danh sách phòng ban trong hệ thống
    Input: Không yêu cầu tham số
    Output: Danh sách phòng ban dưới dạng JSON
    [
        {
            "id": 1,
            "name": "TNOC2",
            "description": "Phòng truyền dẫn"
        }
    ]

    Ví dụ: curl -X GET http://localhost:8000/department/
    """
    # Lấy tất cả các đối tượng Department từ database
    departments = Department.objects.all()

    # Serialize dữ liệu để chuyển sang định dạng JSON
    serializer = DepartmentSerializer(departments, many=True)

    # Trả về response với dữ liệu serialized
    return Response(serializer.data)


@api_view(['POST'])
def department_create(request):
    """
    Tạo mới một phòng ban

    Endpoint: POST /department/create/
    Mô tả: Tạo mới một phòng ban trong hệ thống
    Input: Dữ liệu phòng ban cần tạo (name, description)
           Body (raw JSON): {"name": "TNOC2", "description": "Phòng truyền dẫn"}
    Output: Thông tin phòng ban vừa tạo dưới dạng JSON
    {
        "id": 3,
        "name": "SNOC2",
        "description": "Phòng chuyển mạch"
    }
    hoặc thông báo nếu tên phòng đã tồn tại trên hệ thống
    {
        "name": [
            "Phòng ban với tên 'TNOC2' đã tồn tại."
        ]
    }

    Ví dụ: curl -X POST http://localhost:8000/department/create/ -H "Content-Type: application/json" -d '{"name": "TNOC2", "description": "Phòng truyền dẫn"}'
    """
    # Deserialize dữ liệu từ request body và kiểm tra tính hợp lệ
    serializer = DepartmentSerializer(data=request.data)

    # Nếu dữ liệu hợp lệ thì lưu vào database
    if serializer.is_valid():
        serializer.save()

        # Trả về response với dữ liệu phòng ban vừa tạo và status code 201 (CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Nếu dữ liệu không hợp lệ thì trả về lỗi với status code 400 (BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def department_detail(request, pk):
    """
    Lấy thông tin chi tiết một phòng ban

    Endpoint: GET /department/{id}/
    Mô tả: Trả về thông tin chi tiết của một phòng ban dựa trên ID
    Input: ID của phòng ban cần lấy (pk) - thay thế {id} bằng ID thực tế
    Output: Thông tin phòng ban dưới dạng JSON
    {
        "id": 3,
        "name": "SNOC2",
        "description": "Phòng chuyển mạch"
    }

    Ví dụ: curl -X GET http://localhost:8000/department/3/
    """
    # Lấy đối tượng Department theo ID, nếu không tồn tại thì trả về lỗi 404
    department = get_object_or_404(Department, pk=pk)

    # Serialize dữ liệu của phòng ban đó
    serializer = DepartmentSerializer(department)

    # Trả về response với dữ liệu serialized
    return Response(serializer.data)


@api_view(['PUT'])
def department_update(request, pk):
    """
    Cập nhật toàn bộ thông tin một phòng ban

    Endpoint: PUT /department/{id}/update/
    Mô tả: Cập nhật toàn bộ thông tin của một phòng ban
    Input: ID của phòng ban cần cập nhật (pk) và dữ liệu cập nhật
           Body (raw JSON): {"name": "SOC2", "description": "Phòng dịch vụ"}
    Output: Thông tin phòng ban đã cập nhật dưới dạng JSON
    {
        "id": 1,
        "name": "SOC2",
        "description": "Phòng dịch vụ"
    }

    Ví dụ: curl -X PUT http://localhost:8000/department/1/update/ \
               -H "Content-Type: application/json" \
               -d '{"name": "SOC2", "description": "Phòng dịch vụ"}'
    """
    # Lấy đối tượng Department theo ID, nếu không tồn tại thì trả về lỗi 404
    department = get_object_or_404(Department, pk=pk)

    # Deserialize dữ liệu từ request body và cập nhật vào đối tượng
    serializer = DepartmentSerializer(department, data=request.data)

    # Nếu dữ liệu hợp lệ thì lưu vào database
    if serializer.is_valid():
        serializer.save()

        # Trả về response với dữ liệu phòng ban đã cập nhật
        return Response(serializer.data)

    # Nếu dữ liệu không hợp lệ thì trả về lỗi với status code 400 (BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def department_partial_update(request, pk):
    """
    Cập nhật một phần thông tin phòng ban

    Endpoint: PATCH /department/{id}/partial-update/
    Mô tả: Cập nhật một phần thông tin của một phòng ban (chỉ những trường được cung cấp)
    Input: ID của phòng ban cần cập nhật (pk) và dữ liệu cập nhật một phần
           Body (raw JSON): {"name": "RNOC2"} hoặc {"description": "Phòng vô tuyến"}
    Output: Thông tin phòng ban đã cập nhật dưới dạng JSON
    {
        "id": 1,
        "name": "SOC2",
        "description": "Phòng vô tuyến"
    }

    Ví dụ: curl -X PATCH http://localhost:8000/department/1/partial-update/ \
               -H "Content-Type: application/json" \
               -d '{"name": "Phòng vô tuyến"}'
    """
    # Lấy đối tượng Department theo ID, nếu không tồn tại thì trả về lỗi 404
    department = get_object_or_404(Department, pk=pk)

    # Deserialize dữ liệu từ request body và cập nhật một phần vào đối tượng
    serializer = DepartmentSerializer(department, data=request.data, partial=True)

    # Nếu dữ liệu hợp lệ thì lưu vào database
    if serializer.is_valid():
        serializer.save()

        # Trả về response với dữ liệu phòng ban đã cập nhật
        return Response(serializer.data)

    # Nếu dữ liệu không hợp lệ thì trả về lỗi với status code 400 (BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def department_delete(request, pk):
    """
    Xóa một phòng ban

    Endpoint: DELETE /department/{id}/delete/
    Mô tả: Xóa một phòng ban khỏi hệ thống
    Input: ID của phòng ban cần xóa (pk) - thay thế {id} bằng ID thực tế
    Output: Response với status code 204

    Ví dụ: curl -X DELETE http://localhost:8000/department/1/delete/
    """
    # Lấy đối tượng Department theo ID, nếu không tồn tại thì trả về lỗi 404
    department = get_object_or_404(Department, pk=pk)

    # Xóa đối tượng khỏi database
    department.delete()

    # Trả về response rỗng với status code 204 (NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def department_detail_by_name(request, name):
    """
    API endpoint để lấy thông tin phòng ban theo tên

    Endpoint: GET /department/name/{name}/
    Mô tả: Trả về thông tin phòng ban theo tên
    Input: Tên phòng ban cần tìm kiếm (name) - thay thế {name} bằng tên thực tế
    Output: Thông tin phòng ban dưới dạng JSON
    {
        "id": 3,
        "name": "SNOC2",
        "description": "Phòng chuyển mạch"
    }

    Ví dụ: curl -X GET http://localhost:8000/department/name/SNOC2/
    """
    # Lấy đối tượng Department theo tên, nếu không tồn tại thì trả về lỗi 404
    try:
        department = Department.objects.get(name=name)
    except Department.DoesNotExist:
        from django.http import Http404
        raise Http404("Department does not exist")

    # Serialize dữ liệu của phòng ban đó
    serializer = DepartmentSerializer(department)

    # Trả về response với dữ liệu serialized
    return Response(serializer.data)
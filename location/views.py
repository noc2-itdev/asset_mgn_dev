"""
Views cho ứng dụng location
Xử lý các yêu cầu HTTP cho quản lý vị trí lắp đặt
"""
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from main.models import Location
from .serializers import LocationSerializer


class LocationListView(generics.ListCreateAPIView):
    """
    View xử lý danh sách và tạo mới vị trí lắp đặt
    GET: Lấy danh sách tất cả vị trí lắp đặt
    POST: Tạo mới một vị trí lắp đặt
    """
    pass


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View xử lý chi tiết, cập nhật và xóa vị trí lắp đặt
    GET: Lấy thông tin chi tiết một vị trí lắp đặt
    PUT/PATCH: Cập nhật thông tin vị trí lắp đặt
    DELETE: Xóa vị trí lắp đặt
    """
    pass

@api_view(['POST'])
def location_create(request):
    """
    Docstring for location_create
    Tạo mới vị trí lắp đặt
    Endpoint: POST /location/create/
    Mô tả: Tạo mới vị trí lắp đặt trong hệ thống
    Input: Dữ liệu vị trí lắp đặt cần tạo (name, description)
        Bode (raw JSON): {"name": "N21-NOC", "description": "Phòng trực nhà 21"}
    Output:
        {
            "id": 1,
            "name": "N21-NOC",
            "description": "Phòng trực nhà 21"
        }  
    hoặc thông báo nếu địa điểm đã tồn tại

    {
        "name": [
            "Địa điểm lắp đặt với tên 'N21-NOC' đã tồn tại."
        ]
    
    }
        
    :param request: Description
    """
    # Deserialoze dữ liệu từ request boty và kiểm tra tính hợp lệ
    
    serializer = LocationSerializer(data=request.data)
    # Nếu dữ liệu hợp lệ thì lưu vào database
    if serializer.is_valid():
        serializer.save()

        # Trả về reponse với dữ liệu vừa tạo và status code 201 (CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Nếu dữ liệu không hợp lệ thì trả về lỗi với status code 404 (BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)      



@api_view(['GET'])
def location_detail(request, pk):
    """
    API endpoint để lấy thông tin vị trí lắp đặt theo tên
    GET: /location/{id}/
    Mô tả: Trả về thông vị trí lắp đặt theo tên
    Input: Không yêu cầu tham số
    Output: Danh sách vị trí lắp đặt dưới dạng JSON
    [
        {
            "id": 1,
            "name": "N21-NOC",
            "description": "Phòng trực nhà 21"
        }   
    ]

    """
    # Lấy đối tượng location theo ID, nếu không tồn tại thì trả về lỗi 404
    locations = get_object_or_404(Location, pk=pk)

    # Serialize dữ liệu của phòng ban đó
    serializer = LocationSerializer(locations)

    # Trả về respone với dữ liệu serialized
    return Response(serializer.data)



    



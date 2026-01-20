from rest_framework import serializers
from main.models import Person
import re


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Person
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = Person
        fields = '__all__'
        # TODO: Triển khai các phương thức xác thực dữ liệu
        # TODO: Thêm phương thức validate_name để xác thực tên người
        # TODO: Thêm phương thức để xử lý tài sản liên quan trong danh mục
    def validate(self, data):
        name = data.get('name')
        email = data.get('email')
        #Lấy instance hiện tại (trong trường hợp cập nhật)
        instance = self.instance
        #Tên người ít nhất 2 ký tự
        if len(name.strip()) < 2:
            raise serializers.ValidationError("Tên người phải lớn hơn 2 ký tự")
        #Kiểm tra tên người không chứa ký tự đặc biết
        if not re.match(r'^[a-zA-ZÀ-ỹ\s]+$', name):
            raise serializers.ValidationError("Tên người không được chứa ký tự đặc biệt")        
        #Kiểm tra email người dùng đã tồn tại hay chưa
        if email:
            email_query = Person.objects.filter(email__iexact=email)
            if instance:
                email_query = email_query.exclude(pk=instance.pk) 
            if email_query.exists():
                raise serializers.ValidationError({
                "email": "Email này đã được sử dụng bởi một nhân viên khác. Vui lòng nhập email khác."
             })
        #Kiểm tra người dùng đã tồn tại hay chưa, nếu trùng thì yêu cầu nhập email
        queryset = Person.objects.filter(name__iexact=name)
        #Nếu đang cập nhật, bỏ qua chính instance hiện tại
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)
        
        #Nếu bị trùng tên thì tiếp tục kiểm tra email
        if queryset and not email:
                raise serializers.ValidationError({"email": f"Đã có nhân viên tên '{name}' trong hệ thống. "f"Vui lòng cung cấp email để phân biệt người này."})        
        return data


        
        



"""
Serializers cho ứng dụng department
Xử lý chuyển đổi dữ liệu giữa model và JSON
"""
from rest_framework import serializers
from main.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer cho model Department
    Chuyển đổi dữ liệu giữa model và JSON format
    """
    class Meta:
        model = Department
        fields = '__all__'

    def validate_name(self, value):
        """
        Kiểm tra xem tên phòng ban đã tồn tại chưa

        Trường hợp CREATE:
        - self.instance sẽ là None vì chưa có instance nào được tạo
        - Queryset sẽ kiểm tra tất cả các phòng ban có name trùng với value
        - Nếu tìm thấy, trả ra lỗi vì tên đã tồn tại

        Trường hợp UPDATE:
        - self.instance sẽ là instance hiện tại đang được cập nhật
        - Queryset sẽ kiểm tra các phòng ban có name trùng với value, trừ chính instance hiện tại
        - Nếu tìm thấy, trả ra lỗi vì tên đã được sử dụng bởi phòng ban khác
        - Nếu không tìm thấy, cho phép cập nhật tên thành công

        Ví dụ:
        - Có 2 phòng ban: 'TNOC2' (ID=1) và 'SNOC2' (ID=2)
        - Trường hợp CREATE: Nếu tạo phòng ban mới với tên 'TNOC2' -> lỗi
        - Trường hợp UPDATE (ID=1): Nếu đổi tên 'TNOC2' thành 'SOC2' -> OK
        - Trường hợp UPDATE (ID=1): Nếu đổi tên 'TNOC2' thành 'SNOC2' -> lỗi
        - Trường hợp UPDATE (ID=1): Nếu giữ nguyên tên 'TNOC2', chỉ thay đổi description -> OK
        """
        # Lấy instance hiện tại (trong trường hợp cập nhật)
        instance = self.instance

        # Kiểm tra xem có phòng ban nào khác với tên trùng không
        # Nếu đang cập nhật, bỏ qua chính instance hiện tại
        queryset = Department.objects.filter(name=value)
        if instance is not None:
            queryset = queryset.exclude(pk=instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(f"Phòng ban với tên '{value}' đã tồn tại.")

        return value
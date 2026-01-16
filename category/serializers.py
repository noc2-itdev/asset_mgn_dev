"""
Serializers cho ứng dụng category
Xử lý chuyển đổi dữ liệu giữa model và JSON
Dưới đây là khung cho các action cần triển khai:
- Tạo mới danh mục tài sản
- Cập nhật danh mục tài sản
- Xóa danh mục tài sản
- Lấy danh sách danh mục tài sản
- Lấy chi tiết danh mục tài sản theo ID
- Lấy danh mục tài sản theo tên
"""
from rest_framework import serializers
from main.models import AssetCategory
import re

class AssetCategorySerializer(serializers.ModelSerializer):
    """
    Serializer cho model AssetCategory
    Chưa triển khai đầy đủ - dành cho developer tiếp tục phát triển
    """
    class Meta:
        model = AssetCategory
        fields = '__all__'
        # TODO: Triển khai các phương thức xác thực dữ liệu
        # TODO: Thêm phương thức validate_name để xác thực tên danh mục
        # TODO: Thêm phương thức để xử lý tài sản liên quan trong danh mục
    def validate_name(self, value):

        # Xác thực tên danh mục phải hơn 2 ký tự
        if len(value.strip()) < 2:

            raise serializers.ValidationError("Tên danh mục phải có ít nhất 2 ký tự.")
        
        """
        re.match(): Hàm kiểm tra xem chuỗi có khớp với khuôn mẫu từ đầu đến cuối không.

        r: Ký hiệu "raw string", giúp Python xử lý các dấu gạch chéo ngược (\) chính xác hơn.

        ^: Bắt đầu chuỗi.

        $: Kết thúc chuỗi.

        [\w\sà-ỹÀ-Ỹ]: Đây là tập hợp các ký tự cho phép:

        \w: Chữ cái và chữ số.

        \s: Khoảng trắng (dấu cách).

        à-ỹÀ-Ỹ: Các ký tự tiếng Việt có dấu.

        +: Cho phép có 1 hoặc nhiều ký tự như vậy.
        
        """
        # Kiểm tra Danh mục có chứa ký tự đặc biệt hay không
        if not re.match(r'^[\w\sà-ỹÀ-Ỹ]+$', value):
            raise serializers.ValidationError("Tên danh mục không được chứa ký tự đặc biệt")

        
        
        """
        Kiểm tra tên danh mục đã tồn tại hay chưa, nếu có thì không cho tạo
        
        """
        # Lấy instance hiện tại, nếu cập nhật là có còn tạo mới thì None
        instance = self.instance
        # Kiểm tra xem danh mục tài sản có bị trùng hay không
        # Nếu đang cập nhật, bỏ qua chính instance hiện tại
        #Truy vấn vào database xem tên đã có hay chưa, queryset là danh sách các bản ghi thu được từ lệnh filter với tên là value
        queryset = AssetCategory.objects.filter(name=value)
        # Nếu danh mục tồn tại, tức là đang cập nhật thông tin chứ không tạo mới.
        if instance is not None:
            # danh sách bản ghi sau khi đã loại bỏ chính instance hiện tại, dù cho việc cập nhật thông tin
            queryset = queryset.exclude(pk=instance.pk)
        # Nếu queryset vẫn còn tức là danh mục tài sản mới đã tồn tại
        if queryset.exists():
            raise serializers.ValidationError(f"Danh mục tài sản với tên '{value}' đã tồn tại.")
        # Trả lại giá trị để lưu vào trong database, giá trị mới hoặc giá trị cập nhật
        return value

  """   def validate(self, data):
        # xác thực danh mục là linh kiện hay tài sản chính. (máy tính, máy in, RAM, SSD,...).
        name = data.get('name', '').lower()
        is_component_input = data.get('is_component')
        # nếu danh mục là linh kiện
        if is_component_input:
            # lấy danh sách tài sản chính
            # flat= True: làm phẳng kết quả, thành danh sách
            main_asset_queryset = AssetCategory.objects.filter(is_component=False).values_list('name', flat= True)
            # chuyển danh sách sang chữ thường để dễ so sánh
            main_asset = [item.lower() for item in main_asset_queryset]
            if any(asset in name for asset in main_asset_queryset):
                raise serializers.ValidationError({"is_component":"Tên này chưa từ khóa của một Tài sản chính đã tồn tại, vui lòng kiểm tra lại"})


        return data """
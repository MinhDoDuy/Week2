# Module = Một file Python có sẵn (hoặc bạn tự viết) chứa sẵn các hàm, biến, lớp để tái sử dụng.

# 1. Sử dụng module có sẵn
import math

x = math.sqrt(4)  # Sử dụng hàm sqrt (Căn) từ module math
print(x)
print("-------------------")

# 2. Các hàm toán học thường dùng trong module math
# Dùng khi cần tính toán chính xác, làm việc với số thập phân, lượng giác, log...
import math

print(math.pi)
print(math.sqrt(9))
print(math.pow(2, 3))  # 2 mũ 3
print(math.ceil(3.4))  # Làm tròn lên
print(math.floor(3.7))  # Làm tròn xuống
print("-------------------")

# 3. Sinh dữ liệu ngẫu nhiên với module random
# Dùng để sinh số, chọn phần tử ngẫu nhiên (thường dùng trong game, test dữ liệu, tạo mật khẩu,…)
import random

print(random.randint(1, 10))  # Số nguyên ngẫu nhiên từ 1 đến 10
print(random.random())  # Số thực ngẫu nhiên từ 0 đến 1
print(random.choice(['apple', 'banana', 'cherry']))  # Chọn ngẫu nhiên
print(random.sample(range(1, 20), 3))  # Lấy mẫu ngẫu nhiên 3 số từ 1 đến 20
print("-------------------")

# 4. Làm việc với thời gian bằng module datetime
# Dùng để lấy thời gian hiện tại, định dạng ngày tháng, tính toán với thời gian,...
from datetime import datetime, timedelta

now = datetime.now()  # Lấy thời gian hiện tại
print("Thời gian hiện tại: ", now)

# Định dạng ngày giờ đẹp hơn
formatted = now.strftime("%d/%m/%Y - %H:%M:%S")
print("Định dạng: ", formatted)

# Tính toán với thời gian
tomorrow = now + timedelta(days=1)
print("Ngày mai: ", tomorrow.strftime("%d/%m/%Y"))

yesterday = now - timedelta(days=1)
print("Hôm qua: ", yesterday.strftime("%d/%m/%Y"))

# Rõ ngày giờ cụ thể
print(now.strftime("Hôm nay là %A tháng %B, ngày %d/tháng %m/năm %Y và bây giờ là %H/phút %M/giây %S"))
# %A là tên ngày trong tuần, %B là tên tháng
# %a là tên viết tắt ngày trong tuần, %b là tên viết tắt tháng
print("-------------------")

# 5. Tạo ngày ngẫu nhiên
# Giả sử bạn muốn sinh ra ngày sinh ngẫu nhiên cho người dùng:
from datetime import datetime, timedelta
import random


def get_date_input(prompt):
    """Hàm nhập và kiểm tra ngày hợp lệ"""
    while True:
        user_input = input(prompt)
        for fmt in ("%d-%m-%Y", "%d/%m/%Y"):
            try:
                # Thử chuyển chuỗi nhập vào thành datetime
                date_obj = datetime.strptime(user_input, fmt)
                return date_obj
            except ValueError:
                pass
        print("Định dạng ngày không hợp lệ! Vui lòng nhập lại theo định dạng dd-mm-YYYY hoặc dd/mm/YYYY.")


# Nhập 2 ngày có kiểm tra
start_date = get_date_input("Nhập ngày bắt đầu (dd-mm-YYYY): ")
end_date = get_date_input("Nhập ngày kết thúc (dd-mm-YYYY): ")

# Kiểm tra xem ngày kết thúc có sau ngày bắt đầu không
if end_date <= start_date:
    print("Ngày kết thúc phải sau ngày bắt đầu!")
    end_date = get_date_input("Nhập lại ngày kết thúc (dd-mm-YYYY): ")
else:
    # Tính số ngày giữa hai mốc
    delta_days = (end_date - start_date).days

    # Sinh ngẫu nhiên 1 số trong khoảng đó
    random_days = random.randint(0, delta_days)

    # Cộng vào ngày bắt đầu để ra ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In kết quả
    print("✅ Ngày ngẫu nhiên là:", random_date.strftime("%d-%m-%Y"))

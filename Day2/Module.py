#Module = Một file Python có sẵn (hoặc bạn tự viết) chứa sẵn các hàm, biến, lớp để bạn dùng lại.

#1. Sử dụng module có sẵn
import math
x = math.sqrt(4) # Sử dụng hàm sqrt (Căn) từ module math
print(x)
print("-------------------")

#2. Các hàm toán học thường dùng trong module math
#Dùng khi cần tính toán chính xác, làm việc với số thập phân, lượng giác, log...
import math
print(math.pi)
print(math.sqrt(9))
print(math.pow(2, 3)) # 2 mũ 3
print(math.ceil(3.4)) # Làm tròn lên
print(math.floor(3.7)) # Làm tròn xuống
print("-------------------")

#3. Sinh dữ liệu ngẫu nhiên với module random
#Dùng để sinh số, chọn phần tử ngẫu nhiên (thường dùng trong game, test dữ liệu, tạo mật khẩu,…)
import random
print(random.randint(1, 10)) # Số nguyên ngẫu nhiên từ 1 đến 10
print(random.random()) # Số thực ngẫu nhiên từ 0 đến 1
print(random.choice(['apple', 'banana', 'cherry'])) # Chọn ngẫu nhiên
print(random.sample(range(1, 20), 3)) # Lấy mẫu ngẫu nhiên 3 số từ 1 đến 20
print("-------------------")

#4. Làm việc với thời gian bằng module datetime
#Dùng để lấy thời gian hiện tại, định dạng ngày tháng, tính toán với thời gian,...
from datetime import datetime, timedelta
now = datetime.now() # Lấy thời gian hiện tại
print("Thời gian hiện tại: ", now)

#Định dạng ngày giờ đẹp hơn
formatted = now.strftime("%d/%m/%Y - %H:%M:%S")
print("Định dạng: ", formatted)

#Tính toán với thời gian
tomorrow = now + timedelta(days=1)
print("Ngày mai: ", tomorrow.strftime("%d/%m/%Y"))

yesterday = now - timedelta(days=1)
print("Hôm qua: ", yesterday.strftime("%d/%m/%Y"))
print("-------------------")
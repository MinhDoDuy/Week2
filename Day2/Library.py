# Library

# Là một tập hợp nhiều module có cùng mục đích (gói lớn).
# math, random, datetime là các standard libraries (thư viện tiêu chuẩn) — Python cài sẵn.
# requests, flask, pandas là các external libraries — phải cài thêm bằng pip.

# 1. Cách import module
# a. Import toàn bộ module
import math

print(math.sqrt(16))
print(math.pi)

# b. Import riêng hàm hoặc lớp
from math import sqrt, pi

print(sqrt(25))
print(pi)

# c. Đặt bí danh (alias)
import datetime as dt

print(dt.datetime.now())
print("-------------------")

# 2. Thư viện math - toán học cơ bản
import math

print(math.sqrt(25))  # căn bậc hai
print(math.pow(2, 3))  # lũy thừa (2^3 = 8)
print(math.ceil(3.4))  # làm tròn lên → 4
print(math.floor(3.9))  # làm tròn xuống → 3
print(math.pi)  # số π
print(math.e)  # số e
print("-------------------")

# 3. Thư viện random - sinh số ngẫu nhiên
import random

print(random.randint(1, 10))  # số nguyên ngẫu nhiên 1–10
print(random.uniform(1, 10))  # số thực ngẫu nhiên 1–10
print(random.choice(["a", "b", "c"]))  # chọn ngẫu nhiên 1 phần tử
print(random.sample(range(10), 3))  # chọn 3 số khác nhau trong 0–9

print("-------------------")

# 4. Thư viện datetime - làm việc với ngày giờ
from datetime import datetime, timedelta

now = datetime.now()  # thời gian hiện tại
print(now.strftime("%d-%m-%Y - %H:%M:%S"))

# Cộng trừ ngày
future = now + timedelta(days=7)
print("Sau 7 ngày:", future.strftime("%d-%m-%Y"))

# utils.py
def get_numbers_from_user():
    """Nhập danh sách số, kiểm tra lỗi."""
    while True:
        try:
            user_input = input("Nhập các số (cách nhau bằng khoảng trắng): ")
            numbers = [float(x) for x in user_input.split()]
            return numbers
        except ValueError:
            print("⚠️ Vui lòng nhập số hợp lệ!")

def calculate_stats(numbers):
    """Tính trung bình và số lớn nhất."""
    avg = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return avg, maximum

📊 CHƯƠNG TRÌNH TÍNH TOÁN SỐ LIỆU
Trung bình: 4.4
Lớn nhất: 10.0


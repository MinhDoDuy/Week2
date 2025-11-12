# Định nghĩa class Student
class Student:
    # Hàm khởi tạo (constructor) chạy khi tạo đối tượng
    def __init__(self, name, grade):
        self.name = name     # thuộc tính name
        self.grade = grade   # thuộc tính grade

    # Phương thức hiển thị thông tin học sinh
    def show_info(self):
        print(f"{self.name}: {self.grade}")

# Tạo 2 đối tượng học sinh
s1 = Student("Minh", 9.0)
s2 = Student("An", 8.5)

# Gọi phương thức show_info() của từng đối tượng
s1.show_info()
s2.show_info()

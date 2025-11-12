import json

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Tạo danh sách học sinh
students = [
    Student("Minh", 9.0),
    Student("An", 8.5),
    Student("Linh", 7.8)
]

# Chuyển sang dict để ghi file JSON
data = [{"name": s.name, "grade": s.grade} for s in students]

with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

print("Đã lưu danh sách học sinh vào students.json")

# Đọc lại dữ liệu
with open("students.json", "r") as f:
    loaded = json.load(f)
    print("\nDữ liệu đọc từ file:", loaded)

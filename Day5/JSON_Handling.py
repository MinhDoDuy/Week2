import json  # module để xử lý dữ liệu JSON

# Định nghĩa class Student
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Tạo danh sách đối tượng học sinh
students = [
    Student("Minh", 9.0),
    Student("An", 8.5),
    Student("Linh", 7.8)
]

# Chuyển danh sách đối tượng sang list dict (để ghi ra JSON)
data = [{"name": s.name, "grade": s.grade} for s in students]

# Ghi dữ liệu ra file JSON (có format đẹp với indent=4)
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

print("Đã lưu danh sách học sinh vào students.json")

# Đọc lại dữ liệu từ file JSON
with open("students.json", "r") as f:
    loaded = json.load(f)  # parse JSON -> list dict
    print("\nDữ liệu đọc từ file:", loaded)

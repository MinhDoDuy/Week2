# import json  # module để xử lý dữ liệu JSON
#
# # Định nghĩa class Student
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
# # Tạo danh sách đối tượng học sinh
# students = [
#     Student("Minh", 9.0),
#     Student("An", 8.5),
#     Student("Linh", 7.8)
# ]
#
# # Chuyển danh sách đối tượng sang list dict (để ghi ra JSON)
# data = [{"name": s.name, "grade": s.grade} for s in students]
#
# # Ghi dữ liệu ra file JSON (có format đẹp với indent=4)
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4)
#
# print("Đã lưu danh sách học sinh vào students.json")
#
# # Đọc lại dữ liệu từ file JSON
# with open("students.json", "r") as f:
#     loaded = json.load(f)  # parse JSON -> list dict
#     print("\nDữ liệu đọc từ file:", loaded)

import json

import json

# Định nghĩa class Student
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

students = []

while True:
    # Nhập tên, exit để dừng
    name = input("Nhập tên học sinh (hoặc 'exit' để thoát, chỉ chữ): ")
    if name.lower() == "exit":
        break

    # Kiểm tra tên chỉ chứa chữ và khoảng trắng
    if not name.replace(" ", "").isalpha():
        print("❌ Tên không hợp lệ, chỉ được nhập chữ, thử lại!")
        continue

    # Nhập điểm hợp lệ 0–10
    while True:
        grade_input = input(f"Nhập điểm của {name} (0-10): ")
        try:
            grade = float(grade_input)
            if 0 <= grade <= 10:
                break
            else:
                print("❌ Điểm phải trong khoảng 0–10, thử lại!")
        except ValueError:
            print("❌ Điểm không hợp lệ, thử lại!")

    students.append(Student(name, grade))

# Chuyển sang dict để lưu JSON
data = [{"name": s.name, "grade": s.grade} for s in students]

# Ghi ra file
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Đã lưu danh sách học sinh vào students.json")

# Đọc lại dữ liệu để kiểm tra
with open("students.json", "r") as f:
    loaded = json.load(f)
    print("\nDữ liệu đọc từ file:")
    for s in loaded:
        print(f"{s['name']}: {s['grade']}")

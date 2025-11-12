class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self):
        print(f"{self.name}: {self.grade}")

# Tạo đối tượng
s1 = Student("Minh", 9.0)
s2 = Student("An", 8.5)

s1.show_info()
s2.show_info()

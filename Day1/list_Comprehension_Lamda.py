#1.List Comprehension
#List comprehension giúp bạn tạo list mới dựa trên list có sẵn — chỉ trong một dòng.

#a. Tạo list bình phương các số:
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

#b. Tạo list các số chẵn:
even_numbers = [n for n in range(10) if n % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

# Tạo list bình phương của các số chẵn:
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16]

#c. List comprehension lồng nhau (nâng cao)
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5]]
print(pairs)  # [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

#2. Lambda Function
# Lambda là hàm không tên, dùng cho những thao tác đơn giản, ngắn gọn.

#a. Hàm lambda cơ bản:
add = lambda x, y: x + y
print(add(2, 3))  # 5

#b. Sử dụng lambda với hàm map:
#Áp dụng hàm cho mỗi phần tử trong danh sách.
numbers = [1,2,3,4,5]
square = list(map(lambda x: x ** 2, numbers))
print(square)  # [1, 4, 9, 16, 25]

#c. Sử dụng lambda với hàm filter:
#Giữ những phần tử mà hàm điều kiện trả về True.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

#d. Ket hop ca hai
numbers = [1, 2, 3, 4, 5, 6]
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numbers)))
print(even_squares)  # [9, 36]

#1. Tạo list bình phương các số:
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

#2. Tạo list các số chẵn:
even_numbers = [n for n in range(10) if n % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16]

#3. List comprehension lồng nhau (nâng cao)
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5]]
print(pairs)  # [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
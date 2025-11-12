#Ghi log người dùng nhập vào file
# Mở file user_log.txt ở chế độ append (thêm nội dung, không xóa cũ)
with open("user_log.txt", "a") as f:
    while True:  # vòng lặp vô hạn cho đến khi người dùng gõ 'exit'
        text = input("Nhập nội dung (hoặc 'exit' để thoát): ")
        if text.lower() == "exit":  # nếu người dùng gõ 'exit'
            break                   # thoát vòng lặp
        f.write(text + "\n")        # ghi nội dung vào file, xuống dòng

print("Nội dung đã được ghi vào user_log.txt")

#Đọc lại nôị dung file
with open("user_log.txt", "r") as f:
    print("Nội dung file user_log.txt:")
    content = f.read()
    print(content) #In toàn bộ nội dung file
#Ghi log người dùng nhập vào file
with open("user_log.txt", "a") as f:
    while True:
        text = input("Nhập nội dung log (hoặc 'exit' để thoát): ")
        if text.lower() == 'exit':
            break
        f.write(f"{text}\n")

print("Nội dung đã được ghi vào user_log.txt")

#Đọc lại nôị dung file
with open("user_log.txt", "r") as f:
    print("Nội dung file user_log.txt:")
    content = f.read()
    print(content)
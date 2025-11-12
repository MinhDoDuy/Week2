# #Ghi log người dùng nhập vào file
# # Mở file user_log.txt ở chế độ append (thêm nội dung, không xóa cũ)
# with open("user_log.txt", "a") as f:
#     while True:  # vòng lặp vô hạn cho đến khi người dùng gõ 'exit'
#         text = input("Nhập nội dung (hoặc 'exit' để thoát): ")
#         if text.lower() == "exit":  # nếu người dùng gõ 'exit'
#             break                   # thoát vòng lặp
#         f.write(text + "\n")        # ghi nội dung vào file, xuống dòng
#
# print("Nội dung đã được ghi vào user_log.txt")
#
# #Đọc lại nôị dung file
# with open("user_log.txt", "r") as f:
#     print("Nội dung file user_log.txt:")
#     content = f.read()
#     print(content) #In toàn bộ nội dung file

import os  # import module os để thao tác với file (xóa, kiểm tra tồn tại, ...)

file_path = "user_log.txt"  # đặt tên file log

while True:  # vòng lặp menu chính, chạy liên tục đến khi chọn thoát
    # Hiển thị menu
    print("\n=== MENU ===")
    print("1. Nhập log mới")
    print("2. Xem log")
    print("3. Xóa nội dung file")
    print("4. Xóa hẳn file")
    print("5. Thoát")

    choice = input("Chọn 1-5: ")  # nhận lựa chọn từ người dùng

    if choice == "1":
        # Mở file ở chế độ append để thêm log mới, không xóa dữ liệu cũ
        with open(file_path, "a") as f:
            while True:  # vòng lặp nhập nhiều dòng log
                text = input("Nhập nội dung log (hoặc 'e' để dừng): ")  # nhập từng dòng
                if text.lower() == "e":  # nếu gõ 'exit' thì dừng nhập
                    break
                f.write(text + "\n")  # ghi dòng log vào file, xuống dòng
        print("✅ Đã lưu log.")  # thông báo đã lưu

    elif choice == "2":
        # Xem nội dung file
        if os.path.exists(file_path):  # kiểm tra file có tồn tại không
            with open(file_path, "r") as f:  # mở file đọc
                print("\n--- Nội dung file ---")
                print(f.read())  # in toàn bộ nội dung file
        else:
            print("❌ File không tồn tại.")  # báo lỗi nếu file chưa có

    elif choice == "3":
        # Xóa nội dung file nhưng giữ file
        if os.path.exists(file_path):  # kiểm tra file tồn tại
            confirm = input("⚠ Bạn có chắc chắn muốn xóa Nội Dung file không? (Y/N): ")  # hỏi xác nhận
            if confirm.lower() == "y":  # nếu đồng ý
                with open(file_path, "w") as f:  # mở file ghi mới → xóa hết nội dung cũ
                    pass  # không ghi gì
                print("✅ Nội dung file đã bị xóa.")  # thông báo thành công
            else:
                print("❌ Hủy thao tác xóa nội dung file.")  # nếu không đồng ý
        else:
            print("❌ File không tồn tại.")  # file chưa tồn tại

    elif choice == "4":
        # Xóa hẳn file
        if os.path.exists(file_path):  # kiểm tra file tồn tại
            confirm = input("⚠ Bạn có chắc chắn muốn Xóa File này không? (Y/N): ")  # hỏi xác nhận
            if confirm.lower() == "y":  # nếu đồng ý
                os.remove(file_path)  # xóa file khỏi hệ thống
                print("✅ File đã bị xóa.")  # thông báo thành công
            else:
                print("❌ Hủy thao tác xóa file.")  # nếu không đồng ý
        else:
            print("❌ File không tồn tại.")  # file chưa tồn tại

    elif choice == "5":
        print("Thoát chương trình.")  # thông báo thoát
        break  # thoát vòng lặp menu

    else:
        print("❌ Chỉ được nhập số từ 1 - 5.")  # xử lý nhập sai


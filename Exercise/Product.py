import json  # để làm việc với JSON
import os    # để kiểm tra file tồn tại

# 1️⃣ Định nghĩa class Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# 2️⃣ Đọc dữ liệu từ file text
input_file = "products.txt"   # file chứa danh sách sản phẩm
output_file = "products.json" # file JSON sẽ lưu

products = []  # list lưu các đối tượng Product

# Kiểm tra file tồn tại
if not os.path.exists(input_file):
    print(f"❌ File {input_file} không tồn tại!")
else:
    try:
        with open(input_file, "r") as f:
            for line_number, line in enumerate(f, 1):  # đọc từng dòng, đánh số dòng
                line = line.strip()  # loại bỏ khoảng trắng thừa và xuống dòng
                if not line:  # bỏ qua dòng trống
                    continue
                parts = line.split(",")  # giả sử định dạng: name,price,quantity
                if len(parts) != 3:
                    print(f"❌ Dữ liệu không hợp lệ ở dòng {line_number}: {line}")
                    continue
                name, price_str, quantity_str = parts
                try:
                    price = float(price_str)
                    quantity = int(quantity_str)
                    product = Product(name.strip(), price, quantity)  # tạo object Product
                    products.append(product)
                except ValueError:
                    print(f"❌ Sai định dạng số ở dòng {line_number}: {line}")
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")

# 3️⃣ Chuyển list object sang list dict để lưu JSON
data = [{"name": p.name, "price": p.price, "quantity": p.quantity} for p in products]

# 4️⃣ Ghi dữ liệu JSON ra file
try:
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Đã lưu dữ liệu vào {output_file}")
except Exception as e:
    print(f"❌ Lỗi khi ghi file JSON: {e}")

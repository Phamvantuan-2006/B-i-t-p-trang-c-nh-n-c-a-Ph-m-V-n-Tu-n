# Nhập chuỗi
s = input("Nhap chuoi (it nhat 4 chu so): ")

# Lấy ra các ký tự là chữ số
digits = [ch for ch in s if ch.isdigit()]

# Kiểm tra đủ 4 chữ số không
if len(digits) < 4:
    print("Khong du 4 chu so!")
else:
    k = 4  # cần chọn 4 chữ số
    result = []
    start = 0  # vị trí bắt đầu tìm

    for i in range(k):
        # Giới hạn vùng tìm kiếm
        # đảm bảo còn đủ ký tự phía sau
        end = len(digits) - (k - i) + 1

        # Tìm chữ số lớn nhất trong đoạn [start, end)
        max_digit = -1
        max_pos = start

        for j in range(start, end):
            if int(digits[j]) > max_digit:
                max_digit = int(digits[j])
                max_pos = j

        # Thêm vào kết quả
        result.append(str(max_digit))

        # Cập nhật vị trí bắt đầu
        start = max_pos + 1

    # Ghép lại thành số
    print("So lon nhat con lai:", "".join(result))

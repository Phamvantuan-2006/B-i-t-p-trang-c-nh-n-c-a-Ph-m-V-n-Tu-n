# Hàm chuyển phân số s/t thành phân số liên tục [b1, b2, ..., bk]
def continued_fraction(s, t):
    result = []

    while t != 0:
        a = t // s        # Lấy phần nguyên
        result.append(a)  # Thêm vào danh sách

        r = t % s         # Số dư

        # Nếu dư = 0 thì dừng
        if r == 0:
            break

        # Biến đổi tiếp: s/t -> s/r -> (r, s)
        t, s = s, r

    return result


# ===== Chương trình chính =====
s, t = map(int, input("Nhap s, t (0 < s < t): ").split())

# Kiểm tra điều kiện
if s <= 0 or s >= t:
    print("Du lieu khong hop le!")
else:
    kq = continued_fraction(s, t)
    print(kq)

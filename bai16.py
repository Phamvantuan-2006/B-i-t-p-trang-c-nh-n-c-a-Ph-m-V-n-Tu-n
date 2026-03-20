# Hàm tính thứ của một ngày theo công thức Zeller
def zeller(day, month, year):
    # Nếu tháng là 1 hoặc 2 thì đổi thành 13, 14 của năm trước
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100

    # Công thức Zeller
    h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

    # Đổi về: 0=CN, 1=Thứ 2, ..., 6=Thứ 7
    return (h + 6) % 7


# Hàm kiểm tra năm nhuận
def la_nam_nhuan(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Số ngày trong từng tháng
def so_ngay_trong_thang(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if la_nam_nhuan(year) else 28


# ===== Chương trình chính =====
year = int(input("Nhap nam: "))

for month in range(1, 13):
    print(f"\nThang {month}:")
    print("S M T W T F S")  # Chủ nhật → Thứ 7

    # Tính thứ của ngày 1
    start_day = zeller(1, month, year)

    # Số ngày trong tháng
    days = so_ngay_trong_thang(month, year)

    # In khoảng trắng trước ngày 1
    print("  " * start_day, end="")

    # In các ngày
    for d in range(1, days + 1):
        print(f"{d:2}", end=" ")

        # Xuống dòng khi hết tuần
        if (start_day + d) % 7 == 0:
            print()

    print()  # Xuống dòng sau mỗi tháng

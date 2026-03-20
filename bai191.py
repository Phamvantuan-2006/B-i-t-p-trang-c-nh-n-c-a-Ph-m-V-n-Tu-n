import calendar

# Thiết lập tuần bắt đầu từ Chủ nhật (giống đề)
calendar.setfirstweekday(calendar.SUNDAY)

# Nhập tháng và năm
month, year = map(int, input("Nhap thang, nam (sau 1900): ").split())

# In tiêu đề
print(f"Thang {month} {year}")
print("CN Hai Ba Tu Nam Sau Bay")  # Tên các ngày trong tuần

# Lấy ma trận lịch của tháng
# Mỗi hàng là 1 tuần, ngày không thuộc tháng sẽ là 0
month_cal = calendar.monthcalendar(year, month)

# In từng tuần
for week in month_cal:
    for day in week:
        if day == 0:
            print("   ", end="")  # khoảng trống
        else:
            print(f"{day:2} ", end="")  # in ngày (2 ký tự)
    print()  # xuống dòng sau mỗi tuần

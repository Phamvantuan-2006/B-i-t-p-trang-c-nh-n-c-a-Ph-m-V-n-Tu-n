import math

# Nhập tử số và mẫu số (mẫu khác 0)
tu, mau = map(int, input("Nhap tu so, mau so: ").split())

# Đảm bảo mẫu số khác 0
if mau == 0:
    print("Mau so khong hop le!")
else:
    # Nếu mẫu âm → đổi dấu cả tử và mẫu
    if mau < 0:
        tu = -tu
        mau = -mau

    # Tìm UCLN (ước chung lớn nhất)
    ucln = math.gcd(tu, mau)

    # Rút gọn phân số
    tu //= ucln
    mau //= ucln

    # In kết quả
    print("Rut gon:", f"{tu}/{mau}")

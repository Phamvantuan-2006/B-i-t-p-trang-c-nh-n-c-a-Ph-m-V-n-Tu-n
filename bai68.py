import random

# Nhập n (n chẵn)
n = int(input("Nhap n (n chan): "))

# Kiểm tra n chẵn
if n % 2 != 0:
    print("n phai la so chan!")
else:
    # a. Tạo mảng ngẫu nhiên [100, 200]
    arr = [random.randint(100, 200) for _ in range(n)]

    print("Mang ban dau:")
    print(*arr)

    # b. Sắp xếp mảng tăng dần
    arr.sort()

    # Chia thành 2 nhóm:
    # nhóm nhỏ (n/2 phần tử đầu)
    # nhóm lớn (n/2 phần tử cuối)
    group1 = arr[:n//2]
    group2 = arr[n//2:]

    sum1 = sum(group1)
    sum2 = sum(group2)

    # Hiệu tổng
    diff = abs(sum1 - sum2)

    # In kết quả
    print("Nhom 1:", *group1)
    print("Nhom 2:", *group2)
    print("Tong 1:", sum1)
    print("Tong 2:", sum2)
    print("Hieu nho nhat:", diff)

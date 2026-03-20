import random

# Kích thước ma trận
n = 4

# a. Tạo ma trận 4x4 với giá trị ngẫu nhiên [-100, 100]
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-100, 100))
    A.append(row)

# In ma trận ban đầu
print("Mang goc:")
for row in A:
    print(*row)


# b. Sắp xếp ma trận
# Bước 1: Trải phẳng ma trận thành 1 mảng
flat = []
for row in A:
    flat.extend(row)

# Bước 2: Sắp xếp mảng tăng dần
flat.sort()

# Bước 3: Đưa lại vào ma trận theo thứ tự hàng
k = 0
for i in range(n):
    for j in range(n):
        A[i][j] = flat[k]
        k += 1

# In ma trận sau khi sắp xếp
print("\nMang sau khi sap xep:")
for row in A:
    print(*row)

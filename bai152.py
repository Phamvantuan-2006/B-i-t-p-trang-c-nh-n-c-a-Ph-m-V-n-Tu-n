# Hàm đệ quy kiểm tra mảng đối xứng
def is_symmetric(arr, left, right):
    # Điều kiện dừng:
    # Nếu left >= right → đã kiểm tra hết
    if left >= right:
        return True

    # Nếu 2 phần tử không bằng nhau → không đối xứng
    if arr[left] != arr[right]:
        return False

    # Gọi đệ quy kiểm tra phần còn lại
    return is_symmetric(arr, left + 1, right - 1)


# ===== Chương trình chính =====
# Nhập mảng (cách nhau bởi khoảng trắng)
arr = list(map(int, input("Nhap mang: ").split()))

# Gọi hàm kiểm tra
if is_symmetric(arr, 0, len(arr) - 1):
    print("Mang doi xung")
else:
    print("Mang khong doi xung")

# Hàm strspn: đếm số ký tự đầu tiên của s chỉ chứa các ký tự trong accept
def my_strspn(s, accept):
    count = 0
    for ch in s:
        if ch in accept:
            count += 1
        else:
            break  # gặp ký tự không thuộc accept thì dừng
    return count


# Hàm strncmp: so sánh n ký tự đầu của 2 chuỗi
def my_strncmp(s1, s2, n):
    for i in range(n):
        # Nếu vượt quá độ dài chuỗi
        if i >= len(s1) or i >= len(s2):
            return 0
        
        if s1[i] != s2[i]:
            # Trả về hiệu ASCII (giống C)
            return ord(s1[i]) - ord(s2[i])
    
    return 0  # giống nhau


# Hàm strstr: tìm chuỗi con trong chuỗi
def my_strstr(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i  # trả về vị trí đầu tiên
    return -1  # không tìm thấy


# ===== Chương trình chính =====
s = input("Chuoi kiem tra: ")
accept = input("Nhap tap ky tu (strspn): ")

# strspn
print("strspn =", my_strspn(s, accept))

# strncmp
s1 = input("Nhap chuoi 1: ")
s2 = input("Nhap chuoi 2: ")
n = int(input("So ky tu so sanh: "))
print("strncmp =", my_strncmp(s1, s2, n))

# strstr
sub = input("Nhap chuoi can tim: ")
pos = my_strstr(s, sub)

if pos != -1:
    print("Tim thay tai vi tri:", pos)
else:
    print("Khong tim thay")

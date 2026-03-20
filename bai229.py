# ================== Node AVL ==================
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


# ================== Hàm hỗ trợ ==================
def height(node):
    return node.height if node else 0


def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0


# ================== Xoay phải ==================
def rotate_right(y):
    x = y.left
    T2 = x.right

    # Xoay
    x.right = y
    y.left = T2

    # Cập nhật chiều cao
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# ================== Xoay trái ==================
def rotate_left(x):
    y = x.right
    T2 = y.left

    # Xoay
    y.left = x
    x.right = T2

    # Cập nhật chiều cao
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# ================== Chèn AVL ==================
def insert(root, key):
    # B1: chèn như BST
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # B2: cập nhật chiều cao
    root.height = 1 + max(height(root.left), height(root.right))

    # B3: kiểm tra cân bằng
    bf = balance_factor(root)

    # 4 trường hợp xoay

    # LL
    if bf > 1 and key < root.left.key:
        return rotate_right(root)

    # RR
    if bf < -1 and key > root.right.key:
        return rotate_left(root)

    # LR
    if bf > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # RL
    if bf < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


# ================== Tìm kiếm ==================
def search(root, key):
    if root is None:
        return None

    if root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)


# ================== In cây dạng đề ==================
def print_tree(root, level=0, side=""):
    if root:
        print("   " * level + f"({root.key},{side})")
        print_tree(root.left, level + 1, "L")
        print_tree(root.right, level + 1, "R")


# ================== Chương trình chính ==================
root = None

# Nhập dãy số
arr = list(map(int, input("Nhap cac khoa: ").split()))

# Chèn từng phần tử
for x in arr:
    root = insert(root, x)

# In cây AVL
print("\nCay AVL:")
print_tree(root)

# Tìm kiếm
k = int(input("\nNhap khoa can tim: "))

res = search(root, k)

if res:
    print(f"[{k}, found]")
else:
    print(f"[{k}, not found]")

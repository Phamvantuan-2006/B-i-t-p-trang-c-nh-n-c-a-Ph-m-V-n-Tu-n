# Định nghĩa node của danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Tạo danh sách liên kết từ list
def create_linked_list(arr):
    head = None
    tail = None

    for x in arr:
        new_node = Node(x)

        if head is None:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


# Hàm tách thành các run tăng
def split_runs(head):
    runs = []  # danh sách các run
    current = head

    while current:
        # bắt đầu 1 run mới
        run_head = current
        run_tail = current

        # duyệt đến khi còn tăng
        while run_tail.next and run_tail.next.data >= run_tail.data:
            run_tail = run_tail.next

        # cắt run ra
        next_run = run_tail.next
        run_tail.next = None

        runs.append(run_head)

        # chuyển sang run tiếp theo
        current = next_run

    return runs


# Hàm in danh sách liên kết
def print_list(head):
    cur = head
    print("[", end="")
    while cur:
        print(cur.data, end="")
        if cur.next:
            print("][", end="")
        cur = cur.next
    print("]")


# ===== Chương trình chính =====
arr = list(map(int, input("Nhap day duong: ").split()))

# Tạo linked list
head = create_linked_list(arr)

# Tách run
runs = split_runs(head)

# In kết quả
print("List 'run':")
for run in runs:
    print_list(run)

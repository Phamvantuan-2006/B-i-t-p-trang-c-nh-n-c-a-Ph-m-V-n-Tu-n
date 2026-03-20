# Hàm kiểm tra hợp lệ (không làm quá 12 giờ = 2 ca)
def hop_le(vao_h, vao_m, ra_h, ra_m):
    vao = vao_h * 60 + vao_m
    ra = ra_h * 60 + ra_m

    # Nếu qua ngày
    if ra < vao:
        ra += 24 * 60

    return (ra - vao) <= 12 * 60  # không quá 12 giờ


# Hàm tính tiền công
def tinh_tien(vao_h, vao_m, ra_h, ra_m):
    vao = vao_h * 60 + vao_m
    ra = ra_h * 60 + ra_m

    # Nếu qua ngày
    if ra < vao:
        ra += 24 * 60

    tong = 0

    # Duyệt từng phút để tính tiền
    for t in range(vao, ra):
        gio = (t // 60) % 24  # giờ hiện tại (0–23)

        # Ca ngày: 06h–18h
        if 6 <= gio < 18:
            tong += 10000 / 60
        else:
            # Ca đêm: còn lại
            tong += 15000 / 60

    return int(tong)


# ===== Chương trình chính =====
n = int(input("Nhap so cong nhan: "))

for _ in range(n):
    id_cn = input("Nhap ID cong nhan: ")

    vao_h, vao_m = map(int, input("Vao (gio phut): ").split())
    ra_h, ra_m = map(int, input("Ra (gio phut): ").split())

    # Kiểm tra hợp lệ
    if not hop_le(vao_h, vao_m, ra_h, ra_m):
        print(id_cn, "Nhap sai!")
        continue

    # Tính tiền
    tien = tinh_tien(vao_h, vao_m, ra_h, ra_m)

    # In kết quả
    print(
        id_cn,
        f"{vao_h:02d}:{vao_m:02d}",
        f"{ra_h:02d}:{ra_m:02d}",
        tien
    )

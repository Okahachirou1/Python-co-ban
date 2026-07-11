gio_hang = []
def them_mon_an(ten_mon):
    gio_hang.append(ten_mon)
    print(f"Đã thêm thành công: '{ten_mon}")
def xem_gio_hang(danh_sach):
    print("\n Giỏ Hàng của bạn")
    if len(danh_sach) == 0:
        print("Giỏ hàng trống!")
    else:
        for index, mon in enumerate(danh_sach, start=1):
            print(f"{index}. {mon}")
    print("--------------------------\n")
xem_gio_hang(gio_hang)
them_mon_an("Phở bò")
them_mon_an("Bún Chả")
them_mon_an("Cơm Tấm")
xem_gio_hang(gio_hang)
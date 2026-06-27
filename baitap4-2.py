ten_mon = input("Nhập tên món ăn bạn muốn gọi: ")
so_tien = int(input("Nhập số tiền hiện có trong ví: "))
is_vip = "VIP" in ten_mon.upper()
if is_vip and so_tien >= 500000:
    print("Order thành công món VIP")
elif (not is_vip) and so_tien >=100000:
    print("Order thành công món thường")
else:
    print("Số dư không đủ, vui lòng nạp thêm")
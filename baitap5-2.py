def dem_so_chan(danh_sach_so):
    so_luong_chan = 0
    for so in danh_sach_so:
        if so % 2 == 0:
            so_luong_chan += 1
    return so_luong_chan
danh_sach_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ket_qua_1 = dem_so_chan(danh_sach_1)
print(f"SỐ lượng số chẵn trong danh sách 1 là: {ket_qua_1}")
danh_sach_2 = [11, 23, 45, 67]
ket_qua_2 = dem_so_chan(danh_sach_2)
print(f"Số lượng số chẵn trong danh sách 2 là: {ket_qua_2}")
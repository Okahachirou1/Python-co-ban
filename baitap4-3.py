tong = 0
print("Chương trình tính tổng các số nguyên liên tiếp")
print("Nhập số 0 để dừng lại và xem kết quả. \n")
while True :
    so = int(input("Nhập một số nguyên: "))
    if so == 0:
        print("Đã nhận số 0. Đang thoát vòng lặp...")
        break
    tong += so
print("-" * 30)
print(f"Tổng của các số bạn đã nhập là: {tong}")

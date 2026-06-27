# nam =int(input("Nhap vao mot nam bat ky:"))
# if nam >=0:
#     if nam % 400 ==0:
#         print(f"Năm {nam} là năm nhuận.")
#     elif nam % 100 ==0:
#         print(f"Năm {nam} không phải là năm nhuận.")
#     elif nam % 4 ==0:
#         print(f"Năm {nam} là năm nhuận.")
#     else:
#         print(f"Năm {nam} không phải là năm nhuận.")
# else:
#     print("Vui lòng nhập năm dương lịch hợp lệ (lớn hơn 0)!")

nam =int(input("Nhap vao mot nam bat ky:"))
if nam >0:
    if (nam % 400 ==0) or (nam % 4 ==0 and nam % 100 != 0):
        print(f"Năm {nam} là năm nhuận.")
    else:
        print(f"Năm {nam} không phải là năm nhuận.")
else:
    print("Vui lòng nhập năm dương lịch hợp lệ (lớn hơn 0)!")
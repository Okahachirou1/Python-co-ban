import csv
from datetime import datetime
import os
ten = input("Nhập tên nhân viên: ")
thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
file_ton_tai = os.path.exists("diem_danh.csv")
with open("diem_danh.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if not file_ton_tai:
        writer.writerow(["Tên", "Thời Gian"])
    writer.writerow([ten, thoi_gian])
print("Điểm danh thành công!")
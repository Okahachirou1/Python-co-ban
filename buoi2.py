ten = input("Nhập tên của bạn: ")

try:
    tuoi = int(input("Nhập tuổi của bạn: "))
except ValueError:
    print("Nhập sai định dạng tuổi!")
    exit()

nghe_nghiep = input("Nhập nghề nghiệp của bạn: ")

print("\n" + "=" * 30)
print("     THÔNG TIN CÁ NHÂN")
print("=" * 30)
print(f"Họ và tên   : {ten}")
print(f"Tuổi        : {tuoi}")
print(f"Nghề nghiệp : {nghe_nghiep}")
print("=" * 30)
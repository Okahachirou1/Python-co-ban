mat_khau_dung = "admin123"
for luot in range(3):
    mat_khau_nhap = input(f"Nhập mật khẩu (Lần {luot + 1}/3): ")
    if mat_khau_nhap == mat_khau_dung:
       print("Đăng nhập thành công!")
       break
    else:
        print("Sai mật khẩu, vui lòng thử lại.")
else:
    print("Tài khoản của bạn đã bị khóa do nhập sai quá 3 lần")
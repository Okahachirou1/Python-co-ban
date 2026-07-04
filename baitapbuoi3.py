password = input("Nhập mật khẩu của bạn: ")
if len(password) >8:
    if "123" in password:
        print("Mật khẩu không được chứa chuỗi '123' ")
    else:
        print("Mật khẩu an toàn")
else:
    print("Mật khẩu yếu")
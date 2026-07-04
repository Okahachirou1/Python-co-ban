password = input("Nhập mật khẩu của bạn: ")
do_dai = len(password)
if do_dai < 5:
    print("Mật khẩu quá yếu! Nguy cơ bị hack rất cao")
elif do_dai <=8:
    print("Mật khẩu ở mức trung bình. Bạn nên đặt dài hơn.")
else:
    print("Mật khẩu an toàn!")
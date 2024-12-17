import bcrypt

# Hash mật khẩu
password = "user_password"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

# Kiểm tra mật khẩu
input_password = "user_password"
if bcrypt.checkpw(input_password.encode('utf-8'), hashed):
    print("Password đúng")
else:
    print("Password sai")

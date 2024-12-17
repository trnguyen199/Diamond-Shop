from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'Sixteen byte key'  # Khóa bí mật (16 byte)
cipher = AES.new(key, AES.MODE_CBC)

# Mã hóa
data = "Địa chỉ: 123 ABC".encode('utf-8')
encrypted = cipher.encrypt(pad(data, AES.block_size))

# Giải mã
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(encrypted), AES.block_size)
print(decrypted.decode('utf-8'))

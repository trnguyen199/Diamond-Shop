import mysql.connector

try:
    # Kết nối đến MySQL và chỉ định database 'qlkc'
    db = mysql.connector.connect(
        user='root',
        password='Thang2209*',
        host='localhost',
        database='qlkc'  # Đúng tham số
    )

    
    mycursor = db.cursor()

   
    code = "SHOW TABLES;"  # Hoặc một câu lệnh khác bạn muốn chạy
    mycursor.execute(code)

    # Lấy kết quả và in ra
    print("Các bảng trong cơ sở dữ liệu 'qlkc':")
    for table in mycursor:
        print(table)

except mysql.connector.Error as e:
    print(f"Lỗi khi kết nối hoặc truy vấn MySQL: {e}")

finally:
    if db.is_connected():
        mycursor.close()
        db.close()
        print("Đã đóng kết nối đến MySQL.")

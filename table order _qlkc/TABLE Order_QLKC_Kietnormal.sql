-- Tạo cơ sở dữ liệu
CREATE DATABASE QLKC;
USE QLKC;


-- Tạo bảng orders
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Mã đơn hàng (tự tăng)
    user_id INT NOT NULL,                      -- Mã người dùng
    product_id INT NOT NULL,                   -- Mã sản phẩm
    quantity INT NOT NULL,                     -- Số lượng sản phẩm
    total_price DECIMAL(10, 2) NOT NULL       -- Tổng giá trị đơn hàng
);

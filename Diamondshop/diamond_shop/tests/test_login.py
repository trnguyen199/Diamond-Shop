import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Đường dẫn đến chromedriver.exe
PATH = r"D:\python\Diamondshop\diamond_shop\chromedriver.exe"

@pytest.fixture(scope="function")
def driver():
    """Khởi tạo WebDriver, mở fullscreen"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Mở trình duyệt tối đa màn hình

    service = Service(PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.execute_script("window.focus();")  # Đưa trình duyệt lên foreground

    yield driver
    driver.quit()  # Đóng trình duyệt sau khi test

def slow_type(element, text, delay=0.2):
    """Nhập từng ký tự một vào ô input với độ trễ"""
    element.clear()  # Xóa nội dung cũ trước khi nhập
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # Tạo hiệu ứng gõ phím chậm

def login(driver):
    """Hàm đăng nhập dùng lại"""
    driver.get("http://127.0.0.1:8000/accounts/login/")
    driver.implicitly_wait(3)

    username = driver.find_element(By.ID, "id_login")
    slow_type(username, "admin")

    password = driver.find_element(By.ID, "id_password")
    slow_type(password, "123")

    login_button = driver.find_element(By.XPATH, '//form/input[@type="submit"]')
    login_button.click()

    # Chờ chuyển trang
    time.sleep(2)

def test_add_product_and_update_profile(driver):
    """Test thêm sản phẩm vào giỏ hàng, cập nhật profile và đăng xuất"""
    login(driver)  # Đăng nhập trước
    time.sleep(2)

    # Nhấn vào menu "Sản phẩm"
    product_menu = driver.find_element(By.XPATH, '//a[@href="/product/" and contains(@class, "nav-top-link")]')
    product_menu.click()
    time.sleep(2)

    # Nhấn vào nút "Thêm vào giỏ" (sản phẩm có ID 13)
    add_to_cart = driver.find_element(By.XPATH, '//button[@data-product="13" and @data-action="add"]')
    add_to_cart.click()
    time.sleep(3)

    # Nhấn vào biểu tượng giỏ hàng
    cart_button = driver.find_element(By.XPATH, '//a[@id="cart-btn"]')
    cart_button.click()
    time.sleep(2)

    # Kiểm tra xem có ở trang giỏ hàng không
    assert "/cart/" in driver.current_url

    # Nhấn vào nút "Thanh toán"
    checkout_button = driver.find_element(By.XPATH, '//a[contains(@class, "btn-cart") and contains(@class, "btn-success")]')
    checkout_button.click()
    time.sleep(2)

    # Nhấn vào Profile
    profile_button = driver.find_element(By.XPATH, '//a[@href="/getProfile/" and contains(@class, "btn")]')
    profile_button.click()
    time.sleep(2)

    # Nhập Họ Tên
    fullname_input = driver.find_element(By.ID, "fullname")
    slow_type(fullname_input, "Nguyễn Trung Nguyên")
    time.sleep(2)

    # Nhập Số Điện Thoại
    phone_input = driver.find_element(By.ID, "phone")
    slow_type(phone_input, "0909123456")
    time.sleep(2)

    # Nhập Địa Chỉ
    address_input = driver.find_element(By.ID, "address")
    slow_type(address_input, "Nguyễn Gia Trí")
    time.sleep(2)

    # Nhấn vào nút "Lưu thông tin"
    save_button = driver.find_element(By.XPATH, '//input[@type="submit" and contains(@class, "form__button")]')
    save_button.click()
    time.sleep(2)  # Chờ sau khi lưu

    # Nhấn vào nút "Đăng xuất"
    logout_button = driver.find_element(By.XPATH, '//a[contains(@href, "/accounts/logout/") and contains(@class, "btn")]')
    logout_button.click()
    time.sleep(2)

    # Tắt trình duyệt
    driver.quit()

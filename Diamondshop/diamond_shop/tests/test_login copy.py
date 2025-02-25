import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Đường dẫn đến chromedriver.exe
PATH = r"D:\python\Diamondshop\diamond_shop\chromedriver.exe"

@pytest.fixture(scope="function")
def driver():
    """Khởi tạo WebDriver"""
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    yield driver  # Không đóng trình duyệt tự động
    # driver.quit()  # Nếu muốn đóng trình duyệt sau khi test, bật dòng này lên

def slow_type(element, text, delay=0.2):
    """Nhập từng ký tự một vào ô input với độ trễ"""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)  # Tạo hiệu ứng gõ phím chậm

def test_login(driver):
    """Test đăng nhập với hiệu ứng nhập từng ký tự"""
    driver.get("http://127.0.0.1:8000/accounts/login/")
    driver.implicitly_wait(3)

    # Kiểm tra phần tử có tồn tại không
    assert driver.find_element(By.ID, "id_login")
    assert driver.find_element(By.ID, "id_password")

    # Gõ từng ký tự vào ô username
    username = driver.find_element(By.ID, "id_login")
    slow_type(username, "admin")

    # Gõ từng ký tự vào ô password
    password = driver.find_element(By.ID, "id_password")
    slow_type(password, "123")

    # Click vào nút login
    login = driver.find_element(By.XPATH, '//form/input[2]')
    login.click()

def test_add_product(driver):
    
    driver.get("http://127.0.0.1:8000/accounts/login/")
    driver.implicitly_wait(3)

    # Kiểm tra phần tử có tồn tại không
    assert driver.find_element(By.ID, "menu-item")

    # Click vào nút login
    login = driver.find_element(By.XPATH, '//form/input[2]')
    login.click()
    # # Kiểm tra đăng nhập thành công
    # assert "dashboard" in driver.current_url

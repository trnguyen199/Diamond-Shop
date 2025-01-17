document.addEventListener("DOMContentLoaded", function () {
  // Lưu/cập nhật thông tin cá nhân
  const personalInfoForm = document.getElementById("personalInfoForm");
  personalInfoForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const fullName = document.getElementById("fullName").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const address = document.getElementById("address").value.trim();

    if (!fullName || !email || !phone || !address) {
      alert("Vui lòng điền đầy đủ thông tin cá nhân.");
      return;
    }
    alert("Thông tin cá nhân đã được lưu!");
  });

  // Cập nhật mật khẩu
  const passwordForm = document.getElementById("passwordForm");
  passwordForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const currentPassword = document.getElementById("currentPassword").value.trim();
    const newPassword = document.getElementById("newPassword").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();

    if (!currentPassword || !newPassword || !confirmPassword) {
      alert("Vui lòng điền đầy đủ các trường mật khẩu.");
      return;
    }
    if (newPassword !== confirmPassword) {
      alert("Mật khẩu mới và xác nhận mật khẩu không trùng khớp.");
      return;
    }
    alert("Mật khẩu đã được cập nhật!");
  });

  // xem chi tiết đơn hàng
  const orderDetailBtns = document.querySelectorAll(".order-detail-btn");
  orderDetailBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const orderId = this.dataset.orderId;
      alert("Xem chi tiết đơn hàng #" + orderId);
    });
  });

  // Sản phẩm yêu thích
  // Thêm vào giỏ hàng
  const addToCartBtns = document.querySelectorAll(".add-to-cart-btn");
  addToCartBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      alert("Sản phẩm đã được thêm vào giỏ hàng!");
    });
  });

  // Xóa khỏi danh sách yêu thích
  const removeFavBtns = document.querySelectorAll(".remove-fav-btn");
  removeFavBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const favItem = this.closest(".favorite__item");
      if (favItem) {
        favItem.remove();
      }
      alert("Đã xóa sản phẩm khỏi danh sách yêu thích!");
    });
  });

  // Quản lý địa chỉ giao hàng
  // Sửa địa chỉ
  const editAddressBtns = document.querySelectorAll(".edit-address-btn");

  editAddressBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      // Lấy địa chỉ (personalAddress) từ phần Thông Tin Cá Nhân
      const personalAddress = document
        .getElementById("address")
        .value
        .trim();
      // Cập nhật địa chỉ
      const addressItem = this.closest(".address__item");
      const addressDetails = addressItem.querySelector(".address__details");

      // Ghi đè địa chỉ của address__details = personalAddress
      if (addressDetails) {
        addressDetails.textContent = personalAddress;
      }


      alert("Địa chỉ giao hàng đã được cập nhật theo thông tin cá nhân!");
    });
  });

  // Xóa địa chỉ
  const deleteAddressBtns = document.querySelectorAll(".delete-address-btn");
  deleteAddressBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const addressItem = this.closest(".address__item");
      if (addressItem) {
        addressItem.remove();
      }
      alert("Địa chỉ đã được xóa!");
    });
  });
});
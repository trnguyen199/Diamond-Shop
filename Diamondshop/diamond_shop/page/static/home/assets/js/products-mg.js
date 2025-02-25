
document.addEventListener("DOMContentLoaded", function () {
    const filterLinks = document.querySelectorAll(".filter-category");
    const products = document.querySelectorAll(".product-card");

    // Lấy category từ URL
    const urlParams = new URLSearchParams(window.location.search);
    let categoryId = urlParams.get("category") || "0"; 

    filterLinks.forEach(link => {
        if (link.getAttribute("data-category-id") === categoryId) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });

    // Lọc sản phẩm theo categoryId từ URL
    products.forEach(product => {
        if (product.getAttribute("data-category-id") === categoryId || categoryId === "0") {
            product.style.display = "block";
        } else {
            product.style.display = "none";
        }
    });

    // Lấy tất cả các product-card và phần tử chứa sản phẩm
    const productCards = document.querySelectorAll('.product-card');
    const listProductDiv = document.getElementById('product-list');
    
    
    productCards.forEach(card => {
        card.addEventListener('click', function (e) {
            if (e.target.closest("button")) {
                return; // Không cho phép click tiếp tục xử lý
            }
            listProductDiv.style.display = 'block';

            const productId = card.dataset.id
            fetch(`/get-product-detail/?id=${productId}`)
                .then(response => response.text())
                .then(html => {
                    listProductDiv.innerHTML = html;
                })
                .catch(err => console.error('Error loading product detail:', err));
        });
    });

});



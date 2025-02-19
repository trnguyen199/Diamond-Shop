function buyNow() {
    fetch('/api/buy', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product: 'Bông Tai Ngọc Trai và Đá Quý Giọt Lệ Sang Trọng', price: 625000000 })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function addToCart() {
    fetch('/api/cart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product: 'Bông Tai Ngọc Trai và Đá Quý Giọt Lệ Sang Trọng', price: 625000000 })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}
// var updateBtns = document.getElementsByClassName('update-cart')

// document.addEventListener('click', function (event) {
//     if (event.target.classList.contains('update-cart')) {
//         var productId = event.target.dataset.product;
//         var action = event.target.dataset.action;
//         console.log('Product ID:', productId, 'Action:', action);
//         console.log('USER', user)

//         if(user === 'AnonymousUser'){
//             console.log('User is not authenticated')
//         } else {
//             updateUserOrder(productId, action)
//         }
//     }

//     });

// function updateUserOrder(productId, action){
//     console.log('User is authenticated, sending data...')

//         var url = '/update_item/'

//         fetch(url, {
//             method:'POST',
//             headers:{
//                 'Content-Type':'application/json',
//                 'X-CSRFToken': csrftoken,
//             }, 
//             body:JSON.stringify({'productId':productId, 'action':action})
//         })
//         .then((response) => {
//             return response.json();
//         })
//         .then((data) => {
//             console.log('data', data)
//             //location.reload()
//         });
// }
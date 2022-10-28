document.addEventListener('DOMContentLoaded', () => {
        updateCart()
    }
)


let products = document.querySelectorAll('.add-to-cart-btn');

products.forEach((item) => {

        item.addEventListener('click', (event) => {
                let productId = event.target.dataset.id

                fetch(`http://127.0.0.1:8000/api/v1/cart/create/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json;charset=utf-8'
                        },
                        body: JSON.stringify(
                            {
                                product: productId,
                            }
                        )
                    }
                ).then(r => updateCart())
            }
        )
    }
)


function updateCart() {
    fetch(`http://127.0.0.1:8000/api/v1/cart/`)
        .then(resp => resp.json())
        .then(async (data) => {
                let cart = document.getElementById("cart")
                let mainPriceEl = document.getElementById('mainPrice')
                let qty = document.getElementById('qty')

                cart.innerHTML = ``

                let count = 0
                let mainPrice = 0

                let html = ``

                for (const item of data) {
                    let response = await fetch(`http://127.0.0.1:8000/api/v1/product/${item.product}`);
                    if (response.ok) {
                        let responseData = await response.json();
                        html += `
                                    <div class="product-widget">
                                        <div class="product-img">
                                            <img src="./static/img/${responseData.path_img}" alt="">
                                        </div>
                                        <div class="product-body">
                                            <h3 class="product-name"><a href="#">${responseData.name}</a></h3>
                                            <h4 class="product-price"><span class="qty">1x</span>${responseData.price}</h4>
                                        </div>
                                        <button onclick="deleteItemCart(${responseData.id})" class="delete"><i class="fa fa-close"></i></button>
                                    </div>
                                    `
                        count += 1
                        mainPrice += responseData.price
                        qty.innerHTML = String(count)
                        mainPriceEl.innerHTML = `SUBTOTAL: $${mainPrice}.00`
                        cart.innerHTML = html
                    } else {
                        alert("Ошибка HTTP: " + response.status);
                    }
                }
            }
        )
}

function deleteItemCart(id) {
    fetch(`http://127.0.0.1:8000/api/v1/cart/${id}`, {
            method: 'DELETE',
        }
    )
        .then(r => console.log(r.json()))
        .then(res => updateCart())
}
const cart = document.getElementById("cart")
const mainPriceEl = document.getElementById('mainPrice')
const qty = document.getElementById('qty')

document.addEventListener('DOMContentLoaded', () => {
        if (window.localStorage.getItem('token')) {
            updateCart()
        } else {
            cart.innerHTML = "<h4>Необходимо авторизоваться</h4>"
            mainPriceEl.innerHTML = ""
            qty.innerHTML = '0'
        }
    }
)


let products = document.querySelectorAll('.add-to-cart-btn');

products.forEach((item) => {

        item.addEventListener('click', (event) => {
                let productId = event.target.dataset.id

                fetch(`http://127.0.0.1:8000/api/v1/cart/create/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json;charset=utf-8',
                            'Authorization': `Token ${window.localStorage.getItem('token')}`
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
    fetch(
        `http://127.0.0.1:8000/api/v1/cart/`,
        {
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Authorization': `Token ${window.localStorage.getItem('token')}`
            },
        }
    )
        .then(resp => resp.json())
        .then(async (data) => {

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
                                            <img src="${responseData.path_img}" alt="">
                                        </div>
                                        <div class="product-body">
                                            <h3 class="product-name"><a href="#">${responseData.name}</a></h3>
                                            <h4 class="product-price"><span class="qty">1x</span>${responseData.price}</h4>
                                        </div>
                                        <button onclick="deleteItemCart(${item.id})" class="delete"><i class="fa fa-close"></i></button>
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
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Authorization': `Token ${window.localStorage.getItem('token')}`
            },
        }
    )
        .then(r => console.log(r.json()))
        .then(res => updateCart())
}

async function authorization(event) {
    event.preventDefault()
    const formData = new FormData(event.target)

    const data = await fetch(
        `http://127.0.0.1:8000/token/`,
        {
            method: "POST",
            body: formData
        }
    )

    const token = await data.json()
    window.localStorage.setItem("token", token.token)
    updateCart()
}
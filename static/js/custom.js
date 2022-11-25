const cart = document.getElementById("cart")
const mainPriceEl = document.getElementById('mainPrice')
const qty = document.getElementById('qty')
const products_slick = document.getElementById('products_slick')

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

async function selectCategory(id) {
    const data = await fetch(`http://127.0.0.1:8000/api/v1/product/${id}/categories`)
    const productsByCategory = await data.json()
    let html = ``
    for (const item of productsByCategory) {
        html += `
        <div class="product">
            <div class="product-img">
                <img src="${item.path_img}" alt="">
            </div>
            <div class="product-body">
                <p class="product-category">Category</p>
                <h3 class="product-name"><a href="#">${item.name}</a></h3>
                <h4 class="product-price">${item.price}
                    <del class="product-old-price">${item.old_price}</del>
                </h4>
                <div class="product-rating">
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                </div>
                <div class="product-btns">
                    <button class="add-to-wishlist"><i class="fa fa-heart-o"></i><span
                            class="tooltipp">add to wishlist</span></button>
                    <button class="add-to-compare"><i class="fa fa-exchange"></i><span
                            class="tooltipp">add to compare</span></button>
                    <button class="quick-view"><i class="fa fa-eye"></i><span class="tooltipp">quick view</span>
                    </button>
                </div>
            </div>
            <div class="add-to-cart">
                <button class="add-to-cart-btn" data-id={{ item.id }}><i class="fa fa-shopping-cart"></i>
                    add to cart
                </button>
            </div>
        </div>
        `
    }
    products_slick.innerHTML = html

    let $this = $(products_slick),
        $nav = $this.attr('data-nav');

    $this.slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        infinite: true,
        speed: 300,
        dots: false,
        arrows: true,
        appendArrows: $nav ? $nav : false,
        responsive: [{
            breakpoint: 991,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
            }
        },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                }
            },
        ]
    });
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


async function orderFunction(event) {
    event.preventDefault()
    const formData = new FormData(event.target)
    const data = formData.getAll('carts')
    for(let i = 0; i < data.length; i++) {
        fetch(
        `http://127.0.0.1:8000/api/v1/checkout/create/`, {
            method: "POST",
            body: JSON.stringify({
                carts: data[i]
            }),
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'Authorization': `Token ${window.localStorage.getItem('token')}`
            },
        }
    ).then(r => console.log(r.json()))
    }
}
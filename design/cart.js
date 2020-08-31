let carts = document.querySelectorAll('.add-cart');

let products = [{

        name: "Python",
        product_id: 'P101',
        description: "Highlevel Language",
        price: 1200,
        incart: 0
    }, {

        name: "JavaScript",
        product_id: 'P102',
        description: "Full stack ",
        price: 1600,
        incart: 0
    },
    {

        name: "Java",
        product_id: 'P103',
        description: "HighLevel",
        price: 2000,
        incart: 0
    }
]

let products = localStorage.getItem('products');
// console.log(product)

for (let i = 0; i < carts.length; i++) {
    console.log('my loop');
    carts[i].addEventListener('click', () => {
        console.log('added to cart')
        cartNumbers(products[i]);
        totalcost(products[i]);
    })
}

function onLoadCartNumbers() {
    let productNumbers = localStorage.getItem('cartNumbers');
    if (productNumbers) {
        document.querySelector('.cart span').textContent = productNumbers;
    }

}


function cartNumbers(product) {
    console.log("The product clicked is", product)
    let productNumbers = localStorage.getItem('cartNumbers');

    // console.log(productNumbers);

    // console.log(typeof productNumbers);
    productNumbers = parseInt(productNumbers);
    if (productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers + 1);
        document.querySelector('.cart span').textContent = productNumbers + 1;
    } else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.cart span').textContent = 1;
    }
    setItems(product);

}


function setItems(product) {
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);

    if (cartItems != null) {
        if (cartItems[product.name] == undefined) {
            cartItems = {
                ...cartItems,
                [product.name]: product
            }

        }
        cartItems[product.name].incart += 1

    } else {
        cartItems = {
            [product.name]: product
        }
        product.incart = 1;

    }

    localStorage.setItem('productsInCart', JSON.stringify(cartItems));
}

function totalcost(product) {
    console.log("The Product Price", product.price)
    let cartCost = localStorage.getItem("totalcost");
    console.log("The Product Price", cartCost)

    console.log("The cart Product Price", cartCost);
    console.log(typeof cartCost);
    if (cartCost != null) {
        cartCost = parseInt(cartCost);
        localStorage.setItem("totalcost", cartCost + product.price);

    } else {
        localStorage.setItem("totalcost", product.price);

    }
}

function displayCart() {
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    console.log(cartItems);
    let productContainer = document.querySelector(".products");
    let cartCost = localStorage.getItem("totalcost");
    if (cartItems && productContainer) {
        productContainer.innerHTML = '';
        Object.values(cartItems).map(item => {
            productContainer.innerHTML += `
            <div class="product">
                <i class="fa fa-times-circle" onclick="deleteProduct(\"${item.product_id}\")" aria-hidden="true"></i>
                <img src="./images/${item.name}.svg" width="100px" height="100px">
                <span>${item.name}</span> 
            </div>
            <div class="price">${item.price}</div>
            <div class="quantity">
                <i class="fa fa-plus-circle" onclick="update(\"${item.product_id}\")" aria-hidden="true">
                <input type="hidden" value="" id="quantity">
                </i>
                <span>${item.incart}</span>
                <i class="fa fa-minus-circle" onclick="update(\"${item.product_id}\")" aria-hidden="true">
                <input type="hidden" value="" id="quantity">
                </i>
            </div>
            <div class="price">Rs.${item.incart * item.price}</div>
            `
        });
        productContainer.innerHTML += `
           <div class="basket">
              <h4 class="basket-title">
              Basket Total
              </h4>
              <h4 class="basketTotal">
              Rs.${cartCost}
            </h4>
        
           </div>
         
         `
    }
}

onLoadCartNumbers();
displayCart();


/** update and delete** */


function update(productid) {
    var quantity = document.getElementById("quantity");
    let userid = localStorage.getItem(user.userid)
    let product_id = localStorage.getItem(product.product_id);
    console.log(userid);
    postData(`'http://127.0.0.1:5000/cart/${userid}'`, {
            product_id: productid,
            quantity: quantity
        })
        .then(data => {
            console.log(data);
            alert(data['message'])

            //loggeduser(data);
        })
}

function deleteProduct(productid) {
    let userid = localStorage.getItem(user.userid)
    console.log(userid);
    postData(`'http://127.0.0.1:5000/cart/${userid}'`, {
            product_id: productid,
        })
        .then(data => {
            console.log(data);
            alert(data['message'])

            //loggeduser(data);
        })
}



async function updateData(url = '', data = {}) {
    console.log("hello");
    const response = await fetch(url, {
        method: 'PUT',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}


async function deleteData(url = '', data = {}) {
    console.log("hello");
    const response = await fetch(url, {
        method: 'DELETE',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}
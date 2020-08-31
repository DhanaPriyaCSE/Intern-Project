let carts = document.querySelectorAll('.add-cart');


let products = [{
        name: "Book",
        description: "books",
        price: 1200,
        incart: 0
    }, {

        name: "Python",
        description: "book",
        price: 1800,
        incart: 0
    },
    {

        name: "Java",
        description: "books",
        price: 1600,
        incart: 0
    }
]

let product = localStorage.getItem('products');
console.log(product)

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
                <i class="fa fa-times-circle" aria-hidden="true"></i>
                <img src="./images/${item.name}.svg" width="100px" height="100px">
                <span>${item.name}</span>
            </div>
            <div class="price">${item.price}</div>
            <div class="quantity">
                <i class="fa fa-plus-circle" aria-hidden="true"></i>
                <span>${item.incart}</span>
                <i class="fa fa-minus-circle" aria-hidden="true"></i>
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
const urlParams = new URLSearchParams(window.location.search);
const categoryid = urlParams.get('category_id')
console.log(categoryid);
var userid = localStorage.getItem('user');
console.log(userid);

fetch(`http://127.0.0.1:5000/categories/${categoryid}/products`)
    .then(response => {
        return response.json();
    }).then(data => {
        console.log(data);

        const html = data.map(product => {
            return ` 
                <div class="container">
                    <div class="image">
                        <img src="images/Book.svg" width="150px" height="150px" alt="">
                        <p id="${product.id}"  class="fa fa-cart-plus add-cart cart1"> Name: ${product.name}</p>
                        <p >Price: ${product.price}</p>
                         <i class="fa fa-cart-plus add-cart cart1" aria-hidden="true"></i><a href="#" onclick='product(\"${product.id}\")' >Add Cart</a>
                        
                      <button class="btn"><i class="fa fa-cart-plus add-cart cart1" onclick='product(\"${product.id}\")'></i> Add to cart</button>
                        <input type="hidden" value="15">
                        
                        </div>
                    </div>
                        `
        }).join("");
        // console.log(html);
        document.querySelector('#cat-product').insertAdjacentHTML('afterend', html);
    }).catch(error => {
        console.log(error);
    });

// let product = localStorage.getItem('products');
// console.log(product)


function product(product_id) {
    var productid = product_id
    console.log(productid)
    fetch(`http://127.0.0.1:5000/product/${productid}`)
        .then(response => {
            return response.json();
        }).then(data => {
            console.log(data);
            addProductToart(productid, userid)
        }).catch(error => {
            console.log(error);
        });
}


async function postData(url = '', data = {}) {
    console.log("hello");
    const response = await fetch(url, {
        method: 'POST',
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

function addProductToart(productid, userid) {
    let user = userid
    postData(`http://127.0.0.1:5000/cart/${user}`, {
            product_id: productid,
            quantity: 1
        })
        .then(data => {
            console.log(data);
            if (data['status'] == 200) {
                alert(data['message'])
                window.location.href = `"http://127.0.0.1:5500/design/cartpage.html?product_id=${productid}"`
            }
            //loggeduser(data);
        })
}
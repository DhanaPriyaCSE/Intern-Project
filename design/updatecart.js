const urlParams = new URLSearchParams(window.location.search);

fetch(`http://127.0.0.1:5000/cart/${user_id}`).then(
    function(response) { return response.json(); }
).then(
    function(data) {
        cartUpdateAndDelete(data);

    }
)

function cartUpdateAndDelete(data) {
    console.log(data)
    document.getElementById("cart").innerHTML = `
    ${data.map(function(data) {
    return `
    <div class="category">
    <img src="${data.name}">
        <h2>Name: ${data.name}</h2>
        <h2> Price: Rs.${data.price}</h2>
        <h2> Quantity - ${data.quantity}</h2>
        <button onclick="del(${data.product_id})" type="submit" class="btn btn-outline-danger">Delete</button>
        <div class="box">
            <input id='quantity' type='number' min='1'>
            <button onclick="update(${data.product_id})" type="submit" class="btn btn-outline-primary">Update quantity</button>
        </div>
        <br>
        <hr>       
    </div>
    
`
} ).join('')}
`    
}
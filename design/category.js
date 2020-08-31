fetch("http://127.0.0.1:5000/categories")
    .then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
        const html = data.map(category => {
            console.log(category.id);
            localStorage.setItem('categories', JSON.stringify(data));
            return ` 
                <div class="category">
                <p> <img src="images/book.svg" alt="Category Image" width="100px" height="100px"> </p>
                </br><hr>
                <p id="${category.id} " onclick='showcategory(${category.id})'> Name: ${category.name}</p>
                <p >Description: ${category.description}</p>
                </div>
                `

        }).join("");
        console.log(html);
        //document.querySelector('#app').insertAdjacentHTML('afterbegin', html);

        document.getElementById('#app').insertAdjacentHTML('afterend', html);
    }).catch(error => {
        console.log(error);
    });



function showcategory(categoryid) {
    console.log(categoryid);
    window.location.href = `
    poduct.html?category_id=${categoryid}`
}
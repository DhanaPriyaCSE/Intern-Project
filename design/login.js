const myForm = document.getElementById('myForm');

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

myForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var name = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    console.log("hello");
    postData('http://127.0.0.1:5000/login', {
            user_name: name,
            password: password
        })
        .then(data => {
            console.log(data, name);
            let userdata = data['user_id'];
            let userdetails = localStorage.setItem('user', data['user_id'])
            console.log(userdata, userdetails)
            if (data['status'] == 200) {
                alert("you are sucessfully logged in")
                window.location.href = "http://127.0.0.1:5500/design/homepage.html";
            } else {
                alert("you are not logged in! ")
                window.location.href = "http://127.0.0.1:5500/design/login.html";
            }
        })

});
function logout() {
    window.localStorage.removeItem('user');
    alert("You are Logged out")
    window.location.href = "homepage.html";
}
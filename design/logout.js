function logout() {
    window.localStorage.removeItem('user');
    alert("You are Logged out")
    window.location.href = "login.html";
}
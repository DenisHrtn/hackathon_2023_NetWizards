let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.querySelector('#logout-btn')
let accountBtn = document.getElementById('my-account')
let registerBtn = document.getElementById('signup-button-1')

loginBtn.addEventListener('click', () => {
    window.location.href = 'http://127.0.0.1:8000/login/';
});

logoutBtn.onclick = function () {
    window.location.href = 'http://127.0.0.1:8000/logout/';
}

registerBtn.addEventListener('click', () => {
    window.location.href = 'http://127.0.0.1:8000/registration/';
});
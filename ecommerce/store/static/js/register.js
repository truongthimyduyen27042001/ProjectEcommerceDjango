var btnRegister = document.getElementById("btn-register");
var usernameElm = document.getElementById("form_username");
var emailElm = document.getElementById("form_email");
var passwordElm = document.getElementById("form_password");
var passwordElm2 = document.getElementById("form_password2");

btnRegister.addEventListener("click", function () {
  var username = usernameElm.value;
  var email = emailElm.value;
  var password = passwordElm.value;
  var password2 = passwordElm2.value;
  if (password !== password2) {
    alert("Mat khau khong trung khop");
  } else {
    registerUser(username, email, password);
  }
});

function registerUser(username,email,password) {
    console.log('User is register, sending data...')
    var url = '/create_user/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'username': username, 'email': email, 'password': password})
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
}

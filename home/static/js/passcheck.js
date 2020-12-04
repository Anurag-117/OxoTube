function checkPasswordMatch() {
    var password = $("#password1").val();
    var confirmPassword = $("#password2").val();

    if (password !== confirmPassword)
        $("#divCheckPasswordMatch").html('<div class="alert alert-danger" role="alert" >Passwords do not match</div>');
    else
        $("#divCheckPasswordMatch").html('<div class="alert alert-success" role="alert" >Password Matched Successfully!!!</div>');
}

$(document).ready(function () {
   $("#password1, #password2").keyup(checkPasswordMatch);
});
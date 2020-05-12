function myFunction() {
    document.getElementById("checkOne1").disabled = true;
    document.getElementById("quantity1").disabled = true;
    document.getElementById("checkOne2").disabled = true;
    document.getElementById("quantity2").disabled = true;
    document.getElementById("checkOne3").disabled = true;
    document.getElementById("quantity3").disabled = true;
    document.getElementById("checkOne4").disabled = true;
    document.getElementById("quantity4").disabled = true;
    document.getElementById("checkOne5").disabled = true;
    document.getElementById("quantity5").disabled = true;
    document.getElementById("checkOne6").disabled = true;
    document.getElementById("quantity6").disabled = true;
}

function showText(text) {
    document.getElementById("text").innerHTML = text;
}
function hide() {
    document.getElementById("text").innerHTML = "";
}

function scrollToElement() {
    document.querySelector('#f2').scrollIntoView({
        behavior: 'smooth'
    });
}

function scrollToElement1() {
    document.querySelector('#f1').scrollIntoView({
        behavior: 'smooth'
    });
}

function scrollToElement3() {
    document.querySelector('#f3').scrollIntoView({
        behavior: 'smooth'
    });
}

function myFunc() {
    document.getElementById("fname").disabled = true;
    document.getElementById("lname").disabled = true;
    document.getElementById("street").disabled = true;
    document.getElementById("numberStr").disabled = true;
    document.getElementById("city").disabled = true;
    document.getElementById("zipcode").disabled = true;
    document.getElementById("email").disabled = true;
    document.getElementById("country").disabled = true;
    document.getElementById("verify").disabled = true;
}

function call() {
    window.alert("Your order has been successfully completed");
    window.location = './firstPage.html';
}


function lettersOnly(input) {
    var regex = /[^a-z]/gi;
    input.value = input.value.replace(regex, "");
}

function NumbersOnly(input) {
    var regex = /[^0-9]/gi;
    input.value = input.value.replace(regex, "");
}
//!check Alex for zip code thelei 5 arithmous (akrivos)
function NumbersRangeOnly(input) {
    var regex = /[^0-9]{5}/gi;
    input.value = input.value.replace(regex, "");
}
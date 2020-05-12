
function only_letters(input) {
    var regex = /[^a-z]/gi;
    input.value = input.value.replace(regex, "");

}

function only_numbers(input) {
    var regex = /[^0-9]/gi;
    input.value = input.value.replace(regex, "");
}

function go_to_element() {
    document.querySelector('#f2').scrollIntoView({
        behavior: 'smooth'
    });
}

function go_to_element1() {
    document.querySelector('#f1').scrollIntoView({
        behavior: 'smooth'
    });
}

function go_to_elementLast() {
    document.querySelector('#fLast').scrollIntoView({
        behavior: 'smooth'
    });
}

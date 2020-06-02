
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


function checkInput(ob) {
       var invalidChars = /[^0-9]/gi
       if(invalidChars.test(ob.value)) 
       {
           ob.value = ob.value.replace(invalidChars,"");
       }
}

    
 function getRandom(arr, n) {
     var result = new Array(n),
         len = arr.length,
         taken = new Array(len);
     if (n > len)
         throw new RangeError("getRandom: more elements taken than available");
     while (n--) {
         var x = Math.floor(Math.random() * len);
         result[n] = arr[x in taken ? taken[x] : x];
         taken[x] = --len in taken ? taken[len] : len;
     }
     return result;
 }

    

function check() {
       if (document.getElementById("checkCourrierOpt").checked==true) {
              courrierExp1();
       }

       if (document.getElementById("checkCourrierOpt").checked==false) {
              courrierExp2();
       } 
}

 function courrierExp1() {
     var inputSubtotal =  document.getElementById("SubTotal");
     var x = parseInt(inputSubtotal.value);
     var result;
     if (x > 0) {
         result = x + 4;
         x = result;
     } 
     if (x > 30) {
         result = x - 6
     }
     var inputSubtotal = document.getElementById("SubTotal");
     inputSubtotal.value = result;   
 }

 function courrierExp2() {
     var inputSubtotal =  document.getElementById("SubTotal");
     var x = parseInt(inputSubtotal.value);
     if (x > 30) {
         result = x + 2
     } 
     if (x <= 30) {
         var result = x - 4;
     }
     var inputSubtotal = document.getElementById("SubTotal");
     x = result;
     inputSubtotal.value = result;   
 }



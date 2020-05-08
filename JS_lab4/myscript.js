function func1() {
    //query 1
    var var1 = document.forms["form1"]["fname"].value;
    var var2 = document.forms["form1"]["lname"].value;
    var var3 = document.forms["form1"]["address"].value;
    var var4 = document.forms["form1"]["addr"].value;
    var var5 = document.forms["form1"]["web"].value;
    var var6 = document.forms["form1"]["email"].value;

    //if condition
    if (var1 == "" && var2 == "" && var3 == "" && var4 == "" && var5 == "" && var6 == "") {
        window.alert("Please add field type input your form on screen");
    }

    //query 2
    var var7 = document.forms["form1"]["country"].value;
    console.log("var7 =>", var7);
    if (!(var7 === "Greece" || var7 === "Italy" || var7 ===  "Spain")) {
        var arr = ["Greece", "Italy", "Spain"];
        var randomItem = arr[Math.floor(Math.random() * arr.length)];
        var7 = randomItem;
        //  Your line below Nikos is wrong  
        // document.getElementById("country").innerHTML = var7; 
        
        // The below is correct
        document.getElementById("country").value = var7;
    }

    //query3
    var var8 = document.getElementById("tel").value;

    if (var8.length != 10) {
        var line = document.createElement("p");
        var t = document.createTextNode("alert the length of telephone is different from 10 numbers");
        document.body.appendChild(line);
        line.appendChild(t);

    }
}

function func2() {
    //query4
    // Nikos you 3 lines of code are not correct 
    // var var11 = document.getElementById("text");
    // var var12 = document.getElementById("color");
    // var11.style.body.backgroundColor = var12.value;
    
    let colorInput = document.querySelector('#color');
    colorInput.addEventListener('input', () =>{
        let color = colorInput.value;
        document.body.style.backgroundColor = color
    });
}

function func3() {
    //query5
    var var9 = document.getElementById("in").value;
    if (var9 < 0) {
        window.alert("Put a value that is bigger from zero");
    }
    else {
        var var10 = document.getElementById("in").value;
        var par = document.getElementById("par1");
        // Nikos your 3 lines of code below are not enough
        // for (var i = 0; i < var10; i++) {
        //     var star = document.createTextNode("*");
        //     par.appendChild(star);
        function repeatStringNumTimes(str, num) {
            return str;
          }
        
        for(var i=var10;i>=0;i--) 
        {
            for(j=1;j<=i;j++)
            {
                var star = document.createTextNode("*");
                par.appendChild(star);
                par.style.textAlign = "justify"; 
                par.style.position = "relative";
                par.style.left = "50%";
                par.style.right = "50%";
            }
            var br = document.createElement("br");
            par.appendChild(br);
        }

        // Nikos the lines of code are not correct, please see above.
            /*document.createElement("br");
            for (i = par; i >= 1; i--) {
                //inner loop
                for (j = 1; j <= i; j++) {
                    document.createTextNode("*");
                    par.appendChild(star);
                }
                document.createElement("br");
            }*/
        
    }
}

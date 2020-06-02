<?php
//connect to database 
$connection = new mysqli("sql7.freemysqlhosting.net","sql7344408","SCwHcRXUAM","sql7344408"); 
if(mysqli_connect_errno()){
    printf("Connection failed: %s\n",mysqli_connect_error());   
    exit(); 
}
?> 

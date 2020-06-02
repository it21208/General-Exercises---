<?php
include("conn.php");
$username=$_POST['username'];
// $password=sha1($_POST['password']); //my passwords are hashed in the database using the sha1
$password=$_POST['pwd'];
// $checklogin="SELECT * FROM users_tbl WHERE Username=? AND Password=?";
$checklogin="SELECT * FROM logincredentials WHERE user=? AND password=?";
$query = $connection->prepare($checklogin);
$query->bind_param("ss",$username,$password);
$query->execute() or die($connection->error);
$count = $query->num_rows;
if($count==1)
   {
    while($row=$query->fetch_assoc)
        {
     $_SESSION['username']=$row['user'];
    }
header("Location:categories_page.html")
   }
exit;
?>

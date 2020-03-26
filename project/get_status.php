<?php
  include("connection.php");
  $query = "SELECT status FROM transaction ORDER BY id DESC LIMIT 1;";
  $result = mysqli_query($con,$query);
  $result = mysqli_fetch_assoc($result);
  echo $result['status'];
  

?>
<?php 
	include("connection.php");
	
	$photo = $_POST['photo'];
	
	$query = "INSERT INTO `transaction` (`id`, `photo`,`status`) VALUES (NULL, '$photo','');";
	$result = mysqli_query($con,$query);
	$query = "SELECT id FROM transaction ORDER BY id DESC LIMIT 1;";
	$result = mysqli_query($con,$query);
	$result = mysqli_fetch_assoc($result);
	print($result['id']);
?>
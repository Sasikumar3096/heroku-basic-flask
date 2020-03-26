<?php
	if(isset($_POST['id']))
	{
		include('connection.php');
		if($con){
			$id = $_POST['id'];
			$query = "Select email_id from user_info where id = {$id};";
			$result = mysqli_query($con,$query);
			$result = mysqli_fetch_assoc($result);
				
			if($result){
				print $result['email_id'];
			}
		}
	}
	if(isset($_GET['id']))
	{
		include('connection.php');
		if($con){
			$id = $_GET['id'];
			$query = "Select email_id from user_info where id = {$id};";
			$result = mysqli_query($con,$query);
			$result = mysqli_fetch_assoc($result);
				
			if($result){
				print $result['email_id'];
			}
		}
	}
?>
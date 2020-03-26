<?php 
	if(isset($_GET['key'])){
		include("connection.php");
		$action = $_GET['action'];
		$key = $_GET['key'];
		if($action == 1)
				$query = "Update transaction set status = 1 WHERE id = $key";
		else
			$query = "Update transaction set status = 2 WHERE id = $key";
		mysqli_query($con,$query);
}	
?>
<script>
	alert("Your Responce has been Recorded");
</script>
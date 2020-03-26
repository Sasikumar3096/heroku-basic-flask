<?php
	if(isset($_GET['key'])){
		include("connection.php");
		$key = $_GET['key'];
		$query = "Select photo from transaction where id = $key";
		$result = mysqli_query($con,$query);
		$result = mysqli_fetch_assoc($result);
		
		print('');
	}

?>

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
 <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.25/webcam.js"></script>
<script type="text/javascript" src="send_pic.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<style>
body {font-family: Arial, Helvetica, sans-serif;}
form {border: 3px solid #f1f1f1;}

input[type=number] {
  width: 50%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}
.okbtn {
  width: auto;
  padding: 10px 18px;
  background-color: green;
}
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}


.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
 .okbtn {
     width: 100%;
  }
}
</style>
</head>
<body>

<h1 align="center">SSSV BANK</h1>

<form action="/action_page.php" method="post">
  <div class="imgcontainer">
		
  </div>

  <div class="container">
   <center> 
  <a href="record_responce.php?&action=1&key=<?php print($key)?>"><button type="button" class="okbtn">Accept Transaction</button></a>
  <a href="record_responce.php?&action=2&key=<?php print($key)?>"><button type="button" class="cancelbtn">Cancel Transaction</button></a>
  
     
</center>
    
  </div>
   
  <div class="container" style="background-color:#f1f1f1">
 <center>
    <a href="index.html"><button type="button" class="cancelbtn">Cancel</button></a>
    </center>
  </div>
</form>

</body>
</html>

<script>
var image = document.createElement('img');
image.src="<?php echo $result['photo']?>";
    
image.width=300;
image.height=300;
image.alt="here should be some image";
 $(".imgcontainer").html(image);
</script>
	function request(){
		url = "get_status.php"
		$.ajax(url, 
		{
			type: 'POST',  // http method
			data: { },  // data to submit
			success: function (data, status, xhr) {
				console.log(data);
				if(data==0)
				{
					console.log("Running....");
					request();
				}
				if(data==1)
				{$(location).attr('href', 'enter_pin.html');}
				if(data==2){
					alert("The card holder declined your transcation");
					$(location).attr('href', 'index.html');
				}
			},
			error: function (jqXhr, textStatus, errorMessage) {
				alert(errorMessage);
			}
		});
	}
	request();

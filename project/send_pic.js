
	function sendPic(){
		let image_data = $("#photo").attr('src');
		console.log(image_data);	
		
		
		let url = "get_photo.php";

		$.ajax(url, 
		{
			type: 'POST',  // http method
			data: { photo:  image_data},  // data to submit
			success: function (data, status, xhr) {
				console.log(data);
				get_email(data);
				//send_mail("thisismyinternetid@gmail.com",data);
				
			},
			error: function (jqXhr, textStatus, errorMessage) {
				alert(errorMessage);
			}
		});

	}
	function get_email(data){
		let url = "get_email.php";

		$.ajax(url, 
		{
			type: 'POST',  // http method
			data: { id: urlParam('id') },  // data to submit
			success: function (email, status, xhr) {
				console.log(email);
				
				send_mail(email,data);
				
			},
			error: function (jqXhr, textStatus, errorMessage) {
				alert(errorMessage);
			}
		});

	}
	function send_mail(email="thisismyinternetid@gmail.com",key){
		
		
		let url = "http://127.0.0.1:5000/"+email+"/"+key;

		$.ajax(url, 
		{
			type: 'GET',  // http method
			 crossDomain: true,
			success: function (data, status, xhr) {
				console.log("Mail Sent");

				$(location).attr('href', 'loading_page.php')
			},
			error: function (jqXhr, textStatus, errorMessage) {
				alert("Enter Vaid Card Id");
				$(location).attr('href', 'index.html');
			}
		});

	}
	
	function urlParam(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return results[1] || 0;
    }
}

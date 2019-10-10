function add_data(){
var user_name = encodeURI($("#username").val());
var link = encodeURI($("#link").val());
var roll_number = encodeURI($("#roll_number").val());
var final_url = "https://theappcode.herokuapp.com/"+user_name+"/"+roll_number+"/"+link;
if (user_name =="" || roll_number=="" || link =="")
{	alert("Fill All the Values");
return 0;
}
$.ajax(final_url,{
	success: function (data, status, xhr) {
		console.log(data);
		alert("Data Added Success");
	}
});
}

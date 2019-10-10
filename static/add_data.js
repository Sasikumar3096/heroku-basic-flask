fuction add(){
var user_name = encodeURI($("username").html());
var link = encodeURI($("link").html());
var roll_number = encodeURI($("roll_number").html());
var final_url = "https://theappcode.herokuapp.com/"+user_name+"/"+roll_number+"/"+link;

}

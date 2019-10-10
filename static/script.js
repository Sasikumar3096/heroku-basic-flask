function  get_data() {
//POINTS
    $.ajax('https://data.heroku.com/dataclips/bychxylaotgqpdfbatjabprxqzto.json?access-token=ccd1a19e-c447-4251-88af-f4e0670db8b1',   // Order By score
    {
        success: function (data, status, xhr) {// success callback function
			let res = (data.values);
			let no =1;
			res.forEach(function(item){ 
			let name = item[1];
			let roll_number = item[2];
			let points = item[4];
			let badges = item[3];
			let trailmix = item[5];
			let url = item[6];
			$('#points-body').append('<tr><td>'+no+'</td><td>' + name+'</td><td>'+roll_number+'</td><td>'+points+'</td><td>'+badges+'</td><td>'+trailmix+'</td><td>'
			+'<a href="'+url+'" target="_blank">Open Profile</a></td></tr>');
			no++;
    }); 
    }
});

//BADGES
    $.ajax('https://data.heroku.com/dataclips/vfvwzkrskseemogjfcncowpwvglx.json?access-token=7cffc458-f70c-49bc-a39b-19eaed25d776',   // Order By score
    {
        success: function (data, status, xhr) {// success callback function
			let res = (data.values);
			let no =1;
			res.forEach(function(item){ 
			let name = item[1];
			let roll_number = item[2];
			let points = item[4];
			let badges = item[3];
			let trailmix = item[5];
			let url = item[6];
			$('#badges-body').append('<tr><td>'+no+'</td><td>' + name+'</td><td>'+roll_number+'</td><td>'+points+'</td><td>'+badges+'</td><td>'+trailmix+'</td><td>'
			+'<a href="'+url+'" target="_blank">Open Profile</a></td></tr>');
			no++;	
    }); 
    }
});

//TRAILMIX
    $.ajax('https://data.heroku.com/dataclips/ucdyncutuhiiiawsivrqpbrzcrgd.json?access-token=79436e5a-d1f6-4b0a-bc49-6a080af68ca7',   // Order By score
    {
        success: function (data, status, xhr) {// success callback function
			let res = (data.values);
			let no =1;
			res.forEach(function(item){ 
			let name = item[1];
			let roll_number = item[2];
			let points = item[4];
			let badges = item[3];
			let trailmix = item[5];
			let url = item[6];
			$('#trailmix-body').append('<tr><td>'+no+'</td><td>' + name+'</td><td>'+roll_number+'</td><td>'+points+'</td><td>'+badges+'</td><td>'+trailmix+'</td><td>'
			+'<a href="'+url+'" target="_blank">Open Profile</a></td></tr>');
			no++;
    }); 
    }
});


var url ="https://theappcode.herokuapp.com/update";
$("#response").html("The Score is being Updated in the background please wait a second....");
$.ajax(url,   // Order By score
    {
        success: function (data, status, xhr) {// success callback function
				$("#response").html("The Scores are upto date");
			
			

    }
});


}

get_data();

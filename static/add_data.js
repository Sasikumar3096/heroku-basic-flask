fuction add(){
var user_name = encodeURI($("username").html());
var link = encodeURI($("link").html());
var roll_number = encodeURI($("roll_number").html());
var final_url = "https://theappcode.herokuapp.com/"+user_name+"/"+roll_number+"/"+link;

}



<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<div class="container">    
            
    <div id="signupbox" style=" margin-top:50px" class="mainbox col-md-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
        <div class="panel panel-info">
            <div class="panel-heading">
                <div class="panel-title">Add Info</div>

            </div>  
            <div class="panel-body" >
                <form method="post" action=".">
                    <input type='hidden' name='csrfmiddlewaretoken' value='XFe2rTYl9WOpV8U6X5CfbIuOZOELJ97S' />
                            

                    <form  class="form-horizontal" method="post" >
                      
                     
                        <div id="div_id_username" class="form-group required">
                            <label for="id_username" class="control-label col-md-4  requiredField"> Full Name<span class="asteriskField">*</span> </label>
                            <div class="controls col-md-8 ">
                                <input class="input-md  textinput textInput form-control" id="username" maxlength="30" name="username" placeholder="Choose your username" style="margin-bottom: 10px" type="text" />
                            </div>
                        </div>
                        <div id="div_id_email" class="form-group required">
                            <label for="id_email" class="control-label col-md-4  requiredField"> Roll Number<span class="asteriskField">*</span> </label>
                            <div class="controls col-md-8 ">
                                <input class="input-md emailinput form-control" id="roll_number" name="email" placeholder="Your current email address" style="margin-bottom: 10px" type="email" />
                            </div>     
                        </div>
                 
                        <div id="div_id_name" class="form-group required"> 
                            <label for="id_name" class="control-label col-md-4  requiredField"> Trailhead URl<span class="asteriskField">*</span> </label> 
                            <div class="controls col-md-8 "> 
                                <input class="input-md textinput textInput form-control" id="link" name="name" placeholder="Your Frist name and Last name" style="margin-bottom: 10px" type="text" />
                                <small style="color:red"> Enter the URL after https://trailhead.salesforce.com/en/me/ without QUOTES</small>
                            </div>
                        </div>
                     
                        <div class="form-group"> 
                            <div class="aab controls col-md-4 "></div>
                            <div class="controls col-md-8 ">
                                <input type="button" onclick="add_data()" name="Add" value="Add" class="btn btn-primary btn btn-info" id="submit-id-signup" />
                              
                            </div>
                        </div> 
                            
                    </form>

                </form>
            </div>
        </div>
    </div> 
</div>
    





</div>            

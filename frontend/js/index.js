var baseURL = "http://localhost:5000/twitter-sentiment-analysis/v1/";

function signin()
{
	var username = $("#login-username").val();
	var password = $("#login-password").val();
	var payload = {
		"username":username,
		"password":password
	};
	if (username == "" || password == "")
	{
		swal("Warning!", "All fields are mandatory for sign in.", "warning");
	}
	else
	{
		var settings = {
		  "async": true,
		  "crossDomain": true,
		  "url": baseURL + "login",
		  "method": "POST",
		  "headers": {
		    "content-type": "application/json",
		    "cache-control": "no-cache"
		  },
		  "processData": false,
		  "data": JSON.stringify(payload)
		};

		$.ajax(settings).done(function (response) {
		  if (response.status) {
		  	swal("Success", response.message, "success");
		  	sessionStorage.setItem("firstName", response.data.first_name);
		  	sessionStorage.setItem('username',response.data.username);
	  		sessionStorage.setItem('is_admin',response.data.is_admin);
		  	window.setTimeout(function(){
             	window.location.replace("dashboard.html");    
            }, 1500);
		  	
		  }
		  else
		  {
		  	swal("Warning!", response.message, "warning");
		  }
		});
	}
}

function signup()
{
	var username = $("#signup-username").val();
	var password = $("#password").val();
	var confirmPassword = $("#confirm-password").val();
	var firstName = $("#first-name").val();
	var lastName = $("#last-name").val();
	var phone = $("#phone").val();
	var address = $("#address").val();
	var registrationNumber = $("#registration-no").val();
	var speciality = $("#speciality").val();
	var email = $("#email").val();
	if(password == confirmPassword)
	{
		var payload = {
			"username" : username,
			"password" : password,
			"first_name" : firstName,
			"last_name" : lastName,
			"address" : address,
			"phone_no" : phone,
			"email" : email,
			"registration_no" : registrationNumber,
			"speciality":speciality
		};
		var settings = {
		  "async": true,
		  "crossDomain": true,
		  "url": baseURL + "register",
		  "method": "POST",
		  "headers": {
		    "content-type": "application/json",
		    "cache-control": "no-cache"
		  },
		  "processData": false,
		  "data": JSON.stringify(payload)
		};

		$.ajax(settings).done(function (response) {
		  if (response.status) {
		  	swal("Success", response.message, "success");
		  	sessionStorage.setItem("firstName", response.data.first_name);
		  	sessionStorage.setItem('username',response.data.username);
	  		sessionStorage.setItem('is_admin',response.data.is_admin);
		  	window.setTimeout(function(){
             	window.location.replace("dashboard.html");    
            }, 1500);
		  }
		  else
		  {
		  	swal("Warning!", response.message, "warning");
		  }
		});
	}
	else
	{
		swal("Warning!", "Password and Confirm Password must be same.", "warning");
	}
}

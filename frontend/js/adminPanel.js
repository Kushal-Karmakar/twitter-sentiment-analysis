var baseURL = "http://localhost:5000/twitter-sentiment-analysis/v1/";

$(document).ready(function(){

	if (sessionStorage.getItem("firstName") == null || sessionStorage.getItem("is_admin") == null) {
		swal("Warning!", "Your session has expired, please sign in again.", "warning");
	  	window.setTimeout(function(){
         	window.location.replace("index.html");
        }, 2000);
	}
	else
	{
		$('#user-message').text('Hi, '+ sessionStorage.getItem("firstName") +'!');
	
		populateHashtagTableData();
		populateTableData();
		getSelectedOperator();

		$('#hashtagtable').on('click','.btn-success',function(){
			var current_row = $(this).closest('tr');
			var hashtag = current_row.find('td:eq(1)').text();
			var settings = {
			  "async": true,
			  "crossDomain": true,
			  "url": baseURL + "activate-hashtag/" + hashtag,
			  "method": "PUT",
			  "headers": {
			    "cache-control": "no-cache"
			  }
			}

			$.ajax(settings).done(function (response) {
			  if (response.status) {
			  	swal("Success!", response.message, "success");
			  	window.setTimeout(function(){
	             	location.reload();
	            }, 2000);
			  }
			  else
			  {
			  	swal("Error!", "Oops! Something went wrong", "error");
			  }
			});
		});

		$('#hashtagtable').on('click','.btn-danger',function(){
			var current_row = $(this).closest('tr');
			var hashtag = current_row.find('td:eq(1)').text();
			var settings = {
			  "async": true,
			  "crossDomain": true,
			  "url": baseURL + "deactivate-hashtag/" + hashtag,
			  "method": "PUT",
			  "headers": {
			    "cache-control": "no-cache"
			  }
			}

			$.ajax(settings).done(function (response) {
			  if (response.status) {
			  	swal("Success!", response.message, "success");
			  	window.setTimeout(function(){
	             	location.reload();
	            }, 2000);
			  }
			  else
			  {
			  	swal("Error!", "Oops! Something went wrong", "error");
			  }
			});
		});

		$('#datatable').on('click','.btn-success',function(){
			var current_row = $(this).closest('tr');
			var username = current_row.find('td:eq(0)').text();
			var settings = {
			  "async": true,
			  "crossDomain": true,
			  "url": baseURL + "promote-user/" + username,
			  "method": "PUT",
			  "headers": {
			    "cache-control": "no-cache"
			  }
			}

			$.ajax(settings).done(function (response) {
			  if (response.status) {
			  	swal("Success!", response.message, "success");
			  	window.setTimeout(function(){
	             	location.reload();
	            }, 2000);
			  }
			  else
			  {
			  	swal("Error!", "Oops! Something went wrong", "error");
			  }
			});
		});

		$('#datatable').on('click','.btn-danger',function(){
			var current_row = $(this).closest('tr');
			var username = current_row.find('td:eq(0)').text();
			var settings = {
			  "async": true,
			  "crossDomain": true,
			  "url": baseURL + "demote-user/" + username,
			  "method": "PUT",
			  "headers": {
			    "cache-control": "no-cache"
			  }
			}

			$.ajax(settings).done(function (response) {
			  if (response.status) {
			  	swal("Success!", response.message, "success");
			  	
			  	window.setTimeout(function(){
	             	location.reload();
	            }, 2000);
			  }
			  else
			  {
			  	swal("Error!", "Oops! Something went wrong", "error");
			  }
			});
		});
	}


});

function populateHashtagTableData()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "hashtags",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	};

	$.ajax(settings).done(function (response) {
	  var hashtag_data = "";
	  $.each(response.data,function(key,value){
	  	hashtag_data += "<tbody>";
	  	hashtag_data += "<tr>";
	  	hashtag_data += "<td>"+value.id+"</td>";
	  	hashtag_data += "<td>"+value.hashtag+"</td>";
	  	if (value.is_activated == 1)
	  	{
	  		hashtag_data += "<td><button class=\"btn btn-success disabled\">Activate</button><button class=\"btn btn-danger\">Deactivate</button></td>";
	  	}
	  	else
	  	{
	  		hashtag_data += "<td><button class=\"btn btn-success\">Activate</button><button class=\"btn btn-danger disabled\">Deactivate</button></td>";
	  	}
	  	hashtag_data += "</tr>";
	  	hashtag_data += "</tbody>";
	  });
	  $('#hashtagtable').append(hashtag_data);
	  $('#hashtagtable').DataTable();
	});
}

function populateTableData()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "users",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	};

	$.ajax(settings).done(function (response) {
	  // console.log(response);
	  var users_data = "";
	  $.each(response.data,function(key,value){
	  	users_data += "<tbody>";
	  	users_data += "<tr>";
	  	users_data += "<td>"+value.username+"</td>";
	  	users_data += "<td>"+value.first_name+"</td>";
	  	users_data += "<td>"+value.last_name+"</td>";
	  	users_data += "<td>"+value.registration_no+"</td>";
	  	users_data += "<td>"+value.speciality+"</td>";
	  	users_data += "<td>"+value.address+"</td>";
	  	if (value.is_admin == 1)
	  	{
	  		users_data += "<td><button class=\"btn btn-success disabled\">Activate</button><button class=\"btn btn-danger\">Deactivate</button></td>";
	  	}
	  	else
	  	{
	  		users_data += "<td><button class=\"btn btn-success\">Activate</button><button class=\"btn btn-danger disabled\">Deactivate</button></td>";
	  	}
	  	users_data += "</tr>";
	  	users_data += "</tbody>";
	  });
	  $('#datatable').append(users_data);
	  $('#datatable').DataTable();
	});
}

function createHashtag()
{
	var hashtag = $("#hashtag").val();
	alert(hashtag);
	var payload = {
		"hashtag" : hashtag
	};

	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "create-hashtag",
	  "method": "POST",
	  "headers": {
	    "content-type": "application/json",
	    "cache-control": "no-cache"
	  },
	  "processData": false,
	  "data": JSON.stringify(payload)
	};

	$.ajax(settings).done(function (response) {
	  if (response.status)
	  {
	  	swal("Success", response.message, "success");
	  	window.setTimeout(function(){
             	location.reload();
            }, 2000);
	  }
	  else
	  {
	  	swal("Warning!", response.message, "warning");
	  }
	});
}

function getSelectedOperator()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "operations",
	  "method": "GET",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status)
	  {
	  	if (response.data[0].operation == "OR") {
	  		$(".btn-or").prop('disabled', true);
	  	}
	  	else
	  	{
	  		$(".btn-and").prop('disabled', true);
	  	}
	  }
	});
}

function clickANDOperator()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "update-operation/AND",
	  "method": "PUT",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status) {
	  	swal("Success", response.message, "success");
	  	window.setTimeout(function(){
             	location.reload();
            }, 2000);
	  }
	  else
	  {
	  	swal("Warning!", response.message, "warning");
	  }
	});
}

function clickOROperator()
{
	var settings = {
	  "async": true,
	  "crossDomain": true,
	  "url": baseURL + "update-operation/OR",
	  "method": "PUT",
	  "headers": {
	    "cache-control": "no-cache"
	  }
	}

	$.ajax(settings).done(function (response) {
	  if (response.status) {
	  	swal("Success", response.message, "success");
	  	window.setTimeout(function(){
             	location.reload();
            }, 2000);
	  }
	  else
	  {
	  	swal("Warning!", response.message, "warning");
	  }
	});
}

function logout()
{
	swal("Success!", "You are successfully logged out.", "success");
	sessionStorage.getItem("firstName") = null;
	sessionStorage.getItem("is_admin") = null;
  	window.setTimeout(function(){
     	window.location.replace("index.html");
    }, 2000);
}
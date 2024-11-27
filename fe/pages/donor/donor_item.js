function init_donor_item(id){
	$('#x-body').load('/fe/pages/donor/donor_item.htm')

	if (id != ''){		
		$.get( "/api/donor/" + id, function( data ) {
			render_details(data);
		});
	}
}

function save_donor(){
	formData = {
		"donor_name":$('#donorname').val()
	}
	var centerId = $('#donorid').val();
	
	var jsonData = JSON.stringify(formData);
	console.log(jsonData)
	$.post({
			url:"/api/donor/" + centerId,
			contentType:'application/json',
			data: jsonData
			})			
	 .done(function( data ) {
		show_donor_list();
	 }); 
}

function show_donor_list(){
	$.getScript('/fe/pages/donor/donor_list.js')
}

function render_details(data){
	$('#donorid').val(data._id)
	$('#donorname').val(data.donor_name)
}
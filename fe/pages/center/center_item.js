function init_author_item(id){
	$('#x-body').load('/fe/pages/center/center_item.htm')

	if (id != ''){		
		$.get( "/api/center/" + id, function( data ) {
			render_details(data);
		});
	}
}

function save_center(){
	formData = {
		"center_name":$('#centername').val()
	}
	var centerId = $('#centerid').val();
	
	var jsonData = JSON.stringify(formData);
	console.log(jsonData)
	$.post({
			url:"/api/center/" + centerId,
			contentType:'application/json',
			data: jsonData
			})			
	 .done(function( data ) {
		show_center_list();
	 }); 
}

function show_center_list(){
	$.getScript('/fe/pages/center/center_list.js')
}

function render_details(data){
	$('#centerid').val(data._id)
	$('#centername').val(data.center_name)
}
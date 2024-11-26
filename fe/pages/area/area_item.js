function init_author_item(id){
	$('#x-body').load('/fe/pages/area/area_item.htm')

	if (id != ''){		
		$.get( "/api/area/" + id, function( data ) {
			render_details(data);
		});
	}
}

function save_area(){
	formData = {
		"area_name":$('#areaname').val()
	}
	var areaId = $('#areaid').val();
	
	var jsonData = JSON.stringify(formData);
	console.log(jsonData)
	$.post({
			url:"/api/area/" + areaId,
			contentType:'application/json',
			data: jsonData
			})			
	 .done(function( data ) {
		show_area_list();
	 }); 
}

function show_area_list(){
	$.getScript('/fe/pages/area/area_list.js')
}

function render_details(data){
	$('#areaid').val(data._id)
	$('#areaname').val(data.area_name)
}
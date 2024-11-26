function init_author_item(id){
	$('#x-body').load('/fe/pages/author/author_item.htm')

	if (id != ''){		
		$.get( "/api/author/" + id, function( data ) {
			render_details(data);
		});
	}
}

function save_author(){
	formData = {
		"name":$('#authorname').val()
	}
	var authorId = $('#authorid').val();
	
	var jsonData = JSON.stringify(formData);
	console.log(jsonData)
	$.post({
			url:"/api/author/" + authorId,
			contentType:'application/json',
			data: jsonData
			})			
	 .done(function( data ) {
		show_author_list();
	 }); 
}

function show_author_list(){
	$.getScript('/fe/pages/author/author_list.js')
}

function render_details(data){
	$('#authorid').val(data._id)
	$('#authorname').val(data.name)
}
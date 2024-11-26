function init_area_list(){
	$('#x-body').load('/fe/pages/area/area_list.htm')
	$.get( "/api/area/", function( data ) {
		render_area_table(data);
	});
}

function render_area_table(data){
	area_table_html = `
		<table class="table table-striped" id="tbl_ch">
		  <thead  class="table-dark">
			<tr>
			  <th scope="col">Area</th>			  
			  <th scope="col" class="text-center">Action</th>
			</tr>
		  </thead>
		  <tbody>
		`;

	for (let i = 0; i < data.length; i++){
		console.log(data[i]);
		area_table_html += '<tr>'
		area_table_html += '<td class="col-2">' + data[i].area_name + '</td>'
		area_table_html += '<td class="col-2">'
		area_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="del_area(\'' + data[i]._id + '\')"><i class="bi bi-trash"></i></button>';
		area_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="find_area(\'' + data[i]._id + '\')"><i class="bi bi-pencil-square"></i></button>';
		area_table_html += '</td>'
	}

	area_table_html += '</tbody></table>';
	document.getElementById('div_area_table').innerHTML = area_table_html;
}

function add_area(){
	//alert('Adding new area');	
	$.getScript("/fe/pages/area/area_item.js", function() {
		init_area_item('');
	});
}

function find_area(id){
	//alert('Finding area ' + id);	
	$.getScript("/fe/pages/area/area_item.js", function() {
		init_area_item(id);
	});
}

function del_area(id){
	if (confirm('Are you sure you want to delete this area?')){
		$.ajax({
		  method: "DELETE",
		  url: "/api/area/" + id
		})
		  .done(function( msg ) {
			alert("area Deleted");
			init_area_list();
		  });				
	}
}
init_area_list();
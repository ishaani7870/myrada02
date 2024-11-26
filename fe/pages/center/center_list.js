function init_center_list(){
	$('#x-body').load('/fe/pages/center/center_list.htm')
	$.get( "/api/center/", function( data ) {
		render_center_table(data);
	});
}

function render_center_table(data){
	center_table_html = `
		<table class="table table-striped" id="tbl_ch">
		  <thead  class="table-dark">
			<tr>
			  <th scope="col">Center</th>			  
			  <th scope="col" class="text-center">Action</th>
			</tr>
		  </thead>
		  <tbody>
		`;

	for (let i = 0; i < data.length; i++){
		console.log(data[i]);
		center_table_html += '<tr>'
		center_table_html += '<td class="col-2">' + data[i].center_name + '</td>'
		center_table_html += '<td class="col-2">'
		center_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="del_area(\'' + data[i]._id + '\')"><i class="bi bi-trash"></i></button>';
		center_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="find_area(\'' + data[i]._id + '\')"><i class="bi bi-pencil-square"></i></button>';
		center_table_html += '</td>'
	}

	center_table_html += '</tbody></table>';
	document.getElementById('div_center_table').innerHTML = center_table_html;
}

function add_center(){
	//alert('Adding new center');	
	$.getScript("/fe/pages/center/center_item.js", function() {
		init_center_item('');
	});
}

function find_center(id){
	//alert('Finding center ' + id);	
	$.getScript("/fe/pages/center/center_item.js", function() {
		init_center_item(id);
	});
}

function del_center(id){
	if (confirm('Are you sure you want to delete this center?')){
		$.ajax({
		  method: "DELETE",
		  url: "/api/center/" + id
		})
		  .done(function( msg ) {
			alert("center Deleted");
			init_center_list();
		  });				
	}
}
init_center_list();
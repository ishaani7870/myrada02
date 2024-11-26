function init_donor_list(){
	$('#x-body').load('/fe/pages/donor/donor_list.htm')
	$.get( "/api/donor/", function( data ) {
		render_donor_table(data);
	});
}

function render_donor_table(data){
	donor_table_html = `
		<table class="table table-striped" id="tbl_ch">
		  <thead  class="table-dark">
			<tr>
			  <th scope="col">donor</th>			  
			  <th scope="col" class="text-donor">Action</th>
			</tr>
		  </thead>
		  <tbody>
		`;

	for (let i = 0; i < data.length; i++){
		console.log(data[i]);
		donor_table_html += '<tr>'
		donor_table_html += '<td class="col-2">' + data[i].donor_name + '</td>'
		donor_table_html += '<td class="col-2">'
		donor_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="del_area(\'' + data[i]._id + '\')"><i class="bi bi-trash"></i></button>';
		donor_table_html += '<button type="button" class="btn btn-primary float-end mx-2" onclick="find_area(\'' + data[i]._id + '\')"><i class="bi bi-pencil-square"></i></button>';
		donor_table_html += '</td>'
	}

	donor_table_html += '</tbody></table>';
	document.getElementById('div_donor_table').innerHTML = donor_table_html;
}

function add_donor(){
	//alert('Adding new donor');	
	$.getScript("/fe/pages/donor/donor_item.js", function() {
		init_donor_item('');
	});
}

function find_donor(id){
	//alert('Finding donor ' + id);	
	$.getScript("/fe/pages/donor/donor_item.js", function() {
		init_donor_item(id);
	});
}

function del_donor(id){
	if (confirm('Are you sure you want to delete this donor?')){
		$.ajax({
		  method: "DELETE",
		  url: "/api/donor/" + id
		})
		  .done(function( msg ) {
			alert("donor Deleted");
			init_donor_list();
		  });				
	}
}
init_donor_list();
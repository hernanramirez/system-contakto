function userDetail(id) {
    var url = "/core/user/detail/999999999/";
    document.location.href = url.replace('999999999', id);

}

function userUpdate(id) {
    var url = "/core/user/update/999999999/";
    document.location.href = url.replace('999999999', id);
}

function userUpdatePassword(id) {
    var url = "/core/user/password/update/999999999/";
    document.location.href = url.replace('999999999', id);
}


$(document).ready(function () {

    $("#datatable-users").DataTable({
        "serverSide": true,
        "ajax": "/core/api/users/?format=datatables",
        "language": {
            "url": "/static/libs/datatables.net/lang/es-ES.json"
        },
        columnDefs: [
            {
                targets: 5,
                render: function (data) {
                    let grupos = "";
                    for (i = 0; i < data.length; i++) {
                        grupos += data[i].name + '<br>';
                    } 
                    return grupos;
                },

            },
            {
                targets: 6,
                className: 'dt-body-center', 
                render: function (data, type, row) {
                    if (data==true){
                        return '<i class="fa fa-check"></i>';
                    }else{
                        return '<i class="fa fa-times"></i>';
                    }
                },
            },
            {
                targets: 7,
                className: 'dt-body-center', 
                render: function (data, type, row) {
                    if (data==true){
                        return '<i class="fa fa-check"></i>';
                    }else{
                        return '<i class="fa fa-times"></i>';
                    }
                },
            },
        ],
        "columns": [
            { "data": null,
                "orderable": false,
                "searchable": false,
                "width": "65px",
                "render": function (data, type, row, meta) {
    
                  var a = '<div class="btn-group" role="group" aria-label="Basic checkbox toggle button group">'
                  a += '<a class="btn btn-primary" onclick="userDetail(\'' + row.id + '\')"><i class="bx bxs-user-detail font-size-16 align-middle"></i></a>';
                  a += '<a class="btn btn-primary" onclick="userUpdate(\'' + row.id + '\')"><i class="bx bx-edit-alt font-size-16 align-middle"></i></a>';
                  a += '<a class="btn btn-primary" onclick="userUpdatePassword(\'' + row.id + '\')"><i class="bx bx bx-key font-size-16 align-middle"></i></a>';
    
    
                  a += '</div>'
                  return a;
                }
            },
            {"data": "id", "title": "Id", "searchable": false, "visible": false},
            {"data": "first_name", "title": "Nombres", "responsivePriority": 0,},
            {"data": "last_name", "title": "Apellidos", "responsivePriority": 0,}, 
            {"data": "email", "title": "Email"},
            {"data": "groups", "title": "Grupos", "searchable": false}, 
            {"data": "is_active", "title": "Activo", "searchable": false},
            {"data": "is_staff", "title": "Administrador", "searchable": false},
        ],
        lengthChange: !1,
        // buttons: ["copy", "excel", "pdf", "colvis"],
        "initComplete": function (settings, json) {
            $('div.loading-table-data').hide()
          },
    });

});

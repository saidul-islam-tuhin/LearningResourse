/**
 * Created by Saidul on 8/18/2017.
 */
function create_post(){
    console.log("function is working");
    $.ajax({
            type: "POST",
            url: "result/",
            data:{
                'post_value': $('#test_input').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },

            success : function (json) {
                $('#test_value').val('');
                console.log(json);
                alert("success working");
            },

            error: function (xhr,errmsg,err) {
                alert("error");
                $('#result').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText);
            }
        });
}
$("#test_form").on('submit',function(event){
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    var value = $('#test_value').val();
    console.log(value);
    create_post();

});

$('#id_username').change(function () {
    var username =$(this).val();
    var form = $(this).closest("form");
    $.ajax({
        url: form.attr("data-validate-username-url"), 
        data: form.serialize(), // its send to view
        datatype: 'json',
        success: function (data,url) {
            console.log(data.password);
            //console.log(url.url);
            if (data.is_taken){
                alert(data.error); // it comes from view
                console.log("check working");
            }
        }
    });
});

$('#json_test').keyup(function () {
    var value = $(this).val();
    console.log("working");
    $.ajax({
         url: '/ajax/json/',
         data: {'value': value,}, //send to view function and convertinto json
         datatype: 'json',
         success: function (data) {
             console.log("success working");
             alert(data.hello); // json er data
             console.log(data.input_value); //get from view function which are convert in json
         }

     });
});

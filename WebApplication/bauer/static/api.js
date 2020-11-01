$("document").ready(function(){
    $("#equal").click(function(){
        var message = $("#stringexpression").val();
        console.log(message);
        $.ajax({
            url: "http://localhost:5000/api/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": message}),
            dataType: "json"
        }).done(function(data) {
            console.log(data);
        });
    });
});

$(function() {
    $("#btnSearch").click(function() {
        $("#tableSeries").children("tbody").html('');
        $.getJSON("http://localhost:5000/search/title/" + $("#text").val(), function(data) {
            var html = "";
            $.each(data, function(i, item) {
                html += "<tr><td>" + item.title + "</td><td>" + item.notes + "</td><td>" + item.genre + "</td><td>" + item.year + "</td></tr>";
            });
            $("#tableSeries").children("tbody").html(html);
        });
    });
});
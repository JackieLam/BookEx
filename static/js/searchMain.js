$(function () {
    type = $.getUrlParam("type");
    hint = $.getUrlParam("hint").toString();

    $("#search_input").val(hint);
    books = search(type, hint);

    var radio = $("input[type='radio'][name='type']");
    switch (type) {
        case 'book_name':
            $("#radio0").attr("checked") = true;
            $("#radio1").attr("checked") = false;
            $("#radio2").attr("checked") = false;
            break;
        case 'author':
            $("#radio1").attr("checked") = true;
            $("#radio0").attr("checked") = false;
            $("#radio2").attr("checked") = false;
            break;
        case 'genre':
            alert(1);
            $("#radio2").attr("checked") = true;
            $("#radio1").attr("checked") = false;
            $("#radio0").attr("checked") = false;
            break;
    }


});
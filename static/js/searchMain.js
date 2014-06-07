$(function () {
    type = $.getUrlParam("type");
    hint = $.getUrlParam("hint").toString();
    $("#search_input").val(hint);

    search(type, hint);

    console.log(type + hint);
    var radio = $("input[type='radio'][name='type']");
    switch (type) {
        case "book_name":
            $("#radio0").removeAttr("checked");
            $("#radio2").removeAttr("checked");
            $("#radio1").attr("checked", true);
            break;
        case "author":
            
            $("#radio1").removeAttr("checked");
            $("#radio0").removeAttr("checked");
            $("#radio2").attr("checked", true);
            break;
        case "genre":
            
            $("#radio1").removeAttr("checked");
            $("#radio2").removeAttr("checked");
            $("#radio0").attr("checked", true);
            break;
    }
});
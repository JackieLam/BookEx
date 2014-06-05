(function ($) {
    $.getUrlParam = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return decodeURIComponent(r[2]); return null;
    }
})(jQuery);

function search(type, hint) {
    var books = [];

    $.ajax({
        dataType: "json",
        url: "sysubookex.sinaapp.com/api/v1/books",
        data: { type: hint },
        success: function (data) {
            books = data;
            if (books == []) {
                location.href = "/notfound";
            }
            else {
                $("#result").html("");
                for (book in books) {

                    var div = "<div class=\"book_container\"><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\""+ books[book].book_name +"\">"+
                    "<img src=\"\" alt=\""+ books[book].book_name +"\"></a>"+
            "</div><div class=\"bookInfo\"><p class=\"bookName\">书名：" + books[book].book_name + "</p>" +
                    "<p class=\"author\">作者：" + books[book].author + "</p><p class=\"bookType\">类别：" + books[book].genre + "</p>" +
                    "<p class=\"bookNum\">x人提供此书</p></div><div class=\"clear\"></div></div>";

                    $("#result").append(div);
                }
            }
        },
        error: function () {
            location.href = "/notfound";
        }
    });

    return books;
}

$(function () {
    // 搜索按钮被按下时
    $("#search_btn").click(function () {

        var hint = $("#search_input").val();
        var type = $('input[type="radio"][name="type"]:checked').val();

        if (!hint) {
            location.href = "/notfound";
        }
        else {
            location.href = "/found?hint=" + encodeURIComponent(hint) + "&type=" + type;


        }
    });

    //登录模块


   
});
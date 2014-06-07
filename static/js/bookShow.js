(function ($) {
    $.getUrlParam = function (name) {
        var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
        var r = window.location.search.substr(1).match(reg);
        if (r != null) return decodeURIComponent(r[2]); return null;
    }
})(jQuery);

$(function () {
    var book_id = $.getUrlParam("book_id");

    if (!book_id) {
        history.back(-1);
    }
    else {
        var user = $("#user_id").html();
        $("#punish").click(function () {
            location.href = "/addbook";
        });
        $.ajax({
            dataType: "json",
            url: "api/v1/books",
            data: { "book_name": book_id },
            success: function (data) {
                console.log(data);

                $bookItem = "<p class=\"bookName\">书名：" + data[0].book_name + "</p>" +
                    "<p class=\"author\">作者：" + data[0].author + "</p><p class=\"bookType\">类别：" + data[0].genre + "</p>" +
                    "<p class=\"bookNum\">x人提供此书</p>";

                $("#bookInfo").prepend($bookItem);

                if (data[0].summary) {
                    var summary = "<h3 class=\"headline\">详情</h3><hr /><p>" + data[0].summary + "</p>";
                    $("#information").html(summary);
                    $("#information").show();
                }
                else {
                    $("#information").hide();
                }

                $.ajax({
                    dataType: "json",
                    data: { "book_name": book_id },
                    url: "api/v1/comment",
                    success: function (data) {
                        console.log(data);

                        var i = 0;
                        if (data) {
                            $("#comment_content").show();
                        }
                        else {
                            $("#comment_content").hide();
                        }
                        while (data[i].content) {
                            var content = "<p>" + data[i].content + "</p>" +
                                "<p class=\"user_name\">By: " + data[i].user_id + "</p>";


                            $("#comment_content").append(content);
                            i++;
                        }
                    }
                });
            }
        });

        $("#comment").click(function () {

            if (!user) {
                alert("你还未登录~请点击右上角的登录按钮");
            }
            else {
                var comment_input = $("#comment_input").val();

                if (!comment_input) {
                    alert("评论不能为空！");
                }
                else {
                    $.ajax({
                        type: "post",
                        data: {
                            "book_name": book_id,
                            "user_id": user,
                            "content": comment_input
                        },
                        url: "api/v1/comment",
                        success: function (data) {
                            console.log(data);
                        }
                    });
                }
            }
        });
    }



});
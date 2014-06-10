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
            data: { "isbn": book_id },
            success: function (data) {
                console.log(data);

                var $bookCover = "<div class=\"cover\"><a href=\'book?book_id=" + data[0].isbn + "\' target=\"_blank\" title=\"" + data[0].book_name +
                                        "\"><img src=\"" + data[0].image_url + "\" alt=\"" + data[0].book_name +
                                    "\"></a></div>";

                var $bookItem = "<p class=\"bookName\">书名：" + data[0].book_name + "</p>" +
                    "<p class=\"author\">作者：" + data[0].author + "</p><p class=\"bookType\">类别：" + data[0].genre + "</p>" +
                    "<p class=\"isbn\">ISBN：<span id=\"isbn\">"+data[0].isbn+"</span></p>";

                $("#book").prepend($bookCover);
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
                    data: { "isbn": book_id },
                    url: "api/v1/comment",
                    success: function (data) {
                        console.log(data);

                        var i = 0;
                        
                        if (data.length === 0) {
                            $("#comment_content").hide();
                        }
                        else {
                            
                            $("#comment_content").show();
                            while (data[i]) {
                                var content;
                         
                                if (user == data[i].user_id) {
                                    content = "<p><button class=\"delete greenBtn\" id=\"deletebook\">删除</button>" + data[i].content + "</p>" +
                                    "<p class=\"user_name\">By: <span class=\"users\">"+ data[i].user_id + "</span></p>";
                                }
                                else {
                                    content = "<p>" + data[i].content + "</p>" +
                                    "<p class=\"user_name\">By: <span class=\"users\">"+ data[i].user_id + "</span></p>";
                                }

                                $("#comment_content").append(content);
                                i++;
                            }
                        }
                       
                    }
                }).done(function () {
                    $("#deletebook").click(function () {
                        var isbn = $("#isbn").val().toString();
                        var user_id = $("#user_id").val().toString();
                        console.log(isbn + user_id);

                        $.ajax({
                            type: "DELETE",
                            dataType: "json",
                            url: "/api/v1/comment",
                            data: { "isbn": isbn, "user_id": user_id },
                            success: function (data) {
                                alert("删除评论成功！");
                            }
                        });
                    });
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
                    console.log(comment_input);
                    $.ajax({
                        type: "post",
                        dataType: "json",
                        data: {
                            "isbn": book_id,
                            "user_id": user,
                            "content": comment_input
                        },
                        url: "api/v1/comment",
                        success: function (data) {
                            console.log(data);

                            location.reload();
                        },
                        error: function () {
                            alert("不好意思，您只能对同一本书评论一次~");
                        }
                    });
                }
            }
        });
    }
});
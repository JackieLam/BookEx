$(function () {
    user = $("#user_id").html();

    if (user == undefined) {
        location.href = "/api/v1/users/login";
    }
    else {
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/api/v1/info",
            data: {"user_id": user.toString()},
            success: function (data) {
                $("#userName").html("名字："+data[0].user_name);
                $("#userLocation").html("地址："+data[0].address);
                $("#communicate").html("email："+data[0].email);
            }
        });

        $.ajax({
            dataType: "json",
            url: "/api/v1/borrowbook",
            data: {"owner_id": user},
            success: function (data) {
                console.log(data);
                $("#myBookDetail").html("");
                if (data.length == 0) {
                    $("#myBookDetail").append("<p style=\"font-size:0.8em; margin: 10px;\">你没有共享自己的书籍哦~~<a href=\"/addbook\" class=\"greenBtn\" style=\"margin-left:50px;\">添加书籍</a></p>");
                }
                else {
                    for (book in data) {
                        var div = "<li><img  src=\"./static/img/2.jpg\"><p>" + data[book].book_name + "</p></li>";

                        $("#myBookDetail").append(div);
                    }
                }
            }
        });

        $.ajax({
            dataType: "json",
            url: "/api/v1/savebook",
            data: { "user_id": user },
            success: function (data) {
                console.log(data);
                $("#myDetail").html("");
                for (book in data) {
                    var div = "<li><img  src=\"./static/img/2.jpg\"><p>" + data[book].book_name + "</p></li>";

                    $("#myDetail").append(div);
                }
            }
        });


    }
});
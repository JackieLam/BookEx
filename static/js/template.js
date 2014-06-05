$(document).ready(function () {
    //$.post("api/v1/books/add", { "book_name": "hihi", "author": "万海", "genre": "科技", "image_url": "", "summary": "sshsh", "user_id": "11331066" },
    //function () { alert(1); });

    $.ajax({
        dataType: "json",
        url: "//sysubookex.sinaapp.com/api/v1/books",
        success: function (data) {
            console.log(data);
            var book = {};

            $("#books").html("");
            console.log(data[0]);
            for (book in data) {

                $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                            "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                        "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                $("#books").append($bookItem);
            }
        }
    });

    var menu = $("menu li");
    menu.click(function () {
        switch (menu.index(this)) {
            case 0:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "教材教辅" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 1:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "少儿" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 2:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "文学艺术" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 3:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "人文社科" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 4:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "经济管理" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 5:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/api/v1/books",
                    data: { "genre": "励志与成功" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 6:
                $.ajax({
                    dataType: "json",
                    url: "//sysubookex.sinaapp.com/v1/books",
                    data: { "genre": "科技" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\"\" target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\"" + data[book].image_url + "\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
        }
    });

});
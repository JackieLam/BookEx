$(document).ready(function () {
    //$.post("api/v1/books/add", { "book_name": "hihi", "author": "万海", "genre": "科技", "image_url": "", "summary": "sshsh", "user_id": "11331066" },
    //function () { alert(1); });

    $.ajax({
        dataType: "json",
        url: "api/v1/books",
        success: function (data) {
            console.log(data);
            var book = {};

            $("#books").html("");
            console.log(data[0]);
            for (book in data) {

                $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                            "\"><img src=\""+ data[book].image_url +"\" alt=\"" + data[book].book_name +
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
                    url: "api/v1/books",
                    data: { "genre": "eduBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 1:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "kidBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 2:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "artBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 3:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "peoBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 4:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "ecoBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 5:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "sucBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
            case 6:
                $.ajax({
                    dataType: "json",
                    url: "api/v1/books",
                    data: { "genre": "techBook" },
                    success: function (data) {
                        console.log(data);
                        var book = {};

                        $("#books").html("");
                        console.log(data[0]);
                        for (book in data) {

                            $bookItem = "<li><div class=\"cover\"><a href=\'book?book_id="+data[book].isbn+"\' target=\"_blank\" title=\"" + data[book].book_name +
                                        "\"><img src=\""+data[book].image_url+"\" alt=\"" + data[book].book_name +
                                    "\"></a></div><a class=\"info\">" + data[book].book_name + "</a></li>";

                            $("#books").append($bookItem);
                        }
                    }
                });
                break;
        }
    });
});
$(function () {
    $("#submit").click(function () {
        var book_name = $("#book_name").val().toString();
        var isbn = $("#isbn").val().toString();
        var image_url = $("#image_url").val().toString();
        var author = $("#author").val().toString();
        var genre = $("#genre").val().toString();
        var summary = $("#summary").val().toString();
        var user_id = $("#user_id").html() ? $("#user_id").html().toString() : null;
        console.log(image_url);
        if (!user_id) {
            alert("你还未登录！请点击右上角登录按钮，登陆后登记书本信息");
        }
        else {
            if (isbn && book_name && author && genre) {

                $.post("api/v1/books/add",
                    {
                        "book_name": book_name,
                        "isbn": isbn,
                        "author": author,
                        "image_url": image_url,
                        "genre": genre,
                        "summary": summary,
                        "user_id": user_id
                    },
                    function (data) {
                        alert("成功添加书籍！");
                    }).error(function () { alert("添加书籍失败！"); });
            }
            else {
                alert("请确认标 * 的必填项已填满");
            }
        }
    });
});
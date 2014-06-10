$(function () {
    $("#submit").click(function () {
        var book_name = $("#book_name").val().toString();
        var image_url = $("#image_url").val().toString();
        var author = $("#author").val().toString();
        var genre = $("#genre").val().toString();
        var summary = $("#summary").val().toString();
        var user_id = $("#user_id").html() ? $("#user_id").html().toString() : null;
        console.log(typeof (book_name));
        if (!user_id) {
            alert("你还未登录！请点击右上角登录按钮，登陆后登记书本信息");
        }
        else {
            if (book_name && author && genre) {

                $.post("api/v1/books/add",
                    {
                        "book_name": book_name,
                        "author": author,
                        "image_url": "none",
                        "genre": genre,
                        "summary": summary,
                        "user_id": user_id
                        //"book_name": "xiyouji",
                        //"author": 3,
                        //"image_url": 3,
                        //"genre": 3,
                        //"summary": 3,
                        //"user_id": 3
                    },
                    function (data) {
                        alert("成功添加书籍！");
                    });
            }
            else {
                alert("请确认标 * 的必填项已填满");
            }
        }
    });
});
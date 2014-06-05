$(function () {
    $("#submit").click(function () {
        var book_name = $("#book_name").val();
        var image_url = $("#image_url").val();
        var author = $("#author").val();
        var genre = $("#genre").val();
        var summary = $("#summary").val();
        var user_id = $("#user_id").val()?$("#user_id").val() : null;

        console.log(image_url);
        if (!user_id) {
            alert("你还未登录！<br/>请点击右上角登录按钮，登陆后登记书本信息");
        }
        else{
            if (book_name && image_url && author && genre) {
                $.ajax({
                    type: "POST",
                    dataType: "json",
                    url: "sysubookex.sinaapp.com/api/v1/books/add",
                    data: {"book_name": book_name, "image_url": image_url,
                        "author" : author, "#genre": genre, "summary":summary, "user_id": user_id },
                    success: function (data) {
                        alert(1);
                        if (data.status == 200) {
                            confirm("成功添加书籍");
                        }
                        else {
                            alert(data.error);
                        }
                    }
                });
            }
            else {
                alert("请确认标 * 的必填项已填满");
            }
        }
    });
});
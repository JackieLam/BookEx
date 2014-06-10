$(function getowners() {
        var isbn = $("#isbn").val().toString();
        var user_id = $("#user_id").val().toString();

        $.ajax({
			type: "delete",
            dataType: "json",
            url: "api/v1/comment",
            data: { "isbn": isbn, "user_id": user_id },
            success: function (data) {
                alert("删除评论成功！");
            }
        });
});
$(function () {
    user = $.getUrlParam("user");

    if (user == undefined) {
        location.href = "/api/v1/users/login";
    }
    else {
        
    }

});
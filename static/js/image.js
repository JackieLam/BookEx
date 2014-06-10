//string name = this.FileUpload1.FileName;//获取上载文件的名称


function uploadImg(name){
    if (name != "")
    {
        path = Server.MapPath("~/Image/");
        this.FileUpload1.PostedFile.SaveAs(path + name);//将文件保存在相应的路径下
        this.Image1.ImageUrl = path + name;//将图片显示在Image控件上
    }
}
function loadFile(obj) {
    let file = obj.files[0];	//선택된 파일 가져오기

    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function () {
        $('#uploadImg').attr("src", reader.result);
    }
}

function uploadFile() {
    let file = $('#chooseFile')[0].files[0]
    let title = $('#fileName').val()
    let form_data = new FormData()

    form_data.append("file_give", file)
    form_data.append("title_give", title)

    $.ajax({
        type: "POST",
        url: "/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
        }
    });
}
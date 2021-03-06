function loadFile(obj) {
    let file = obj.files[0];	//선택된 파일 가져오기

    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function () {
        $('#uploadImg').attr("src", reader.result);
        $('#uploadImg').attr("style", 'display: initial');
    }
}

function uploadFile() {
    let file = $('#chooseFile')[0].files[0];
    let title = $('#fileName').val();
    let form_data = new FormData();

    form_data.append("file_give", file);
    form_data.append("title_give", title);

    $.ajax({
        type: "POST",
        url: "/api/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
        }
    });
}

function clickSearchButton() {
    let name = $('#searchName').val();

    $.ajax({
        type: 'POST',
        url: '/api/search',
        data: {'name_give': name},
        success: function (response) {
            let images = response['images'];
            $('#result').empty();

            for(let i=0; i<images.length; i++) {
                let path = images[i]['path'];
                let pred = images[i]['pred'];
                let temp_html = `<div class="result"><img src="${path}" width="100px"/>
                                <p>${pred}</p></div>`
                $('#result').append(temp_html)
            }
        }
    });
}
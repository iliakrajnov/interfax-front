function news_update(){
    $.getJSON('/api/getNews', function (data){
        data.forEach(function (name){
            console.log('!');
            $('#news-place').append(`<div class="d-md-flex align-items-md-center news" style="min-height: 70px;background: rgb(248,239,226);margin-top: 1%;border-left: 4px solid rgb(0,156,166);">
                                        <h3 style="font-family: 'Proxima Nova';padding-top: 1%;padding-bottom: 1%;padding-right: 2%;padding-left: 2%;width: 90%;">${name}<br /></h3>
                                    </div>`)
        });
        timer = 0;
        $('.news').each(function(){
            setTimeout(()=>$(this).css({animationPlayState: 'running'}), timer);
            timer += 100;
        })
    })
    
}

function confirm_uploading(){
    $('#info-card').css({'animation': 'info-card 1s', 'animation-fill-mode': 'forwards'});
    setTimeout(()=>{
        $('#info-card').css({animation: '', animationFillMode: '', transform: 'translateY(-100%)'});
        $('#info-text').html('Итоговое название');
        $('#confirm').css({'display': 'none'});
        
        $('#tags').css({display: 'block'});
        $('#tags').animate({opacity: 1}, 500);
        tags_random();
        $.get('api/getName', (data)=>{see_res(data)});
    }, 1000);
}


function see_res(name){
    $('#res').html(name);
    $('#res').css({'display': 'inline-flex'});
    
    $('#tags').animate({opacity: 0}, 500);
    $('#tags').css({'display': 'none', 'z-index': '-1'});
    console.log($('#tags').css('display'));
    
    $('#info-card').css({animation: 'info-card 1s reverse', 'animation-fill-mode': 'forwards'})
}

function tags_random(){
    $.getJSON('/api/getTags', function(data){
        data.forEach((name)=>$('#tags-place').append(`<div class="col-auto" style="transform: translateX(${-100 + Math.random() * 200}vw) translateY(${-100 + Math.random() * 200}vw);">
            <h1 class="display-4" style="font-family: 'Proxima Nova Extrabold';color: rgb(0,156,166);">${name}</h1>
        </div>`));
    })
}


function upload_animation(){
    $('#overlay').css({display: 'block'})
    $('#overlay').animate({opacity: 1}, 200)
    $('#upload').animate({backgroundColor: "rgb(0,156,166)",
    color: "rgb(255,255,255)",
    borderColor: "rgb(255,255,255)"}, 200)
}

function drop(){
    $('#overlay').animate({opacity: 0}, 200, ()=>$('#overlay').css({display: 'none'}))
    $('#upload').animate({backgroundColor: "rgb(255,255,255)",
    color: "rgb(0,156,166)",
    borderColor: "rgb(0,156,166)"}, 200)
}


function file_upload(){
    prev = $('#file-input').files;
    console.log(prev);
    $('#file-input').click();
    $('#file-input').on('change', function(){
        $('#form').submit();
    })
}

$('#upload').on('dragenter', function(event){
    event.preventDefault();  
    event.stopPropagation();
    upload_animation();
})
$('#upload').on('dragleave', function(event){
    event.preventDefault();  
    event.stopPropagation();
    drop();
})

$("#upload").on("dragover", function(event) {
    event.preventDefault();  
    event.stopPropagation();
});

$("#upload").on("drop", function(event) {
    event.preventDefault();  
    event.stopPropagation();
    files = event.originalEvent.dataTransfer.files;
    $('#file-input').prop("files", files);
    drop();
    $('#form').submit();
});
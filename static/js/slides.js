function showHideSlides(index){
    var lecture = $(".session:eq(" + index + ")");
    var slides = lecture.find(".slides");
    var id = slides.attr('id');
    if (slides.is(":hidden")){
        slides.html("<iframe class=\"speakerdeck-iframe\" frameborder=\"0\" src=\"//speakerdeck.com/player/" + id + "\" allowfullscreen=\"true\" mozallowfullscreen=\"true\" webkitallowfullscreen=\"true\" style=\"width: 640px; height: 530px;\"></iframe>");
        slides.slideDown("fast",function(){});}
    else {
        slides.slideUp("fast", function(){$(this).hide();});
    }
}
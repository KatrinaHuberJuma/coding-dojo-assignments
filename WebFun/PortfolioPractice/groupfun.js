$(document).ready(function(){
  $("img").click(function(){
    $('h1').after("<b> Don't ya know?</b>");
    $('h1').addClass("crazy");
    $('.top-row').toggle();
  });
});

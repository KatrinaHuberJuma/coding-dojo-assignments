$(document).ready(function(){
  $("img").click(function(){
    $('h1').after("<h1> Don't ya know?</h1>");
    $('h1').addClass("crazy");
    $('.top-row').toggle();
    $('.section-head').hide();
    $( "#serious" ).show( "slow", function() {
    });
  });
});

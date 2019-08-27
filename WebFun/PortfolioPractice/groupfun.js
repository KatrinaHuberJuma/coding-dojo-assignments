$(document).ready(function(){
  $("p").click(function(){
    $('h1').after("<b> Don't ya know?</b>");
    $('h1').addclass("crazy");
  });
});

$(document).ready(function(){
    $.get( "https://pokeapi.co/api/v2/pokemon/?limit=150", function(data){
        // console.log(data)
        var arr = data.results
        for (let i=1; i < arr.length; i++){
            $('body').append("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+i+".png' id='"+arr[i].name+"'>")

        }
    });
});


    $("h1").click(function(){
        console.log("yo")
    });


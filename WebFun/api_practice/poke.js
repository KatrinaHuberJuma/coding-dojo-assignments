$(document).ready(function(){
    $.get( "https://pokeapi.co/api/v2/pokemon/?limit=150", function(data){
        // console.log(data)
        var arr = data.results
        for (let i=1; i < arr.length; i++){
            $('#poke-imgs').append("<img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+i+".png' id='"+arr[i-1].name+"'>")

        }
    });
});


$(document).delegate('img', 'click', function(e) {
    // alert(e.target.id);
    $.get("https://pokeapi.co/api/v2/pokemon/" +e.target.id, function(data){
        // console.log(data);
        var currentTypes = ""
        data.types.forEach(function(element) {
            currentTypes += "<li>" + element.type.name + "</li>";
        });
        $("#current").html( "<h1>"+data.name+"</h1><img src=https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+data.id+".png><h4>Types:</h4><ul> "+currentTypes+"</ul><h4>Height:</h4><p>"+data.height+"</p><h4>weight:</h4><p>"+data.weight+"</p>");
    })
}); 
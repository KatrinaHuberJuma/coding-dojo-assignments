function pushMe(arr, val){
    console.log("pushin' " + val)
    arr[arr.length] = val;
    return arr;
}

function popMe(arr){
    console.log("poppin'")
    var temp = arr[arr.length-1];
    arr.length = arr.length -1
    return temp;
}

var meArray = [1,2,3,4]
console.log("meArray= " + meArray)
pushMe(meArray, 5)
console.log("meArray= " + meArray)
console.log("pop = " + popMe(meArray))
console.log("meArray= " + meArray)


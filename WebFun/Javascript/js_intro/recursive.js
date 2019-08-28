function recursiveSort(arr) {
    console.log('arr passed is', arr);
  
    if(arr.length == 1){
      return arr;
    }
    var max = arr[0];
    var maxidx = 0; //maxidx === index of max
  
    // find maximum value and maxidx
    for(var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
            maxidx = i;
        }
    }
  
    arr[maxidx] = arr[arr.length-1]; // the arr[index of current max] is now the last item
    arr.pop() // removes last thing in arr
    console.log('Maximum found', max); // prints the number that was the index of max
  
    var x = recursiveSort(arr); // recurses! 
    console.log('x is', x);
    x.push(max);
    return x;
}

// output = recursiveSort([5,3,7,1,8,2]);
// console.log('Final Output', output);


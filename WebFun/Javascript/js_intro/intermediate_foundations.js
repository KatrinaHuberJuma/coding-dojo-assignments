var num = 5;
var arr = [1,4,7,2,-3];

// Sigma - Implement function sigma(num) that, given a number, returns the sum of all positive integers up to the given number (inclusive).  Ex: sigma(3) = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

function sigma(num){
    var sum = 0;
    for (let i=0; i<=num; i++){
        sum+=i;
    }
    return sum;
}

// console.log(sigma(5))

// Factorial - Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to the given number (inclusive).  For example, factorial(3) = 6 (or 1*2*3); factorial(5) = 120 (or 1*2*3*4*5).

function factorial(num){
    var sum = 1;
    for (let i=2; i<=num; i++){
        sum*=i;
    }
    return sum;
}

// console.log(factorial(num))

// Fibonacci - Create a function to generate Fibonacci numbers.  In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1.  Your function should accept one argument, an index into the sequence (where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).  
// Examples: 
// fibonacci(0) = 0 (given), 
// fibonacci(1) = 1 (given), 
// fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), f
// ibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), 
// fibonacci(4) = 3 (1+2), 
// fibonacci(5) = 5 (2+3), 
// fibonacci(6) = 8 (3+5), 
// fibonacci(7) = 13 (5+8).  Do this without using recursion first.  If you don't know what a recursion is yet, don't worry as we'll be introducing this concept in Part 2 of this assignment.

function fibonacci(idx){
    
    if (idx===0){
        return 0;
    } else if (idx===1){
        return 1;
    }

    var num1 = 0;
    var num2 = 1;
    for (let i=2; i <=idx; i++){
        if (i%2===0){
            num1 += num2;
            if (i===idx){
                return num1;
            }
        } else {
            num2 += num1;
            if (i===idx){
                return num2;
            }
        }
    }

}

// console.log(fibonacci(num))

// Array: Second-to-Last: Return the second-to-last element of an array. Given [42, true, 4, "Liam", 7], return "Liam".  If array is too short, return null.

function secondToLast(arr){
    if (arr.length-2 >= 0){
        return arr[arr.length-2];
    }
    return "Liam";
}

// console.log(secondToLast(arr));

// Array: Nth-to-Last: Return the element that is N-from-array's-end.  Given ([5,2,3,6,4,9,7],3), return 4.  If the array is too short, return null.

function secondToLast(arr,n){
    if (arr.length-n >= 0){
        return arr[arr.length-n];
    }
    return null;
}

// console.log(secondToLast(arr,3))

// Array: Second-Largest: Return the second-largest element of an array. Given [42,1,4,3.14,7], return 7.  If the array is too short, return null.

// skip, i get the point


// Double Trouble: Create a function that changes a given array to list each existing element twice, retaining original order.  Convert [4, "Ulysses", 42, false] to [4,4, "Ulysses", "Ulysses", 42, 42, false, false].

// skip, i get the point


// ======== PART TWO =========


// Create a function Fib(n) where it returns the nth Fibonacci number.  Use recursion for this.
// Examples: 
// fibonacci(0) = 0 (given), 
// fibonacci(1) = 1 (given), 
// fibonacci(2) = 1 (fib(0)+fib(1), or 0+1), f
// ibonacci(3) = 2 (fib(1) + fib(2)3, or 1+1), 
// fibonacci(4) = 3 (1+2), 
// fibonacci(5) = 5 (2+3), 
// fibonacci(6) = 8 (3+5), 
// fibonacci(7) = 13 (5+8).

// function fib(n, level=0){
    
//     console.log(level, n)

//     if (n===0){
//         return 0;
//     } 
//     if (n===1){
//         return 1;
//     } 
    
    
//     return fib(n-1, level+1)+ fib(n-2, level+1);

// }

function fib(n, level="||"){
    var spacers ="|_  "
    console.log(level + "n= "+ n)

    if (n===0 || n==1){
        console.log("++++++++++++")
        return n;
    } 
    
    return fib(n-1, level+spacers)+ fib(n-2, level+spacers);

}

console.log("the fib of 5 = " + fib(5))

function solve(current_array){
    let firstElement = current_array.shift();
    let lastElement = current_array.pop();
    let finalResult = Number;
    finalResult = firstElement + lastElement;
    console.log(finalResult);
}

// solve([10, 17, 22, 33])
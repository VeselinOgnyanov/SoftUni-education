function solve(lengthOfArray ,currentArray){
    let finalArray = [];
    for (let i = 0; i < lengthOfArray; i++) {
        finalArray.push(currentArray[i]);
    }
    finalArray = finalArray.reverse();
    console.log(finalArray.join(" "));
}

// solve(3, [10, 20, 30, 40, 50])
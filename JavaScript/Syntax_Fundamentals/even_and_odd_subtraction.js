function solve(currentArray){
let oddSum = 0;
let evenSum = 0;
let totalSum = 0;
for (let i = 0; i < currentArray.length; i++) {
    if (currentArray[i] % 2 === 0){
        evenSum += currentArray[i]
    } else {
        oddSum += currentArray[i]
    }
}
totalSum = evenSum - oddSum

console.log(totalSum)
}

// solve([2,4,6,8,10])
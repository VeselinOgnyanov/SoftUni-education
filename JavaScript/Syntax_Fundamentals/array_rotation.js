function solve(firstArray, rotationNumber) {
    let lengthOfArray = firstArray.length
    let realRotationsNumber
    if (rotationNumber > lengthOfArray){
        realRotationsNumber =  rotationNumber % lengthOfArray
    } else {
        realRotationsNumber = rotationNumber
    }
    for (let i = 0; i < realRotationsNumber; i++) {
        firstElement = firstArray.shift()
        firstArray.push(firstElement)
    }
console.log(firstArray.join(" "))
}

// solve([51, 47, 32, 61, 21], 2)
// solve([32, 21, 61, 1], 4)
// solve([2, 4, 15, 31], 5)
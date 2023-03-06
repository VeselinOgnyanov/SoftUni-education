function solve(firstArray, stepNumber) {
    let arrayToBeDisplayed = []

    for (let i = 0; i < firstArray.length; i += stepNumber) {
        arrayToBeDisplayed.push(firstArray[i])
    }

    return arrayToBeDisplayed;
}

// solve(['5', '20', '31', '4', '20'], 2)



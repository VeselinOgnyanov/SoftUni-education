function solve(currentNumber) {
    let finalSum = 0
    let currentNumberToString = currentNumber.toString()
    let hasSameNumbers = true
    let transformedToNumber
    let arrayNumbers = []
    let currentNumberToCompare

    for (let i = 0; i < currentNumberToString.length; i++) {
        transformedToNumber = Number(currentNumberToString[i])
        finalSum += transformedToNumber
        arrayNumbers.push(transformedToNumber)
    }

    currentNumberToCompare = arrayNumbers[0]
    for (let i = 0; i < arrayNumbers.length; i++) {
        if (currentNumberToCompare != arrayNumbers[i] ){
            hasSameNumbers = false
            break
        }
        currentNumberToCompare = arrayNumbers[i]
    }

    console.log(hasSameNumbers)
    console.log(finalSum)

}

// solve(1234)
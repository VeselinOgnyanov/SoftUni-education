function solve(numberArray) {
    let sortedList = numberArray.sort((a, b) => a - b)
    let finalList = []
    let firstNumber
    let secondNumber

    while (sortedList.length != 0) {

        firstNumber = sortedList.shift()
        secondNumber = sortedList.pop()
        finalList.push(firstNumber)
        finalList.push(secondNumber)
    }
    return finalList
}

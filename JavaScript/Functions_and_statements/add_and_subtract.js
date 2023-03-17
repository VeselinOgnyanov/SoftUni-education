function addAndSubtract(...params) {
    let [numOne, numTwo, numThree] = params
    function sum(firstNum, secondNum) {
        let result = firstNum + secondNum
        return result
    }
    function subtract(sumSum, toBeSubtracted) { 
        let result = sumSum- toBeSubtracted
        return result
    }
    let result = subtract(sum(numOne, numTwo), numThree)
    console.log(result)
}

addAndSubtract(23, 6, 10)
addAndSubtract(1, 17, 30)
addAndSubtract(42, 58, 100)
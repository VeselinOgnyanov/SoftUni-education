function solve(firstNumber, secondNumber, firstString){
    if (firstString === "+") {                      
        result = firstNumber + secondNumber
        console.log(result)
    }
    else if (firstString === "-") {
        result = firstNumber - secondNumber
        console.log(result)
    }
    else if (firstString === "*") {
        result = firstNumber * secondNumber
        console.log(result)
    }
    else if (firstString === "/") {
        result = firstNumber / secondNumber
        console.log(result)
    }
    else if (firstString === "%") {
        result = firstNumber % secondNumber
        console.log(result)
    }
    else {
        result = firstNumber ** secondNumber
        console.log(result)
    }
}

// solve(1, 3, "/")
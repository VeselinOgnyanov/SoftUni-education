function simpleCalculator(firstNumber, secondNumber, operation) {

    const multiplyFunc = (a, b) => a * b;
    const divideFunc = (a, b) => a / b;
    const addFunc = (a, b) => a + b;
    const subtractFunc = (a, b) => a - b;

    const calculatingObject = {
        multiply: multiplyFunc,
        divide: divideFunc,
        add: addFunc,
        subtract: subtractFunc,
    }

    return calculatingObject[operation](firstNumber, secondNumber)
}

console.log(simpleCalculator(
    5,
    5,
    'multiply'))
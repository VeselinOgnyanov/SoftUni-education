function subtract() {
    const firstNumber = document.getElementById("firstNumber");
    const secondNumber = document.getElementById("secondNumber");
    const resultDiv = document.getElementById("result")

    let firstNumberValue = Number(firstNumber.value)
    let secondNumberValue = Number(secondNumber.value)
    let result = firstNumberValue - secondNumberValue
    resultDiv.textContent = result


}
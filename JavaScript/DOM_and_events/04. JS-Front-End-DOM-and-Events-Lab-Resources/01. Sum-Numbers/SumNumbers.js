function calc() {
    // TODO: sum = num1 + num2
    const InputOne = document.getElementById("num1")
    const InputTwo = document.getElementById("num2")
    const sumInput = document.getElementById("sum")

    let result = Number(InputOne.value) + Number(InputTwo.value)
    sumInput.value = result
}

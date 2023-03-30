function sumTable() {
    const tableBody = Array.from(document.querySelectorAll("tr > td:nth-child(even)"))
    const resultTab = document.getElementById("sum")

let result = 0
    for (let index = 0; index < tableBody.length - 1; index++) {
        let currentValue = tableBody[index].textContent
        currentValue = Number(currentValue)
        result += currentValue
    }

    resultTab.textContent = result.toFixed(2)
}
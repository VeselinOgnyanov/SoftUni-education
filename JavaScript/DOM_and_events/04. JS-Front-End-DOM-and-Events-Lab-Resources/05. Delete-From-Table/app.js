function deleteByEmail() {
    const input = document.querySelector(`input[name = "email"]`);
    const resultedText = document.getElementById("result")
    const evenTd = Array.from(document.querySelectorAll("td:nth-child(even)"))


    let inputValue = input.value
    let foundedValue = evenTd.find(name => name.textContent === inputValue)
    if (foundedValue) {
        foundedValue.parentElement.remove()
        resultedText.textContent = "Deleted."
    } else {
        resultedText.textContent = "Not found."
    }
}
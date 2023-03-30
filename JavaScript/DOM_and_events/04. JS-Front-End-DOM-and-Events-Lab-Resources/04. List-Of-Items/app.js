function addItem() {
    const input = document.getElementById("newItemText")
    const ul = document.getElementById("items")

    let newLi = document.createElement("li")
    let inputedText = input.value
    newLi.textContent = inputedText
    ul.appendChild(newLi)
}
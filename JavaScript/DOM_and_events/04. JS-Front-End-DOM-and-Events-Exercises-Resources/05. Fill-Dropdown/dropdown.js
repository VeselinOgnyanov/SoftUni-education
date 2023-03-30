function addItem() {
    const textField = document.getElementById("newItemText")
    const valueField = document.getElementById("newItemValue")
    const dropdownField = document.getElementById("menu")
    const newOption = document.createElement("option")

    let currentText = textField.value
    let currentValue = valueField.value
    newOption.textContent = currentText
    newOption.value = currentValue
    
    dropdownField.appendChild(newOption)

    textField.value = ""
    valueField.value = ""


}
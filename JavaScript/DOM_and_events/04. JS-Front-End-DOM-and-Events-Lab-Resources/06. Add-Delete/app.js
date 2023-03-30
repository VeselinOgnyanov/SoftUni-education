function addItem() {
    const input = document.getElementById("newItemText")
    const ul = document.getElementById("items")
    const newAnchor = document.createElement("a")
    

    let newLi = document.createElement("li")
    let inputedText = input.value
    newLi.textContent = inputedText
    ul.appendChild(newLi)

    newAnchor.textContent = "[Delete]"
    newAnchor.href = "#"
    newAnchor.addEventListener("click", handlerAnchor)
    newLi.appendChild(newAnchor)

    function handlerAnchor(e){
        // console.log(newLi)
        newLi.remove()
    }
}
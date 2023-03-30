function toggle() {
    const buttonElement = Array.from(document.getElementsByClassName("button"))[0]
    const extraDiv = document.getElementById("extra")
    let currentState = buttonElement.textContent 
    

    if (currentState === "Less"){
        buttonElement.textContent = "More"
        extraDiv.style.display = "none"
    } else {
        buttonElement.textContent = "Less"
        extraDiv.style.display = "block"
    }
}
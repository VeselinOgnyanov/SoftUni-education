function focused() {
    const allInputs = Array.from(document.getElementsByTagName("input"))


    for (const input of allInputs) {
        input.addEventListener("focus", focusHandler)
        input.addEventListener("blur", blurHandler )
    }

    function focusHandler(event) {
        const currentInput = event.target;
        let currentParent = currentInput.parentNode
        currentParent.classList.add("focused")
        console.log(currentParent)
    }

    function blurHandler(event){
        const currentInput = event.target;
        let currentParent = currentInput.parentNode
        if (currentParent.classList.contains("focused")){
            currentParent.classList.remove("focused")
        }
    }
    

}
 
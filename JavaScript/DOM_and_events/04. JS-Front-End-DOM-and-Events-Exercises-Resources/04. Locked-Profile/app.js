function lockedProfile() {
    const allButtons = Array.from(document.getElementsByTagName("button"))


    for (const currentButton of allButtons) {
        currentButton.addEventListener("click", clickHandler)
    }


    function clickHandler(e) {
        let currentButton = e.currentTarget
        let currentParentNode = currentButton.parentNode
        let allChildren = Array.from(currentParentNode.children)
        let currentDivToAdd = allChildren[9]
        let radioButtonValue = allChildren[4].checked                       /*unlock = true, lock = false*/


        if (radioButtonValue) {
            if (currentButton.textContent === "Show more") {
                currentDivToAdd.style.display = "block"
                currentButton.textContent = "Hide it"
            } else {
                currentDivToAdd.style.display = "none"
                currentButton.textContent = "Show more"
            }
        }

    }

}
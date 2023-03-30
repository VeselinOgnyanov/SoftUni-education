function extractText() {
    const elementsInList = Array.from(document.querySelectorAll("ul > li"))             //(#items > li)
    const textArea = document.getElementById("result")


    
    // textArea.textContent += "test"
    console.log(elementsInList)
    for (const element of elementsInList) {
        let currentText = element.textContent
        textArea.textContent += currentText + "\n"
    }
}
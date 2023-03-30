function solve() {
    const textArea = document.getElementById("input")
    const button = document.getElementById("formatItBtn")
    const divToprint = document.getElementById("output")

    
    let splittedText = String(textArea.value).split(".")
    let substring = ""
    splittedText.pop()

    while (splittedText.length > 0) {
        let splicedText = splittedText.splice(0, 3)
        substring = splicedText.join(" ")
        let newParag = document.createElement("p")
        if (substring[0] === " ") {
            newParag.textContent = substring.substring(1) + "."
        } else (
            newParag.textContent = substring + "."
        )
        divToprint.appendChild(newParag)
    }
}

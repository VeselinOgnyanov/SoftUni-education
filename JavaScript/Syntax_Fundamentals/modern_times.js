function solve(currentString) {
    let currentList = currentString.split(" ")
    let hashTagList = []
    let newString
    let isValid = false

    for (const currentWord of currentList) {
        if (currentWord.startsWith("#") && currentWord.length > 1) {
            newString = currentWord.slice(1, currentWord.length)
            hashTagList.push(newString)
        }
    }
    for (const iterator of hashTagList) {
        for (const currentChar of iterator) {
            let result = currentChar.charCodeAt()
            if ((result >= 97 && result <= 122) || (result >= 65 && result <= 90)) {
                isValid = true
            } else {
                break
            }
        }
        if (isValid) {
            console.log(iterator)
        }
        isValid = false
    }
}

// solve('Nowadays everyone uses # to tag a #special word in ###socialMedia')
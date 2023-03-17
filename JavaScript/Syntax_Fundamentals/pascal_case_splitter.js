function solve(sentence) {
    let currentString = ""
    let currentList = []
    let counter = 0
    let result = ""

    for (const iterator of sentence) {
        let currentLetter = iterator.charCodeAt(0)
        if (currentLetter >= 65 && currentLetter <= 90) {
            if (currentString.length > 0) {
                currentString += ", " + iterator
            } else {
                currentString += iterator
            }
            
        } else {
            currentString += iterator
        }
    }
    
    console.log(currentString)
}

solve("SplitMeIfYouCanHaHaYouCantOrYouCan")
solve("HoldTheDoor")
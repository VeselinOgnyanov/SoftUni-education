function solve(sentence) {
    let currentString = ""
    let currentList = []
    let counter = 0
    let result = ""

    for (const iterator of sentence) {
        let currentLetter = iterator.charCodeAt(0)
        if (currentLetter >= 65 && currentLetter <= 90) {
            counter += 1
            if(counter === 2){
                currentList.push(currentString)
                currentString = ""
                counter = 1
            }
            currentString += iterator
        } else {
            currentString += iterator
        }
    }
result = currentList.join(", ")
console.log(result)
}

// solve("SplitMeIfYouCanHaHaYouCantOrYouCan")
solve("HoldTheDoor")
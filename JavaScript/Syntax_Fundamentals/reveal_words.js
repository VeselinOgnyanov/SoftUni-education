function solve(wantedWord, currentString) {
    let wantedWordList = wantedWord.split(", ")
    let stringList = currentString.split(" ")
    let finalString
    for (const currentElement of stringList) {
        if (currentElement.startsWith("*")){
            let wantedWordLength = currentElement.length
            for (const currentWordInWantedWordList of wantedWordList) {
                let currentWordInWantedWordListLength = currentWordInWantedWordList.length
                if (currentWordInWantedWordListLength === wantedWordLength){
                    finalString = currentString.replace(currentElement, currentWordInWantedWordList)
                    currentString = finalString
                }
            }
        }
    }
    console.log(finalString)
}


// solve('great, learning', 'softuni is ***** place for ******** new programming languages')
function solve(currentString, wordToBeReplaced) {
    censoredText = currentString
    while (censoredText.includes(wordToBeReplaced)) {
        censoredText = censoredText.replace(wordToBeReplaced, "*".repeat(wordToBeReplaced.length))
    }

    console.log(censoredText)
}

// solve('A small sentence with some words ', 'small')
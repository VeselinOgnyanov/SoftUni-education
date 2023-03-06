function solve(wordToSearch, sentenceForSearching) {
    let wordIsFound = false
    sentenceForSearching = sentenceForSearching.split(" ")
    for (const iterator of sentenceForSearching) {
        let toLower = iterator.toLowerCase()
        if (wordToSearch === toLower) {
            console.log(wordToSearch)
            wordIsFound = true
            break
        }
    }
    if (wordIsFound === false) {
        console.log(`${wordToSearch} not found!`)
    }

}

// solve('javascript', 'JavaScript is the best programming language')
// solve('python',
// 'JavaScript is the best programming language')
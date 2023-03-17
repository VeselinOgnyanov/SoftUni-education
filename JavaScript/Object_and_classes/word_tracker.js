function solve(input) {
    let counts = {}
    let otherWords = []
    let wantedWords = input[0]

    let arrayWantedWords = wantedWords.split(" ")
    for (const element of arrayWantedWords) {
        counts[element] = 0
    }

    for (let i = 1; i < input.length; i++) {
        otherWords.push(input[i])
    }

    for (const property in counts) {
        otherWords.forEach(element => {
            if (element === property) {
                counts[property] += 1
            }
        });
    }

    let sortedWords = Object.entries(counts)
        .sort((wordA, wordB) => {
            let [_nameA, countA] = wordA
            let [_nameB, countB] = wordB

            return countB - countA
        })

    for (const iterator of sortedWords) {
        console.log(`${iterator[0]} - ${iterator[1]}`)
    }

}

solve([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
])

solve([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'])
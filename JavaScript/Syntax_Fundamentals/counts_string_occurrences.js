function solve(currentText, wordToBeSearched) {
    arrayToWorkOn = currentText.split(" ");
    let counterOfOccurances = 0;
    for (const currentElement of arrayToWorkOn) {
        if (currentElement === wordToBeSearched) {
            counterOfOccurances += 1;
        }
    }
    console.log(counterOfOccurances)
}

// solve('This is a word and it also is a sentence',
// 'is')
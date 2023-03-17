function negativeChecker(...params) {
    let [numOne, numTwo, numThree] = params
    let counter = 0
    if (numOne < 0) {
        counter += 1
    }
    if (numTwo < 0) {
        counter += 1
    }
    if (numThree < 0) {
        counter += 1
    }
    if (counter % 2 === 1) {
        console.log("Negative")
    } else {
        console.log("Positive")
    }
}

negativeChecker(1, 2, -3)

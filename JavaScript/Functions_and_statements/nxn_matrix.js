function matrix(number) {
    for (let i = 0; i < number; i++) {
        numString = String(number) + " "
        console.log(String(numString.repeat(number)))
    }
}

matrix(7)
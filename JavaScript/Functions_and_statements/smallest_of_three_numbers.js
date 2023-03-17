function smallest(...params) {
    let arrayNumbers = []
    for (const iterator of params) {
        arrayNumbers.push(iterator)
    }    

    // console.log(arrayNumbers)
    let smallestNumber = Math.min(...arrayNumbers)
    console.log(smallestNumber)
}

smallest(22, 3 , 42)
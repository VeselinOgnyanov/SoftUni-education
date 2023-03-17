function oddAndEvenSum(number) {
    let oddArray = []
    let evenArray = []
    let sumOfEvenArray = 0
    let sumOfOddArray = 0

    number = String(number)
    // console.log(typeof(number))
    for (let i = 0; i < number.length; i++) {
        const element = number[i];
        // console.log(element)
        if (element % 2 === 0) {
            evenArray.push(element)
        } else {
            oddArray.push(element)
        }
    }
    for (const iterator of oddArray) {
        currentNum = Number(iterator)
        // console.log(currentNum)
        sumOfOddArray += currentNum
    }
    for (const iterator of evenArray) {
        currentNum = Number(iterator)
        sumOfEvenArray += currentNum
    }
    // console.log(evenArray)
    // console.log(oddArray)
    // console.log(sumOfEvenArray)
    // console.log(sumOfOddArray)
    console.log(`Odd sum = ${sumOfOddArray}, Even sum = ${sumOfEvenArray}`)
}

oddAndEvenSum(3495892137259234)
function solve(currentNumber) {
    let finalSum = 0
    let currentNumberToString = currentNumber.toString()
    
    for (let i = 0; i < currentNumberToString.length; i++) {
       let transformedToNumber = Number(currentNumberToString[i])
       finalSum += transformedToNumber
    }

    console.log(finalSum)

}

solve(245678)	
solve(97561)	
solve(543)

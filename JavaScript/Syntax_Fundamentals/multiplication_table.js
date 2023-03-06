function solve (currentNumber){
    let currentResult;
    for (let i = 1; i < 11; i++) {
        currentResult = currentNumber * i;
        console.log(`${currentNumber} X ${i} = ${currentResult}`)
    }
}

// solve(5)
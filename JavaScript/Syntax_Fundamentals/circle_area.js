function solve(currentInput){
    let result;
    let currentType = typeof(currentInput)
    if (currentType === "number"){
            result = (currentInput ** 2) * Math.PI
            console.log(result.toFixed(2))
    } else{
        console.log(`We can not calculate the circle area, because we receive a ${currentType}.`)
    }
}

// solve(5)
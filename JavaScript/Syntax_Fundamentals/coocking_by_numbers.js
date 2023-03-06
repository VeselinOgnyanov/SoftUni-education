function solve(numberToUse, ...otherOperations) {
    let startingPoint = numberToUse

    for (const currentOperation of otherOperations) {
        if (currentOperation === "chop") {
            currentEvaluation = startingPoint / 2
            startingPoint = currentEvaluation
            console.log(startingPoint)
        }
        else if (currentOperation === "dice") {
            currentEvaluation = Math.sqrt(startingPoint)
            startingPoint = currentEvaluation
            console.log(startingPoint)
        }
        else if (currentOperation === "spice") {
            currentEvaluation = startingPoint + 1
            startingPoint = currentEvaluation
            console.log(startingPoint)
        }
        else if (currentOperation === "bake") {
            currentEvaluation = startingPoint * 3
            startingPoint = currentEvaluation
            console.log(startingPoint)
        }
        else {            //fillet 
            currentEvaluation = startingPoint - (startingPoint * 0.2)
            startingPoint = currentEvaluation
            console.log(startingPoint)
        }
    }

}

// solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')
// solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')

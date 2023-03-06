function solve(firstChar, secondChar, thirdChar){
    let finalArray = []
    finalArray.unshift(firstChar)
    finalArray.unshift(secondChar)
    finalArray.unshift(thirdChar)
    finalString = finalArray.join(" ")
    console.log(finalString)
}

// solve("a", "b", "c")
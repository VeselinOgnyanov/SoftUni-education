function loadingBar(param) {
    let currentPercent = 0
    let percentaceSymbol = "%"
    let dotString = "."
    currentPercent = Math.ceil(param / 10)
    if (param === 100) {
        console.log(`100% Complete`)
    } else {
        console.log(`${param}% [${percentaceSymbol.repeat(currentPercent) + dotString.repeat(10 - currentPercent)}]`)
        console.log(`Still loading...`)
    }

}

loadingBar(60)



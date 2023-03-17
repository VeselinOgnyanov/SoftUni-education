function towns(input) {
    currentTown = {}

    for (const line of input) {
        // console.log(line)
        let splittedArray = line.split(" | ")
        // console.log(splittedArray)
        let [town, latitude, longitude] = splittedArray
        currentTown.town = town
        currentTown.latitude = (Number(latitude)).toFixed(2)
        currentTown.longitude = (Number(longitude)).toFixed(2)
        console.log(currentTown)
    }

    // console.log(currentTown)
}

towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625'])
function solve(input) {
    let piecesObject = {}

    let numberOfpieces = input.shift()
    for (let index = 0; index < numberOfpieces; index++) {
        let currentPieceLine = input.shift()
        let splittedCurrentPieceLine = currentPieceLine.split("|")
        let [piece, composer, key] = splittedCurrentPieceLine
        piecesObject[piece] = { composer: composer, key: key }
    }
    while (input[0] !== "Stop") {
        let line = input.shift()
        line = line.split("|")
        if (line[0] === "Add") {
            if (piecesObject.hasOwnProperty(line[1])) {
                console.log(`${line[1]} is already in the collection!`)
            } else {
                piecesObject[line[1]] = { composer: line[2], key: line[3] }
                console.log(`${line[1]} by ${line[2]} in ${line[3]} added to the collection!`)
            }
        } else if (line[0] === "Remove") {
            if (piecesObject.hasOwnProperty(line[1])) {
                delete piecesObject[line[1]]
                console.log(`Successfully removed ${line[1]}!`)
            } else {
                console.log(`Invalid operation! ${line[1]} does not exist in the collection.`)
            }
        } else if (line[0] === "ChangeKey") {
            if (piecesObject.hasOwnProperty(line[1])) {
                piecesObject[line[1]].key = line[2]
                console.log(`Changed the key of ${line[1]} to ${line[2]}!`)
            } else {
                console.log(`Invalid operation! ${line[1]} does not exist in the collection.`)
            }
        }
    }

    let entries = Object.entries(piecesObject)
    for (const iterator of entries) {
        console.log(`${iterator[0]} -> Composer: ${iterator[1].composer}, Key: ${iterator[1].key}`)
    }
}


solve([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'
]);
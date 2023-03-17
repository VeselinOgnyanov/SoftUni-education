function solve(jsonString) {
    let person = JSON.parse(jsonString)
    personItem = Object.entries(person)
    for (const [key, value] of personItem) {
        console.log(`${key}: ${value}`)
    }

}

solve('{"name": "George", "age": 40, "town": "Sofia"}')
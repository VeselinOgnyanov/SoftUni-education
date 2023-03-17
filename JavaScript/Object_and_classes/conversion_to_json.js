function solve(name	, lastName, hairColor) {
    let personProps = {
        name,
        lastName,
        hairColor,
    }

    let personJSON = JSON.stringify(personProps)
    console.log(personJSON)
}


solve('George', 'Jones', 'Brown')
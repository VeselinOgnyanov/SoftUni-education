function employees(input) {
    employeesObject = {}
    for (const element of input) {
        let lengthOfPerson = element.length
        employeesObject[element] = lengthOfPerson
    }

    for (const [key, value] of Object.entries(employeesObject)) {
        console.log(`Name: ${key} -- Personal Number: ${value}`)
    }
}



employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])
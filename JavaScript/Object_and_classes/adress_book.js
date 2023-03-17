function adressBook(input) {
    let name = ""
    let adress = ""
    let addressBookObject = {}

    for (const line of input) {
        [name, adress] = line.split(":")
        addressBookObject[name] = adress
    }

    sortedKeys = Object.keys(addressBookObject)
    .sort((nameA, nameB)=>(nameA.localeCompare(nameB)))

    for (const key of sortedKeys) {
        console.log(`${key} -> ${addressBookObject[key]}`)
    }


    // console.log(addressBookObject)
    // console.log(sortedKeys)

}

adressBook(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd'])
function phoneBook(param) {
    let phoneBookObject = {}

    for (const line of param) {
        let [key, value] = line.split(" ")
        phoneBookObject[key] = value
    }

for (const key in phoneBookObject) {
    console.log(`${key} -> ${phoneBookObject[key]}`)
}
}



phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344'])
function palindromeIntegers(integer) {
    for (const currentNumber of integer) {
        StringNnumber = String(currentNumber)
        let forwardString = ""
        let backwordString = ""
        for (let i = 0; i < StringNnumber.length; i++) {
            forwardString += StringNnumber[i]
        }
        for (let i = StringNnumber.length - 1; i >= 0 ; i--) {
            backwordString += StringNnumber[i]
        }   
        if (forwardString === backwordString){
            console.log("true")
        } else {
            console.log("false")
        }
    }
        
}

palindromeIntegers([123,323,421,121])
palindromeIntegers([32,2,232,1010])

let a = "äaa"
let b = "äaa"
console.log(a === b)
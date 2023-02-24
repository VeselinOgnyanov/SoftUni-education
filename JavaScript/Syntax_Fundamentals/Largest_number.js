function largestNumber(numberOne, numberTwo, numberThree){
let result = Number.MIN_SAFE_INTEGER
if (numberOne > result){
    result = numberOne
}
if (numberTwo > result){
    result = numberTwo
}
if (numberThree > result){
    result = numberThree
}
console.log(`The largest number is ${result}.`)
}

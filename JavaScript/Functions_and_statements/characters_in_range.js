function charsInRange(charOne, charTwo) {
    firstNum = charOne.charCodeAt(0)
    secondNum = charTwo.charCodeAt(0)
   let newArray = []

    if (firstNum > secondNum) {
        for (let i = secondNum + 1; i < firstNum; i++) {
            newArray.push(String.fromCharCode(i))
            
        }
    } else {
        for (let i = firstNum + 1; i < secondNum; i++) {
            newArray.push(String.fromCharCode(i))
        }
    }
    console.log((newArray.join(" ")));
}

charsInRange('a',
'd')
charsInRange('#',
':')
charsInRange('C',
'#')
function solve(startNumber, endNumber) {
    let listOfNumbers = [];
    let totalSum = 0;
    for (let i = startNumber; i <= endNumber; i++) {
        listOfNumbers.push(i);
    }
    for (let i = 0; i < listOfNumbers.length; i++) {
        totalSum += listOfNumbers[i];
    }
    console.log(listOfNumbers.join(" "))
    console.log(`Sum: ${totalSum}`)
}

solve(5, 10)
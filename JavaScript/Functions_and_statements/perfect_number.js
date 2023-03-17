

function perfectNnumber(number) {
    let divisors = []
    let result = 0

    for (let i = 1; i < number; i++){
        if (number % i === 0){
            divisors.push(i)
        }
    }

    for (const i of divisors) {
        currentNumber = Number(i)
        result += currentNumber
    }

    if (result === number){
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.")
    }
}


perfectNnumber(6)
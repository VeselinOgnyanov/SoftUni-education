function solve(typeOfDay, ageOfThePerson) {
    let currentPriceOfTicket;
    let invalidAge = false;
    switch (typeOfDay) {
        case 'Weekday':
            if ((0 <= ageOfThePerson && ageOfThePerson <= 18) || (64 < ageOfThePerson && ageOfThePerson <= 122)) {
                currentPriceOfTicket = 12
            } else if (18 < ageOfThePerson && ageOfThePerson <= 64) {
                currentPriceOfTicket = 18
            } else {
                invalidAge = true
                break;
            }
            break;
        case 'Weekend':
            if ((0 <= ageOfThePerson && ageOfThePerson <= 18) || (64 < ageOfThePerson && ageOfThePerson <= 122)) {
                currentPriceOfTicket = 15
            } else if (18 < ageOfThePerson && ageOfThePerson <= 64) {
                currentPriceOfTicket = 20
            } else {
                invalidAge = true
                break;
            }
            break;
        case 'Holiday':
            if (0 <= ageOfThePerson && ageOfThePerson <= 18) {
                currentPriceOfTicket = 5
            } else if (18 < ageOfThePerson && ageOfThePerson <= 64) {
                currentPriceOfTicket = 12
            } else if (64 < ageOfThePerson && ageOfThePerson <= 122) {
                currentPriceOfTicket = 10
            } else {
                invalidAge = true
                break;
            }
            break;
    }
    if (invalidAge === true) {
        console.log("Error!")
    } else {
        console.log(`${currentPriceOfTicket}$`)
    }
}

// solve('Weekend', 42)
function solve(numberOfPersons, typeOfTicket, dayOfStaying) {
    let finalPrice = 0;
    let currentTicketPrice = 0;
    if (dayOfStaying === "Friday") {
        if (typeOfTicket === "Students") {
            currentTicketPrice = 8.45;
        } else if (typeOfTicket === "Business") {
            currentTicketPrice = 10.90
        } else {     //Regular
            currentTicketPrice = 15
        }

    } else if (dayOfStaying === "Saturday") {
        if (typeOfTicket === "Students") {
            currentTicketPrice = 9.80;
        } else if (typeOfTicket === "Business") {
            currentTicketPrice = 15.60
        } else {     //Regular
            currentTicketPrice = 20
        }

        //dayOfStaying === "Sunday"

    } else {
        if (typeOfTicket === "Students") {
            currentTicketPrice = 10.46;
        } else if (typeOfTicket === "Business") {
            currentTicketPrice = 16
        } else {     //Regular
            currentTicketPrice = 22.50
        }
    }

    if (typeOfTicket === "Students") {
        if (numberOfPersons >= 30) {
            finalPrice = (currentTicketPrice * numberOfPersons) * 0.85
        }
        else {
            finalPrice = currentTicketPrice * numberOfPersons
        }
    } else if (typeOfTicket === "Business") {
        if (numberOfPersons >= 100) {
            numberOfPersons -= 10
            finalPrice = currentTicketPrice * numberOfPersons
        }
        else {
            finalPrice = currentTicketPrice * numberOfPersons
        }
        //Regular
    } else {
        if ((numberOfPersons >= 10) && (numberOfPersons <= 20)) {
            finalPrice = (currentTicketPrice * numberOfPersons) * 0.95
        } else {
            finalPrice = currentTicketPrice * numberOfPersons
        }
    }

    console.log(`Total price: ${finalPrice.toFixed(2)}`)
}

// solve(40,
//     "Regular",
//     "Saturday")
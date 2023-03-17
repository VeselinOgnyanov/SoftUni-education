function piccolo(input) {
    carsArray = []
    
    for (const iterator of input) {
        let [direction, plate] = iterator.split(", ")
        if (direction === "IN") {
           if (!(carsArray.includes(plate))) {
            carsArray.push(plate)
           }
        } else {
            if ((carsArray.includes(plate))) {
                wantedIndex = carsArray.indexOf(plate)
                carsArray.splice(wantedIndex, 1)
               }
        }
    }
    if (carsArray.length > 0 ) {
        sortedList = carsArray.sort((a,b ) =>a.localeCompare(b))
        for (const iterator of sortedList) {
            console.log(iterator)
        }
    } else {
        console.log("Parking Lot is Empty")
    }
  
}


piccolo(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU'])

piccolo(
    ['IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'OUT, CA1234TA']
)
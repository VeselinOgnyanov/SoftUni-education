function solve(speed, area) {
    let speedDifference = 0
    let overSpeed = false
    let status

    switch (area) {
        case "motorway":
            speedZone = 130
            if (speed <= speedZone) {
                console.log(`Driving ${speed} km/h in a ${speedZone} zone`)
            } else {
                speedDifference = speed - speedZone
                overSpeed = true
            }

            break;
        case "interstate":
            speedZone = 90
            if (speed <= 90) {
                console.log(`Driving ${speed} km/h in a ${speedZone} zone`)
            } else {
                speedDifference = speed - speedZone
                overSpeed = true
            }

            break;
        case "city":
            speedZone = 50
            if (speed <= speedZone) {
                console.log(`Driving ${speed} km/h in a ${speedZone} zone`)
            } else {
                speedDifference = speed - speedZone
                overSpeed = true
            }

            break;
        case "residential":
            speedZone = 20
            if (speed <= speedZone) {
                console.log(`Driving ${speed} km/h in a ${speedZone} zone`)
            } else {
                speedDifference = speed - speedZone
                overSpeed = true
            }
            break;
    }

    if (overSpeed) {
        if (speedDifference <= 20) {
            status = "speeding"
        } else if (speedDifference <= 40) {
            status = "excessive speeding"
        } else {
            status = "reckless driving"
        }
        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedZone} - ${status} `
        )
    }
}

// solve(250, 'city')
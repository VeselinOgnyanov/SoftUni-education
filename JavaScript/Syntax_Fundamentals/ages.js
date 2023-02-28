function solve(current_age) {
    if ((current_age >= 0) && (current_age <= 2)) {
        console.log("baby")
    } else if ((current_age >= 3) && (current_age <= 13)) {
        console.log("child")
    } else if ((current_age >= 14) && (current_age <= 19)) {
        console.log("teenager")
    } else if ((current_age >= 20) && (current_age <= 65)) {
        console.log("adult")
    } else if (current_age >= 66){
        console.log("elder")
    } else {
        console.log("out of bounds")
    }
}

// solve("-15")
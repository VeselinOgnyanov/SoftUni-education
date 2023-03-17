function passValidator(passToCheck) {

    let passIsValid = true
    passToCheck = String(passToCheck.toLowerCase())
    if ((passToCheck.length < 6) || (passToCheck.length > 10)) {
        console.log("Password must be between 6 and 10 characters")
        passIsValid = false
    }

    for (let i = 0; i < passToCheck.length; i++) {
        let currentSymbol = passToCheck[i];
        if (!((currentSymbol.charCodeAt(0) >= 48 && currentSymbol.charCodeAt(0) <= 57) || ((currentSymbol.charCodeAt(0) >= 97) && (currentSymbol.charCodeAt(0) <= 122)))) {
            console.log("Password must consist only of letters and digits")
            passIsValid = false
            break
        }
    }


        let counter = 0
        for (let i = 0; i < passToCheck.length; i++) {
            let currentSymbol = Number(passToCheck[i]);
            if (Number.isInteger(currentSymbol)) {
                counter += 1
            }
        }
        if (counter < 2) {
            console.log("Password must have at least 2 digits")
            passIsValid = false
        }

        if (passIsValid) {
            console.log("Password is valid")

        }

    }


    // passValidator('logIn')
    passValidator('MyPass123')
    // passValidator('Pa$s$s')

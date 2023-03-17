function mathPower(...params) {
    let [number, power] = params
    let result = 0 

    for (let i = 1; i < power; i++) {
        if (result === 0){
            result = number * number;
        } else {
            result = result * number
        }
    }

    console.log(result)
}

mathPower(2, 8)
mathPower(3, 4)
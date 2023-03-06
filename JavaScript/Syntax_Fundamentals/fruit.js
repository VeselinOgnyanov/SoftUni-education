function solve (fruitToBuy, weightInGrams, pricePerKilo){
    let weightInKilograms = weightInGrams / 1000
    let totalSum = pricePerKilo * weightInKilograms


    console.log(`I need $${totalSum.toFixed(2)} to buy ${weightInKilograms.toFixed(2)} kilograms ${fruitToBuy}.`)
}

// solve('orange', 2500, 1.80)
function storeProvisions(firstArray, secondArray) {
    let totalProductsObject = {}

    for (let i = 0; i < firstArray.length - 1; i++) {
        if (i % 2 === 0) {
            totalProductsObject[firstArray[i]] = Number(firstArray[i + 1])
        }
    }

    for (let i = 0; i < secondArray.length - 1; i++) {
        if (i % 2 === 0) {
            if (!(secondArray[i] in totalProductsObject)) {
                totalProductsObject[secondArray[i]] = Number(secondArray[i + 1])
            } else {
                totalProductsObject[secondArray[i]] += Number(secondArray[i + 1])
            }
        }

        

        // console.log(totalProductsObject)
    }
    for (const [key, value] of Object.entries(totalProductsObject)) {
        console.log(`${key} -> ${value}`)
    }
}

storeProvisions([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ])
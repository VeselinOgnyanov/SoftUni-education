function order(currrentProduct, quantityOfProduct) {
    function coffeefunc(quantityCoffe) {                    // coffee = 1.50
        return (quantityCoffe * 1.50).toFixed(2)
    };

    function cokefunc(quantityCoke) {                       // coke = 1.40
        return (quantityCoke * 1.40).toFixed(2)
    };

    function waterfunc(quantityWater) {                     // water = 1.00
        return (quantityWater * 1.00).toFixed(2)
    };

    function snacksfunc(quantitySnacks) {                   //snacks = 2.00
        return (quantitySnacks * 2.00).toFixed(2)
    };

    const calculatingObject = {
        coffee: coffeefunc,
        coke: cokefunc,
        water: waterfunc,
        snacks: snacksfunc,
    };

    return calculatingObject[currrentProduct](quantityOfProduct);
}

console.log(order("coffee", 5))
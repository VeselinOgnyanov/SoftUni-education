function factorDivision(firstNum, secondNum) {
    return ((getFactoriel(firstNum) / getFactoriel(secondNum)).toFixed(2))

    function getFactoriel(number) {

        if (number === 1) {
            return number
        }

        return number * getFactoriel(number - 1)

    }

}
console.log(factorDivision(6, 2))
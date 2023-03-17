function formatGrades(currentGrade) {
    currentGrade = Number(currentGrade)
    if (currentGrade < 3.00) {
        currentGrade = 2
        console.log(`Fail (${currentGrade})`)
    } else if ((currentGrade < 3.50)) {
        console.log(`Poor (${currentGrade.toFixed(2)})`)
    } else if ((currentGrade < 4.50)) {
        console.log(`Good (${currentGrade.toFixed(2)})`)
    } else if ((currentGrade < 5.50)) {
        console.log(`Very good (${currentGrade.toFixed(2)})`)
    } else {
        console.log(`Excellent (${currentGrade.toFixed(2)})`)
    }
}

formatGrades(3.33)
formatGrades(4.50)
formatGrades(2.99)
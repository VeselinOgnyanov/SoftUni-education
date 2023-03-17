function oddNumberOfOccur(input) {
    let oddOccur = []
    arrayInput = input.split(" ")
    let counter = 0

    // console.log(arrayInput)
    arrayInputToLower = arrayInput.map(word => word.toLowerCase())
    arrayInputToLower.forEach(element => {
        for (const iterator of arrayInputToLower) {
            if(element === iterator){
                counter+=1
            }
        }
        if(counter % 2 === 1){
            if(!(oddOccur.includes(element))){
                oddOccur.push(element)
            }
            
        }
        counter = 0
    });
    console.log(oddOccur.join(" "))
}


oddNumberOfOccur('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')
oddNumberOfOccur('Cake IS SWEET is Soft CAKE sweet Food')
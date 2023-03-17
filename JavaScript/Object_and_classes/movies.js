function moviesSolve(input) {
    let allMoviesArray = []

    for (const element of input) {
        let splittedArray = element.split(" ")
        if (splittedArray.includes("addMovie")) {
            let name = splittedArray.slice(1).join(" ")
            allMoviesArray.push({ name: name })
        } else if (splittedArray.includes("directedBy")) {
            let currentIndex = splittedArray.indexOf("directedBy")
            let movieName = splittedArray.slice(0, currentIndex).join(" ")
            let movieDirector = splittedArray.slice(currentIndex + 1).join(" ")

            allMoviesArray.forEach(element => {
                if (element.name === movieName) {
                    element.director = movieDirector
                }
            });
        } else /*onDate*/ {
            let currentIndex = splittedArray.indexOf("onDate")
            let movieName = splittedArray.slice(0, currentIndex).join(" ")
            let movieDate = splittedArray.slice(currentIndex + 1).join(" ")

            allMoviesArray.forEach(element => {
                if (element.name === movieName) {
                    element.date = movieDate
                }
            });
        }
    }
    for (const iterator of allMoviesArray) {
        if ((iterator.hasOwnProperty("name")) && (iterator.hasOwnProperty("director")) && (iterator.hasOwnProperty("date")))
        console.log(JSON.stringify(iterator))
       
    }
    
}


moviesSolve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
])

moviesSolve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ])
function city(currrentCity) {
let tuples = Object.entries(currrentCity)

for (const [keys, values] of tuples) {
    console.log(`${keys} -> ${values}`)
}
}


city({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
})
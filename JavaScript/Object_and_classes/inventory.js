function inventory(input) {
    registerHerosArray = []
    for (const line of input) {
        currentLine = line.split(" / ")
        let [Hero, level, items] = currentLine
        // console.log(currentLine)
        registerHerosArray.push({ Hero, level, items })
    }

    let sortedByLevel = registerHerosArray.sort((heroA, heroB) => heroA.level - heroB.level)

    for (const iterator of sortedByLevel) {
        let { Hero, level, items } = iterator
        console.log(`Hero: ${Hero}\nlevel => ${level}\nitems => ${items}`)
    }

}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
])

inventory([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
])
function mettings(schedules) {
    let dailySchedule = {}
    let conflictSchedule = []

    for (const line of schedules) {
        let [currentDay, Name] = line.split(" ")
        if (currentDay in dailySchedule) {
            conflictSchedule.push(currentDay)
            console.log(`Conflict on ${currentDay}!`)
        } else {
            dailySchedule[currentDay] = Name
            console.log(`Scheduled for ${currentDay}`)
        }
    }

    for (const key in dailySchedule) {
        console.log(`${key} -> ${dailySchedule[key]}`)

    }
}


    mettings(['Monday Peter',
        'Wednesday Bill',
        'Monday Tim',
        'Friday Tim'])

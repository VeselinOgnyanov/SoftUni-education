function colorize() {
    const button = document.getElementsByTagName("button")
    const tablebody = Array.from(document.querySelectorAll("tr"))

    let counter = 1
    for (const iterator of tablebody) {
        counter += 1
        if (counter % 2 === 1){
            iterator.style.backgroundColor = "Teal"
        }
    }
    
   

    // console.log(tablebody)
}
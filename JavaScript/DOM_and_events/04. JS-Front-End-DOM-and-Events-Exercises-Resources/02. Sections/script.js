function create(words) {
   const contentDiv = document.getElementById("content")
  


   for (const currentWord of words) {
      const newDiv = document.createElement("div")
      const newParagraph = document.createElement("p")
      newDiv.appendChild(newParagraph)
      newParagraph.textContent = currentWord
      newParagraph.style.display = "none"
      newDiv.addEventListener("click", () => {
         newParagraph.style.display = "block"
      })
      contentDiv.appendChild(newDiv)
   }


}



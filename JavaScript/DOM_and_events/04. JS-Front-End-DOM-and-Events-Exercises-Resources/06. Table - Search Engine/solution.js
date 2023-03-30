function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const tableDataArray = Array.from(document.querySelectorAll("tbody tr td"))
      const searchFieldArea = document.getElementById("searchField")

      let searchedWord = searchFieldArea.value

      // debugger
      for (const element of tableDataArray) {
         if (element.textContent.includes(searchedWord)) {
            let parentElement = element.parentNode
            parentElement.classList.add("select")
         }         
      }

      searchFieldArea.value = ""
   }
}
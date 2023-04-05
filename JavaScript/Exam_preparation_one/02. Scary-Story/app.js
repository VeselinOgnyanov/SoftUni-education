window.addEventListener("load", solve);

function solve() {
  let firstNameField = document.getElementById("first-name")
  let lastNameField = document.getElementById("last-name")
  let ageField = document.getElementById("age")
  let storyTitleField = document.getElementById("story-title")
  let genreField = document.getElementById("genre")
  let textAreaField = document.getElementById("story")
  let publishBtn = document.getElementById("form-btn")
  let previewList = document.getElementById("preview-list")
  let mainDiv = document.getElementById("main")

  publishBtn.addEventListener("click", publishHandler)

  function publishHandler(e) {
    e.preventDefault()

    let firstNameValue = firstNameField.value
    let lastNameValue = lastNameField.value
    let ageValue = ageField.value
    let storyTitleValue = storyTitleField.value
    let genreFieldValue = genreField.value
    let textAreaFieldValue = textAreaField.value

    if (!firstNameValue || !lastNameValue || !ageValue || !storyTitleValue || !textAreaFieldValue) {
      return
    }

    firstNameField.value = ""
    lastNameField.value = ""
    ageField.value = ""
    storyTitleField.value = ""
    textAreaField.value = ""

    let li = document.createElement("li")
    li.classList.add("story-info")

    let article = document.createElement("article")

    let h4 = document.createElement("h4")
    h4.textContent = `Name: ${firstNameValue} ${lastNameValue}`

    let pAge = document.createElement("p")
    pAge.textContent = `Age: ${ageValue}`

    let pTitle = document.createElement("p")
    pTitle.textContent = `Title: ${storyTitleValue}`

    let pGenre = document.createElement("p")
    pGenre.textContent = `Genre: ${genreFieldValue}`

    let pStory = document.createElement("p")
    pStory.textContent = textAreaFieldValue

    //BUTTONS
    let saveBtn = document.createElement("button")
    saveBtn.classList.add("save-btn")
    saveBtn.textContent = "Save Story"
    saveBtn.disabled = false
    saveBtn.addEventListener("click", saveHandler)

    let editBtn = document.createElement("button")
    editBtn.classList.add("edit-btn")
    editBtn.textContent = "Edit Story"
    editBtn.disabled = false
    editBtn.addEventListener("click", editHandler)

    let deleteBtn = document.createElement("button")
    deleteBtn.classList.add("delete-btn")
    deleteBtn.textContent = "Delete Story"
    deleteBtn.disabled = false
    deleteBtn.addEventListener("click", deleteHandler)

    article.appendChild(h4)
    article.appendChild(pAge)
    article.appendChild(pTitle)
    article.appendChild(pGenre)
    article.appendChild(pStory)
    li.appendChild(article)
    li.appendChild(saveBtn)
    li.appendChild(editBtn)
    li.appendChild(deleteBtn)
    previewList.appendChild(li)

    publishBtn.disabled = true

    //HANDLERS
    function saveHandler(e) {
      mainDiv.innerHTML = ""
      let h1 = document.createElement("h1")
      h1.textContent = `Your scary story is saved!`
      mainDiv.appendChild(h1)

    }
    function editHandler(e) {
      firstNameField.value = firstNameValue
      lastNameField.value = lastNameValue
      ageField.value = ageValue
      storyTitleField.value = storyTitleValue
      genreField.value = genreFieldValue
      textAreaField.value = textAreaFieldValue
      e.target.parentElement.remove()
      publishBtn.disabled = false
    }
    function deleteHandler(e) {
      li.remove()
      publishBtn.disabled = false
    }

  }
}

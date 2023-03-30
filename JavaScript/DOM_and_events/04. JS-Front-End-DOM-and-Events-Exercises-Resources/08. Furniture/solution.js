function solve() {
  let generateButton = document.querySelectorAll('button')[0];
  let buyButton = document.querySelectorAll('button')[1];
  let table = document.querySelector('tbody');
  let result = document.querySelectorAll('textarea')[1];
 
 
  generateButton.addEventListener('click', eventGenerate);
  buyButton.addEventListener('click', eventBuy);
 
  function eventGenerate() {
    let inputArea = JSON.parse(document.querySelectorAll('textarea')[0].value);
 
    for (let inputElement of inputArea) {
      let newTr = document.createElement('tr');
 
      let imgTd = document.createElement('td');
      let img = document.createElement('img');
      img.src = inputElement['img'];
      imgTd.appendChild(img);
      newTr.appendChild(imgTd);
 
      let nameTd = document.createElement('td');
      let nameParagraph = document.createElement('p');
      nameParagraph.textContent = inputElement['name'];
      nameTd.appendChild(nameParagraph);
      newTr.appendChild(nameTd);
 
      let priceTd = document.createElement('td');
      let priceParagraph = document.createElement('p');
      priceParagraph.textContent = inputElement['price'];
      priceTd.appendChild(priceParagraph);
      newTr.appendChild(priceTd);
 
      let decTd = document.createElement('td');
      let decParagraph = document.createElement('p');
      decParagraph.textContent = inputElement['decFactor'];
      decTd.appendChild(decParagraph);
      newTr.appendChild(decTd);
 
      let checBoxTd = document.createElement('td');
      let checkBox = document.createElement('input');
      checkBox.type = 'checkbox';
      checBoxTd.appendChild(checkBox);
      newTr.appendChild(checBoxTd);
 
 
      table.appendChild(newTr);
 
    }
  };
 
  function eventBuy() {
    let inventory = [];
    let priceSum = 0;
    let decSum = 0;
 
    for (let items of Array.from(table.children)) {
      let name = items.querySelectorAll('p')[0];
      let price = items.querySelectorAll('p')[1];
      let dec = items.querySelectorAll('p')[2];
 
      let check = items.querySelectorAll('input');
 
 
      if (check[0].checked) {
        inventory.push(name.textContent)
        priceSum += Number(price.textContent)
        decSum += Number(dec.textContent)
      };
    };
 
    result.value = `Bought furniture: ${inventory.join(', ')}\nTotal price: ${priceSum.toFixed(2)}\nAverage decoration factor: ${decSum / inventory.length}`;
  };
 
}
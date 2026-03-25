document.addEventListener('DOMContentLoaded', solve);

function solve() {
  const shopElement = document.querySelector('#shop');

  const tableBody = shopElement.querySelector('table tbody');

  const generateBtn = document.querySelector('#input input[type=submit]');
  generateBtn.addEventListener('click', generateBtnGetInputHandler);

  function generateBtnGetInputHandler(e) {
    e.preventDefault();

    const furnitures = JSON.parse(document.querySelector('#input textarea').value);
    const furnitureElementsArr = furnitures.map(createRowElement);

    tableBody.append(...furnitureElementsArr);
  }

  function createRowElement(furniture) {
    {
      const trElement = document.createElement('tr');

      const tdSourceElement = document.createElement('td');
      const imgElement = document.createElement('img');
      imgElement.src = furniture.img;
      tdSourceElement.appendChild(imgElement);

      const tdNameElement = document.createElement('td');
      const pNameElement = document.createElement('p');
      pNameElement.classList.add('name');
      pNameElement.textContent = furniture.name;
      tdNameElement.appendChild(pNameElement);

      const tdPriceElement = document.createElement('td');
      const pPriceElement = document.createElement('p');
      pPriceElement.classList.add('price');
      pPriceElement.textContent = furniture.price;
      tdPriceElement.appendChild(pPriceElement);

      const tdDecFactorElement = document.createElement('td');
      const pDecFactorElement = document.createElement('p');
      pDecFactorElement.classList.add('decFactor');
      pDecFactorElement.textContent = furniture.decFactor;
      tdDecFactorElement.appendChild(pDecFactorElement);

      const tdCheckboxELement = document.createElement('td');
      const inputCheckboxElement = document.createElement('input');
      inputCheckboxElement.type = 'checkbox';
      tdCheckboxELement.appendChild(inputCheckboxElement);

      trElement.append(
        tdSourceElement,
        tdNameElement,
        tdPriceElement,
        tdDecFactorElement,
        tdCheckboxELement
      )

      return trElement;
    }
  }

  const buyBtn = shopElement.querySelector('input[type=submit]');
  buyBtn.addEventListener('click', shopFurnituresHandler);

  function shopFurnituresHandler(e) {
    e.preventDefault();

    const nameFurnitures = [];
    let totalPrice = 0;
    let sumDecFactor = 0;

    const tableRows = tableBody.querySelectorAll('tr');
    const checkedFurnitureData = Array.from(
      Array.from(tableRows)
        .filter(row => row.querySelector('td input[type=checkbox]').checked)
        .map(row => {
          return {
            name: row.querySelector('.name').textContent,
            price: row.querySelector('.price').textContent,
            decFactor: row.querySelector('.decFactor').textContent
          }
        }
        )
    )

    checkedFurnitureData.forEach(furniture => {
      nameFurnitures.push(furniture.name);
      totalPrice += Number(furniture.price);
      sumDecFactor += Number(furniture.decFactor);
    })

    let result = `Bought furniture: ${nameFurnitures.join(', ')}\n`
    result += `Total price: ${totalPrice}\n`
    result += `Average decoration factor: ${sumDecFactor / checkedFurnitureData.length}`

    const resultTextbox = shopElement.querySelector('textarea');
    resultTextbox.value = result;
  }
}
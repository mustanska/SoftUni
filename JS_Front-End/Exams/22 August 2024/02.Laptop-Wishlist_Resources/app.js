window.addEventListener("load", solve);

function solve() {
  const laptopModelInputElement = document.getElementById('laptop-model');
  const storageInputElement = document.getElementById('storage');
  const priceInputElement = document.getElementById('price');

  const checkUlListELement = document.getElementById('check-list');
  const laptopsUlListElement = document.getElementById('laptops-list');

  const addBtnElement = document.getElementById('add-btn');
  addBtnElement.addEventListener('click', addLaptopHandler);

  const clearBtnElement = document.querySelector('.clear');
  clearBtnElement.addEventListener('click', clearPageHandler);

  function addLaptopHandler(e) {
    e.preventDefault();

    const laptopModel = laptopModelInputElement.value;
    const storage = storageInputElement.value;
    const price = priceInputElement.value;

    if (!laptopModel || !storage || !price) {
      return;
    }

    addBtnElement.setAttribute('disabled', '');

    const liElement = createLaptopElement(laptopModel, storage, price);
    checkUlListELement.appendChild(liElement);

    laptopModelInputElement.value = '';
    storageInputElement.value = '';
    priceInputElement.value = '';
  }

  function clearPageHandler() {
    location.reload();
  }

  function createLaptopElement(model, storage, price) {
    const liElement = document.createElement('li');
    liElement.classList.add('laptop-item');

    const articleElement = document.createElement('article');

    const pModelElement = document.createElement('p');
    pModelElement.textContent = model;
    const pStorageElement = document.createElement('p');
    pStorageElement.textContent = `Memory: ${storage} TB`;
    const pPriceElement = document.createElement('p');
    pPriceElement.textContent = `Price: ${price}$`;

    articleElement.append(pModelElement, pStorageElement, pPriceElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('btn', 'edit');
    editBtnElement.textContent = 'edit';
    editBtnElement.addEventListener('click', () => {
      addBtnElement.removeAttribute('disabled');

      laptopModelInputElement.value = model;
      storageInputElement.value = storage;
      priceInputElement.value = price;

      liElement.remove();
    })

    const okBtnElement = document.createElement('button');
    okBtnElement.classList.add('btn', 'ok');
    okBtnElement.textContent = 'ok';
    okBtnElement.addEventListener('click', () => {
      editBtnElement.remove();
      okBtnElement.remove();
      
      addBtnElement.removeAttribute('disabled');

      laptopsUlListElement.appendChild(liElement);
    })

    liElement.append(articleElement, editBtnElement, okBtnElement);

    return liElement;
  }
}

const baseUrl = 'http://localhost:3030/jsonstore/grocery';

let currentProductId = '';

const productInputElement = document.getElementById('product');
const countInputElement = document.getElementById('count');
const priceInputElement = document.getElementById('price');

const tableBodyElement = document.getElementById('tbody');

const addProductBtnElement = document.getElementById('add-product');
addProductBtnElement.addEventListener('click', addProductHandler);

const updateProductBtnElement = document.getElementById('update-product');
updateProductBtnElement.addEventListener('click', updateProductHandler);

const loadProductsBtnElement = document.getElementById('load-product');
loadProductsBtnElement.addEventListener('click', loadProductsHandler);

async function addProductHandler(e) {
    e.preventDefault();

    const productObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(productObj)
    });

    loadAllProducts();

    clearInputValues();
}

async function updateProductHandler(e) {
    e.preventDefault();

    const productObj = getInputValues();

    await fetch(`${baseUrl}/${currentProductId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(productObj)
    });

    loadAllProducts();

    clearInputValues();

    updateProductBtnElement.setAttribute('disabled', '');
    addProductBtnElement.removeAttribute('disabled');
}

function loadProductsHandler(e) {
    e.preventDefault();

    loadAllProducts();
}

async function loadAllProducts() {
    const products = (await getAllProducts()).map(createProductElement);

    tableBodyElement.innerHTML = '';

    tableBodyElement.append(...products);
}

async function getAllProducts() {
    const response = await fetch(baseUrl);
    const data = await response.json();
    
    return Object.values(data);
}

function createProductElement(productInfo) {
    const trElement = document.createElement('tr');

    const nameTdElement = document.createElement('td');
    nameTdElement.classList.add('name');
    nameTdElement.textContent = productInfo.product;
    trElement.appendChild(nameTdElement);

    const countTdElement = document.createElement('td');
    countTdElement.classList.add('count-product');
    countTdElement.textContent = productInfo.count;
    trElement.appendChild(countTdElement);

    const priceTdElement = document.createElement('td');
    priceTdElement.classList.add('product-price');
    priceTdElement.textContent = productInfo.price;
    trElement.appendChild(priceTdElement);

    const buttonsTdElement = document.createElement('td');
    buttonsTdElement.classList.add('btn');

    const updateBtnElement = document.createElement('button');
    updateBtnElement.classList.add('update');
    updateBtnElement.textContent = 'Update';
    updateBtnElement.addEventListener('click', () => {
        updateProductBtnElement.removeAttribute('disabled');
        addProductBtnElement.setAttribute('disabled', '');

        productInputElement.value = productInfo.product;
        countInputElement.value = productInfo.count;
        priceInputElement.value = productInfo.price;

        currentProductId = productInfo._id;
    });
    buttonsTdElement.appendChild(updateBtnElement);

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete');
    deleteBtnElement.textContent = 'Delete';
    deleteBtnElement.addEventListener('click', async () => {
        currentProductId = productInfo._id;

        await fetch(`${baseUrl}/${currentProductId}`, {
            method: 'DELETE',
        });

        loadAllProducts();
    });
    buttonsTdElement.appendChild(deleteBtnElement);

    trElement.appendChild(buttonsTdElement);

    return trElement;
}

function getInputValues() {
    const product = productInputElement.value;
    const count = countInputElement.value;
    const price = priceInputElement.value;

    return {
        product,
        count,
        price
    };
}

function clearInputValues() {
    productInputElement.value = '';
    countInputElement.value = '';
    priceInputElement.value = '';
}
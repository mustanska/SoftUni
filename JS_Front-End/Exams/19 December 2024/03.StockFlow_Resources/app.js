let currentOrderId = '';

const nameInputElement = document.getElementById('name');
const quantityInputElement = document.getElementById('quantity');
const dateInputElement = document.getElementById('date');

const ordersListElement = document.getElementById('list');

const loadOrdersBtnElement = document.getElementById('load-orders');
loadOrdersBtnElement.addEventListener('click', loadOrdersHandler);

const orderBtnElement = document.getElementById('order-btn');
orderBtnElement.addEventListener('click', addNewOrderHandler);

const editBtnElement = document.getElementById('edit-order');
editBtnElement.addEventListener('click', editOrderHandler);

async function loadOrdersHandler() {
    await getAllOrders();
}

async function addNewOrderHandler(e) {
    e.preventDefault();

    const name = nameInputElement.value.trim();
    const quantity = quantityInputElement.value.trim();
    const date = dateInputElement.value.trim();

    const orderObj = {name, quantity, date};

    await fetch('http://localhost:3030/jsonstore/orders', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(orderObj)
    });

    getAllOrders();

    clearInputs();
}

async function editOrderHandler(e) {
    e.preventDefault();

    const name = nameInputElement.value.trim();
    const quantity = quantityInputElement.value.trim();
    const date = dateInputElement.value.trim();

    const orderObj = {name, quantity, date};

    await fetch(`http://localhost:3030/jsonstore/orders/${currentOrderId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(orderObj)
    });

    getAllOrders();

    clearInputs();

    editBtnElement.setAttribute('disabled', '');
    orderBtnElement.removeAttribute('disabled');
}

async function getAllOrders() {
    const response = await fetch('http://localhost:3030/jsonstore/orders');
    const data = await response.json();
    const orders = Object.values(data)
    .map(createOrder);

    ordersListElement.append(...orders);
}

function createOrder(order) {
    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    const headerNameElement = document.createElement('h2');
    headerNameElement.textContent = order.name;

    const headerDateElement = document.createElement('h3');
    headerDateElement.textContent = order.date;

    const headerQuantityElement = document.createElement('h3');
    headerQuantityElement.textContent = order.quantity;

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        containerDivElement.remove();

        nameInputElement.value = order.name;
        quantityInputElement.value = order.quantity;
        dateInputElement.value = order.date;

        editBtnElement.removeAttribute('disabled');
        orderBtnElement.setAttribute('disabled', '');

        currentOrderId = order._id;
    })

    const doneBtnElement = document.createElement('button');
    doneBtnElement.classList.add('done-btn');
    doneBtnElement.textContent = 'Done';
    doneBtnElement.addEventListener('click', async () => {
        currentOrderId = order._id;

        await fetch(`http://localhost:3030/jsonstore/orders/${currentOrderId}`, {
        method: 'DELETE',
        });

        getAllOrders();
    })

    containerDivElement.append(
        headerNameElement,
        headerDateElement,
        headerQuantityElement,
        changeBtnElement,
        doneBtnElement
    )

    return containerDivElement;
}

function clearInputs() {
    nameInputElement.value = '';
    quantityInputElement.value = '';
    dateInputElement.value = '';
}
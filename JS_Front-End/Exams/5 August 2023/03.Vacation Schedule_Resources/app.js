const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let currentVacationId = '';

const vacationsListDivElement = document.getElementById('list');

const nameInputElement = document.getElementById('name');
const daysNumberInputElement = document.getElementById('num-days');
const fromDateInputElement = document.getElementById('from-date');

const addVacationBtnElement = document.getElementById('add-vacation');
addVacationBtnElement.addEventListener('click', addVacationHandler);

const editVacationBtnElement = document.getElementById('edit-vacation');
editVacationBtnElement.addEventListener('click', editVacationHandler);

const loadVacationBtnElement = document.getElementById('load-vacations');
loadVacationBtnElement.addEventListener('click', loadVacationHandler);

function loadVacationHandler() {
    loadAllVacationRecords();
}

async function addVacationHandler(e) {
    e.preventDefault();

    const vacationObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(vacationObj)
    });

    loadAllVacationRecords();
    clearInputValues();
}

async function editVacationHandler(e) {
    e.preventDefault();

    const vacationObj = getInputValues();

    await fetch(`${baseUrl}/${currentVacationId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(vacationObj)
    });

    loadAllVacationRecords();
    clearInputValues();

    addVacationBtnElement.removeAttribute('disabled');
    editVacationBtnElement.setAttribute('disabled', '');
}

async function loadAllVacationRecords() {
    const vacations = (await getAllVacationRecords()).map(createVacationElement);

    vacationsListDivElement.innerHTML = '';

    vacationsListDivElement.append(...vacations);
}

async function getAllVacationRecords() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

function createVacationElement(vacationInfo) {
    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    const nameHeaderElement = document.createElement('h2');
    nameHeaderElement.textContent = vacationInfo.name;

    const dateHeaderElement = document.createElement('h3');
    dateHeaderElement.textContent = vacationInfo.date;

    const daysHeaderElement = document.createElement('h3');
    daysHeaderElement.textContent = vacationInfo.days;

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        currentVacationId = vacationInfo._id;

        containerDivElement.remove();

        nameInputElement.value = vacationInfo.name;
        daysNumberInputElement.value = vacationInfo.days;
        fromDateInputElement.value = vacationInfo.date;

        addVacationBtnElement.setAttribute('disabled', '');
        editVacationBtnElement.removeAttribute('disabled');
    });

    const doneBtnElement = document.createElement('button');
    doneBtnElement.classList.add('done-btn');
    doneBtnElement.textContent = 'Done';
    doneBtnElement.addEventListener('click', async () => {
        currentVacationId = vacationInfo._id;
        
        await fetch(`${baseUrl}/${currentVacationId}`, {
            method: 'DELETE',
        });

        loadAllVacationRecords();
    });

    containerDivElement.append(
        nameHeaderElement,
        dateHeaderElement,
        daysHeaderElement,
        changeBtnElement,
        doneBtnElement
    );

    return containerDivElement;
}

function getInputValues() {
    const name = nameInputElement.value;
    const days = daysNumberInputElement.value;
    const date = fromDateInputElement.value;

    return {
        name,
        days,
        date
    };
}

function clearInputValues() {
    nameInputElement.value = '';
    daysNumberInputElement.value = '';
    fromDateInputElement.value = '';
}
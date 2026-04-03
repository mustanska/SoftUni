let currentRecordID = '';

const nameInputElement = document.getElementById('p-name');
const stepsInputElement = document.getElementById('steps');
const caloriesInputElement = document.getElementById('calories');

const loadBtnElement = document.getElementById('load-records');
loadBtnElement.addEventListener('click', getRecordsHandler);

const addRecordBtnElement = document.getElementById('add-record');
addRecordBtnElement.addEventListener('click', addRecordHandler);

const editRecordBtnElement = document.getElementById('edit-record');
editRecordBtnElement.addEventListener('click', changeInfoRecordHandler);

const recordsUlElement = document.getElementById('list');

async function getRecordsHandler() {
    await loadAllRecords();
}

async function addRecordHandler() {
    const name = nameInputElement.value.trim();
    const steps = stepsInputElement.value.trim();
    const calories = caloriesInputElement.value.trim();

    const recordObj = {
        name,
        steps,
        calories
    };

    await fetch('http://localhost:3030/jsonstore/records', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(recordObj)
    });

    clearInputFields();

    await loadAllRecords();
}

async function changeInfoRecordHandler() {
    const name = nameInputElement.value.trim();
    const steps = stepsInputElement.value.trim();
    const calories = caloriesInputElement.value.trim();

    const recordObj = {
        name,
        steps,
        calories
    };

    await fetch(`http://localhost:3030/jsonstore/records/${currentRecordID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(recordObj)
    });

    editRecordBtnElement.setAttribute('disabled', '');
    addRecordBtnElement.removeAttribute('disabled');

    clearInputFields();

    await loadAllRecords();
}

async function loadAllRecords() {
    const response = await fetch('http://localhost:3030/jsonstore/records');
    const data = await response.json();
    const records = Object.values(data)
        .map(createRecordElement);

    recordsUlElement.innerHTML = '';
    recordsUlElement.append(...records);
}

function createRecordElement(record) {
    const liElement = document.createElement('li');
    liElement.classList.add('record');

    const infoDivElement = document.createElement('div');
    infoDivElement.classList.add('info');

    const pNameElement = document.createElement('p');
    pNameElement.textContent = record.name;

    const pStepsElement = document.createElement('p');
    pStepsElement.textContent = record.steps;

    const pCaloriesElement = document.createElement('p');
    pCaloriesElement.textContent = record.calories;

    infoDivElement.append(pNameElement, pStepsElement, pCaloriesElement);

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.classList.add('btn-wrapper');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        nameInputElement.value = record.name;
        stepsInputElement.value = record.steps;
        caloriesInputElement.value = record.calories;

        addRecordBtnElement.setAttribute('disabled', '');
        editRecordBtnElement.removeAttribute('disabled');

        currentRecordID = record._id;
    })

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Delete';
    deleteBtnElement.addEventListener('click', async () => {
        currentRecordID = record._id;

        await fetch(`http://localhost:3030/jsonstore/records/${currentRecordID}`, {
            method: 'DELETE',
        });

        await loadAllRecords();
    })

    buttonsDivElement.append(changeBtnElement, deleteBtnElement);

    liElement.append(infoDivElement, buttonsDivElement);

    return liElement;
}

function clearInputFields() {
    nameInputElement.value = '';
    stepsInputElement.value = '';
    caloriesInputElement.value = '';
}
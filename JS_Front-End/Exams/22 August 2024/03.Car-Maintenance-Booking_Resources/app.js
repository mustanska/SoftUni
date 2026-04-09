const baseUrl = 'http://localhost:3030/jsonstore/appointments';

let currentAppointmentId = '';

const appointmentsUlListElement = document.getElementById('appointments-list');

const modelInputElement = document.getElementById('car-model');
const serviceInputElement = document.getElementById('car-service');
const dateInputElement = document.getElementById('date');

const addAppointmentBtnElement = document.getElementById('add-appointment');
addAppointmentBtnElement.addEventListener('click', addNewAppointmentHandler);

const editAppointmentBtnElement = document.getElementById('edit-appointment');
editAppointmentBtnElement.addEventListener('click', editAppointmentHandler);

const loadAppointmentsBtnElement = document.getElementById('load-appointments');
loadAppointmentsBtnElement.addEventListener('click', loadAppointmentsClickHandler);

function loadAppointmentsClickHandler() {
    loadAppontmentsElements();
}

async function addNewAppointmentHandler() {
    const appointmentObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(appointmentObj)
    });

    loadAppontmentsElements();

    clearInputs();
}

async function editAppointmentHandler() {
    const appointmentObj = getInputValues();

    await fetch(`${baseUrl}/${currentAppointmentId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(appointmentObj)
    });

    loadAppontmentsElements();

    clearInputs();

    editAppointmentBtnElement.setAttribute('disabled', '');
    addAppointmentBtnElement.removeAttribute('disabled');
}

async function getAppointmentsInfo() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

async function loadAppontmentsElements() {
    const appointmentsInfo = await getAppointmentsInfo();
    const appointments = appointmentsInfo.map(createAppointmentElement);

    appointmentsUlListElement.innerHTML = '';

    appointmentsUlListElement.append(...appointments);
}

function createAppointmentElement(appointmentInfo) {
    const liElement = document.createElement('li');
    liElement.classList.add('appointment');

    const modelHeaderElement = document.createElement('h2');
    modelHeaderElement.textContent = appointmentInfo.model;
    const dateHeaderElement = document.createElement('h3');
    dateHeaderElement.textContent = appointmentInfo.date;
    const serviceHeaderElement = document.createElement('h3');
    serviceHeaderElement.textContent = appointmentInfo.service;

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.classList.add('buttons-appointment');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        editAppointmentBtnElement.removeAttribute('disabled');
        addAppointmentBtnElement.setAttribute('disabled', '');

        modelInputElement.value = appointmentInfo.model;
        dateInputElement.value = appointmentInfo.date;
        serviceInputElement.value = appointmentInfo.service;

        currentAppointmentId = appointmentInfo._id;
    })

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Delete';
    deleteBtnElement.addEventListener('click', async () => {
        currentAppointmentId = appointmentInfo._id;

        await fetch(`${baseUrl}/${currentAppointmentId}`, {
        method: 'DELETE',
        });

        loadAppontmentsElements();
    })

    buttonsDivElement.append(changeBtnElement, deleteBtnElement);

    liElement.append(modelHeaderElement, dateHeaderElement, serviceHeaderElement, buttonsDivElement);

    return liElement;
}

function getInputValues() {
    const model = modelInputElement.value;
    const service = serviceInputElement.value;
    const date = dateInputElement.value;

    return {
        model,
        service, 
        date
    };
}

function clearInputs() {
    modelInputElement.value = '';
    serviceInputElement.value = '';
    dateInputElement.value = '';
}
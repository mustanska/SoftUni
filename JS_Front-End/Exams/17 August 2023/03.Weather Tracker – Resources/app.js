const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let currentWeatherId = '';

const locationInputElement = document.getElementById('location');
const temperatureInputElement = document.getElementById('temperature');
const dateInputElement = document.getElementById('date');

const weathersListElement = document.getElementById('list');

const loadHistoryBtnElement = document.getElementById('load-history');
loadHistoryBtnElement.addEventListener('click', loadHistoryHandler);

const addWeatherBtnElement = document.getElementById('add-weather');
addWeatherBtnElement.addEventListener('click', addWeatherHandler);

const editWeatherBtnElement = document.getElementById('edit-weather');
editWeatherBtnElement.addEventListener('click', editWeatherHandler);

function loadHistoryHandler() {
    loadWeathersHistory();
}

async function addWeatherHandler() {
    const weaterObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(weaterObj)
    });

    loadWeathersHistory();

    clearInputValues();
}

async function editWeatherHandler() {
    const weaterObj = getInputValues();

    await fetch(`${baseUrl}/${currentWeatherId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(weaterObj)
    });

    loadWeathersHistory();

    clearInputValues();

    addWeatherBtnElement.removeAttribute('disabled');
    editWeatherBtnElement.setAttribute('disabled', '');
}

async function getWeathersHistory() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

async function loadWeathersHistory() {
    const weathers = (await getWeathersHistory()).map(createWeatherElement);

    weathersListElement.innerHTML = '';
    weathersListElement.append(...weathers);
}

function getInputValues() {
    const location = locationInputElement.value.trim();
    const temperature = temperatureInputElement.value.trim();
    const date = dateInputElement.value.trim();

    return {
        location,
        temperature,
        date
    };
}

function clearInputValues() {
    locationInputElement.value = '';
    temperatureInputElement.value = '';
    dateInputElement.value = '';
}

function createWeatherElement(weatherInfo) {
    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    const locationHeaderElement = document.createElement('h2');
    locationHeaderElement.textContent = weatherInfo.location;
    containerDivElement.appendChild(locationHeaderElement);

    const dateHeaderElement = document.createElement('h3');
    dateHeaderElement.textContent = weatherInfo.date;
    containerDivElement.appendChild(dateHeaderElement);

    const temperatureHeaderElement = document.createElement('h3');
    temperatureHeaderElement.setAttribute('id', 'celsius');
    temperatureHeaderElement.textContent = weatherInfo.temperature;
    containerDivElement.appendChild(temperatureHeaderElement);

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.setAttribute('id', 'buttons-container');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        currentWeatherId = weatherInfo._id;

        containerDivElement.remove();

        locationInputElement.value = weatherInfo.location;
        temperatureInputElement.value = weatherInfo.temperature;
        dateInputElement.value = weatherInfo.date;

        addWeatherBtnElement.setAttribute('disabled', '');
        editWeatherBtnElement.removeAttribute('disabled');
    });
    buttonsDivElement.appendChild(changeBtnElement);

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Delete';
    deleteBtnElement.addEventListener('click', async () => {
        currentWeatherId = weatherInfo._id;

        await fetch(`${baseUrl}/${currentWeatherId}`, {
        method: 'DELETE',
        });
        
        loadWeathersHistory();
    });
    buttonsDivElement.appendChild(deleteBtnElement);

    containerDivElement.appendChild(buttonsDivElement);

    return containerDivElement;
}
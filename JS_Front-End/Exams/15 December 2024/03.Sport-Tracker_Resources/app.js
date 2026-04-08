const baseUrl = 'http://localhost:3030/jsonstore/workout';

let currentWorkoutId = '';

const loadBtnElement = document.getElementById('load-workout');
loadBtnElement.addEventListener('click', loadClickHandler);

const addWorkoutBtnElement = document.getElementById('add-workout');
addWorkoutBtnElement.addEventListener('click', addWorkoutClickHandler);

const editWorkoutBtnElement = document.getElementById('edit-workout');
editWorkoutBtnElement.addEventListener('click', editWorkoutClickHandler);

const workoutInputElement = document.getElementById('workout');
const locationInputElement = document.getElementById('location');
const dateInputElement = document.getElementById('date');

const listDivElement = document.getElementById('list');

function loadClickHandler() {
    loadWorkouts();
}

async function addWorkoutClickHandler() {
    const workout = workoutInputElement.value;
    const location = locationInputElement.value;
    const date = dateInputElement.value;

    const workoutObj = {
        workout,
        location,
        date
    };

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(workoutObj)
    }
    );

    clearInputs();

    loadWorkouts();
}

async function editWorkoutClickHandler() {
    const workout = workoutInputElement.value;
    const location = locationInputElement.value;
    const date = dateInputElement.value;

    const workoutObj = {
        workout,
        location,
        date
    };

    await fetch(`${baseUrl}/${currentWorkoutId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(workoutObj)
    });

    addWorkoutBtnElement.removeAttribute('disabled');
    editWorkoutBtnElement.setAttribute('disabled', '');

    clearInputs();

    loadWorkouts();
}

async function getWorkoutsInfo() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

async function loadWorkouts() {
    const workouts = await getWorkoutsInfo();
    listDivElement.innerHTML = '';
    listDivElement.append(...workouts.map(createWorkoutElement));
}

function createWorkoutElement(workoutInfo) {
    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    const workoutHeaderElement = document.createElement('h2');
    workoutHeaderElement.textContent = workoutInfo.workout;

    const dateHeaderElement = document.createElement('h3');
    dateHeaderElement.textContent = workoutInfo.date;

    const locationHeaderElement = document.createElement('h3');
    locationHeaderElement.setAttribute('id', 'location');
    locationHeaderElement.textContent = workoutInfo.location;

    const containerBtnsDivElement = document.createElement('div');
    containerBtnsDivElement.setAttribute('id', 'buttons-container');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        workoutInputElement.value = workoutInfo.workout;
        locationInputElement.value = workoutInfo.location;
        dateInputElement.value = workoutInfo.date;

        currentWorkoutId = workoutInfo._id;

        addWorkoutBtnElement.setAttribute('disabled', '');
        editWorkoutBtnElement.removeAttribute('disabled');
    })

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Done';
    deleteBtnElement.addEventListener('click', async () => {
        currentWorkoutId = workoutInfo._id;

        await fetch(`${baseUrl}/${currentWorkoutId}`, {
        method: 'DELETE',
        });

        loadWorkouts();
    })

    containerBtnsDivElement.append(
        changeBtnElement,
        deleteBtnElement
    );

    containerDivElement.append(
        workoutHeaderElement,
        dateHeaderElement,
        locationHeaderElement,
        containerBtnsDivElement
    );

    return containerDivElement;
}

function clearInputs() {
    workoutInputElement.value = '';
    locationInputElement.value = '';
    dateInputElement.value = '';
}
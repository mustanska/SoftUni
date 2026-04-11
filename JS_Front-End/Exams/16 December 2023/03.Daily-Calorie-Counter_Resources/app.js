const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let currentMealId = '';

const foodInputElement = document.getElementById('food');
const timeInputElement = document.getElementById('time');
const caloriesInputElement = document.getElementById('calories');

const mealsListDivElement = document.getElementById('list');

const loadMealsBtnElement = document.getElementById('load-meals');
loadMealsBtnElement.addEventListener('click', loadMealsHandler);

const addMealBtnElement = document.getElementById('add-meal');
addMealBtnElement.addEventListener('click', addMealHandler);

const editMealBtnElement = document.getElementById('edit-meal');
editMealBtnElement.addEventListener('click', editMealHandler);

function loadMealsHandler() {
    loadAllMeals();
}

async function addMealHandler() {
    const mealObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(mealObj)
    });

    loadAllMeals();

    clearInputValues();
}

async function editMealHandler() {
    const mealObj = getInputValues();

    await fetch(`${baseUrl}/${currentMealId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(mealObj)
    });

    loadAllMeals();

    clearInputValues();

    addMealBtnElement.removeAttribute('disabled');
    editMealBtnElement.setAttribute('disabled', '');
}

async function loadAllMeals() {
    const meals = (await getAllMeals()).map(createMealElement);

    mealsListDivElement.innerHTML = '';

    mealsListDivElement.append(...meals);
}

async function getAllMeals() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

function createMealElement(mealInfo) {
    const mealDivElement = document.createElement('div');
    mealDivElement.classList.add('meal');

    const foodHeaderElement = document.createElement('h2');
    foodHeaderElement.textContent = mealInfo.food;
    mealDivElement.appendChild(foodHeaderElement);

    const timeHeaderElement = document.createElement('h3');
    timeHeaderElement.textContent = mealInfo.time;
    mealDivElement.appendChild(timeHeaderElement);

    const caloriesHeaderElement = document.createElement('h3');
    caloriesHeaderElement.textContent = mealInfo.calories;
    mealDivElement.appendChild(caloriesHeaderElement);

    const buttonsDivElement = document.createElement('div');
    buttonsDivElement.setAttribute('id', 'meal-buttons');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-meal');
    changeBtnElement.textContent = 'Change';
    buttonsDivElement.appendChild(changeBtnElement);
    changeBtnElement.addEventListener('click', () => {
        currentMealId = mealInfo._id;

        mealDivElement.remove();

        foodInputElement.value = mealInfo.food;
        timeInputElement.value = mealInfo.time;
        caloriesInputElement.value = mealInfo.calories;

        editMealBtnElement.removeAttribute('disabled');
        addMealBtnElement.setAttribute('disabled', '');
    })

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-meal');
    deleteBtnElement.textContent = 'Delete';
    buttonsDivElement.appendChild(deleteBtnElement);
    deleteBtnElement.addEventListener('click', async () => {
        currentMealId = mealInfo._id;
        
        await fetch(`${baseUrl}/${currentMealId}`, {
            method: 'DELETE',
        });

        loadAllMeals();
    })

    mealDivElement.appendChild(buttonsDivElement);

    return mealDivElement;
}

function getInputValues() {
    const food = foodInputElement.value;
    const time = timeInputElement.value;
    const calories = caloriesInputElement.value;

    return {
        food,
        time,
        calories
    };
}

function clearInputValues() {
    foodInputElement.value = '';
    timeInputElement.value = '';
    caloriesInputElement.value = '';
}
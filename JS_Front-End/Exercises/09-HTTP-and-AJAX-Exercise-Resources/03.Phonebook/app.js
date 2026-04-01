const phonebookUlElement = document.getElementById('phonebook');

function attachEvents() {
    const loadBtnElement = document.getElementById('btnLoad');
    const createBtnElement = document.getElementById('btnCreate');

    loadBtnElement.addEventListener('click', getNumbersHandler);
    createBtnElement.addEventListener('click', addNumberHandler);
}

async function getNumbersHandler() {
    const response = await fetch('http://localhost:3030/jsonstore/phonebook');
    const data = await response.json();
    const infoNumbers = Object.values(data)
        .map(createPhonebookItem);

    phonebookUlElement.append(...infoNumbers);
    console.log(data);
    
}

async function addNumberHandler() {
    const person = document.getElementById('person').value;
    const phone = document.getElementById('phone').value;

    const numberObj = {person, phone};
    console.log(numberObj);
    

    const response = await fetch('http://localhost:3030/jsonstore/phonebook', {
        method: 'POST',
        headers: {
            'content-type': 'aplication/json'
        },
        body: JSON.stringify(numberObj)
    });
}

async function deleteNumberHandler(e) {
    const currentLiElement = e.currentTarget.parentElement;
    const response = await fetch(`http://localhost:3030/jsonstore/phonebook/${currentLiElement.id}`, {
        method: 'DELETE'
    })

}

function createPhonebookItem(numberInfo) {
    const liElement = document.createElement('li');
    liElement.id = numberInfo._id;
    liElement.textContent = `${numberInfo.person}: ${numberInfo.phone}`;

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.addEventListener('click', deleteNumberHandler);

    liElement.appendChild(deleteBtn);

    return liElement;
}

attachEvents();
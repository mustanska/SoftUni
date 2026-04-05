window.addEventListener("load", solve);

function solve() {
    const eventNameInputElement = document.getElementById('event');
    const noteInputElement = document.getElementById('note');
    const dateInputElement = document.getElementById('date');

    const upcomingUlListElement = document.getElementById('upcoming-list');
    const eventUlListElement = document.getElementById('events-list');

    const saveBtnElement = document.getElementById('save');
    saveBtnElement.addEventListener('click', upcomingEventHandler);

    const deleteBtnElement = document.querySelector('.delete');
    deleteBtnElement.addEventListener('click', deleteAllEventsHandler);

    function upcomingEventHandler() {
        const eventName = eventNameInputElement.value;
        const note = noteInputElement.value;
        const date = dateInputElement.value;

        if (!eventName || !note || !date) {
            return;
        }

        const liElement = createEvent(eventName, note, date);
        upcomingUlListElement.appendChild(liElement);

        clearInputs();
    }

    function deleteAllEventsHandler() {
        eventUlListElement.innerHTML = '';
    }

    function createEvent(name, note, date) {
        const liElement = document.createElement('li');
        liElement.classList.add('event-item');

        const eventContainerDivElement = document.createElement('div');
        eventContainerDivElement.classList.add('event-container');

        const articleElement = document.createElement('article');

        const pNameElement = document.createElement('p');
        pNameElement.textContent = `Name: ${name}`;
        articleElement.appendChild(pNameElement);

        const pNoteElement = document.createElement('p');
        pNoteElement.textContent = `Note: ${note}`;
        articleElement.appendChild(pNoteElement);

        const pDateElement = document.createElement('p');
        pDateElement.textContent = `Date: ${date}`;
        articleElement.appendChild(pDateElement);

        const buttonsDivElement = document.createElement('div');
        buttonsDivElement.classList.add('buttons');

        const editBtnElement = document.createElement('button');
        editBtnElement.classList.add('btn', 'edit');
        editBtnElement.textContent = 'Edit';
        editBtnElement.addEventListener('click', () => {
            liElement.remove();
            eventNameInputElement.value = name;
            noteInputElement.value = note;
            dateInputElement.value = date;
        });
        buttonsDivElement.appendChild(editBtnElement);

        const doneBtnElement = document.createElement('button');
        doneBtnElement.classList.add('btn', 'done');
        doneBtnElement.textContent = 'Done';
        doneBtnElement.addEventListener('click', () => {
            eventUlListElement.appendChild(liElement);
            buttonsDivElement.remove();
        })
        buttonsDivElement.appendChild(doneBtnElement);

        eventContainerDivElement.appendChild(articleElement);
        eventContainerDivElement.appendChild(buttonsDivElement);

        liElement.appendChild(eventContainerDivElement);

        return liElement;
    }

    function clearInputs() {
        eventNameInputElement.value = '';
        noteInputElement.value = '';
        dateInputElement.value = '';
    }
}


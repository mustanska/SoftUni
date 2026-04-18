window.addEventListener("load", solve);

function solve(){
    const nameInputElement = document.getElementById('name');
    const locationInputElement = document.getElementById('location');
    const genderInputElement = document.getElementById('gender');

    const preparingUlListElement = document.getElementById('preparing-list');
    const characterUlListElement = document.getElementById('character-list');

    const createBtnElement = document.getElementById('create-btn');
    createBtnElement.addEventListener('click', createCharacterHandler);

    function createCharacterHandler(e) {
        e.preventDefault();

        const name = nameInputElement.value;
        const location = locationInputElement.value;
        const gender = genderInputElement.value;

        if(!name || !location || !gender) {
            return;
        }

        const liCharacterElement = createCharacterElement(name, location, gender);
        preparingUlListElement.appendChild(liCharacterElement);

        createBtnElement.setAttribute('disabled', '');

        nameInputElement.value = '';
        locationInputElement.value = '';
        genderInputElement.value = '';
    }

    function createCharacterElement(name, location, gender) {
        const liElement = document.createElement('li');
        liElement.classList.add('creating');

        const articleElement = document.createElement('article');

        const nameHeaderElement = document.createElement('h4');
        nameHeaderElement.textContent = name;
        articleElement.appendChild(nameHeaderElement);

        const pLocationElement = document.createElement('p');
        pLocationElement.textContent = location;
        articleElement.appendChild(pLocationElement);

        const pGenderElement = document.createElement('p');
        pGenderElement.textContent = gender;
        articleElement.appendChild(pGenderElement);

        liElement.appendChild(articleElement);

        const editBtnElement = document.createElement('button');
        editBtnElement.classList.add('action-btn', 'edit');
        editBtnElement.textContent = 'Edit';
        editBtnElement.addEventListener('click', () => {
            nameInputElement.value = name;
            locationInputElement.value = location;
            genderInputElement.value = gender;

            liElement.remove();

            createBtnElement.removeAttribute('disabled');
        });
        liElement.appendChild(editBtnElement);

        const doneBtnElement = document.createElement('button');
        doneBtnElement.classList.add('action-btn', 'done');
        doneBtnElement.textContent = 'Done';
        doneBtnElement.addEventListener('click', () => {
            editBtnElement.remove();
            doneBtnElement.remove();

            characterUlListElement.appendChild(liElement);

            createBtnElement.removeAttribute('disabled');
        });
        liElement.appendChild(doneBtnElement);

        return liElement;
    }
}

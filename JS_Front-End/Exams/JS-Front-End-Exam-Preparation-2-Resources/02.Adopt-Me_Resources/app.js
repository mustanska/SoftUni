window.addEventListener("load", solve);

function solve() {
    const typeInputElement = document.getElementById('type');
    const ageInputElement = document.getElementById('age');
    const genderInputElement = document.getElementById('gender');

    const adoptBtnElement = document.getElementById('adopt-btn');
    adoptBtnElement.addEventListener('click', addAnimalHandler);

    const adoptionInfoUlElement = document.getElementById('adoption-info');
    const adoptedUlElement = document.getElementById('adopted-list');

    function addAnimalHandler(e) {
      e.preventDefault();

      const type = typeInputElement.value;
      const age = ageInputElement.value;
      const gender = genderInputElement.value;

      const animalLiElement = createAnimalElement(type, age, gender);
      adoptionInfoUlElement.appendChild(animalLiElement);

      typeInputElement.value = '';
      ageInputElement.value = '';
      genderInputElement.value = '';
    }

    function createAnimalElement(type, age, gender) {
      const liElement = document.createElement('li');
      
      const articleElement = document.createElement('article');

      const pTypeElement = document.createElement('p');
      pTypeElement.textContent = `Pet:${type}`;
      articleElement.appendChild(pTypeElement);

      const pGenderElement = document.createElement('p');
      pGenderElement.textContent = `Gender:${gender}`;
      articleElement.appendChild(pGenderElement);

      const pAgeElement = document.createElement('p');
      pAgeElement.textContent = `Age:${age}`;
      articleElement.appendChild(pAgeElement);

      const buttonsDivElement = document.createElement('div');
      buttonsDivElement.classList.add('buttons');

      const editBtnElement = document.createElement('button');
      editBtnElement.classList.add('edit-btn');
      editBtnElement.textContent = 'Edit';
      buttonsDivElement.appendChild(editBtnElement);
      editBtnElement.addEventListener('click', () => {
        typeInputElement.value = type;
        ageInputElement.value = age;
        genderInputElement.value = gender;

        liElement.remove();
      })

      const doneBtnElement = document.createElement('button');
      doneBtnElement.classList.add('done-btn');
      doneBtnElement.textContent = 'Done';
      buttonsDivElement.appendChild(doneBtnElement);
      doneBtnElement.addEventListener('click', () => {
        adoptedUlElement.appendChild(liElement);
        buttonsDivElement.remove();

        const clearBtnElement = document.createElement('button');
        clearBtnElement.classList.add('clear-btn');
        clearBtnElement.textContent = 'Clear';
        clearBtnElement.addEventListener('click', () => {
          liElement.remove();
        })

        liElement.appendChild(clearBtnElement);
      })

      liElement.appendChild(articleElement);
      liElement.appendChild(buttonsDivElement);

      return liElement;
    }
  }
  
window.addEventListener("load", solve);

function solve() {
  const firstNameInputElement = document.getElementById('first-name');
  const lastNameInputElement = document.getElementById('last-name');
  const ageInputElement = document.getElementById('age');
  const storyTitleInputElement = document.getElementById('story-title');
  const genreInputElement = document.getElementById('genre');
  const storyTextInputElement = document.getElementById('story');

  const mainDivElement = document.getElementById('main');
  const previewUlListElement = document.getElementById('preview-list');

  const publishBtnElement = document.getElementById('form-btn');
  publishBtnElement.addEventListener('click', addStoryHandler);

  function addStoryHandler() {
    const firstName = firstNameInputElement.value;
    const lastName = lastNameInputElement.value;
    const age = ageInputElement.value;
    const storyTitle = storyTitleInputElement.value;
    const genre = genreInputElement.value;
    const storyText = storyTextInputElement.value;

    if (!firstName || !lastName || !age || !storyTitle || !genre || !storyText) {
      return;
    }

    const liElement = createStoryElement(firstName, lastName, age, storyTitle, genre, storyText);
    previewUlListElement.appendChild(liElement);

    firstNameInputElement.value = '';
    lastNameInputElement.value = '';
    ageInputElement.value = '';
    storyTitleInputElement.value = '';
    genreInputElement.value = '';
    storyTextInputElement.value = '';

    publishBtnElement.setAttribute('disabled', '');
  }

  function createStoryElement(firstName, lastName, age, storyTitle, genre, storyText) {
    const liElement = document.createElement('li');
    liElement.classList.add('story-info');

    const articleElement = document.createElement('article');

    const nameHeaderElement = document.createElement('h4');
    nameHeaderElement.textContent = `Name: ${firstName} ${lastName}`;
    articleElement.appendChild(nameHeaderElement);

    const pAgeElement = document.createElement('p');
    pAgeElement.textContent = `Age: ${age}`;
    articleElement.appendChild(pAgeElement);

    const pTitleElement = document.createElement('p');
    pTitleElement.textContent = `Title: ${storyTitle}`;
    articleElement.appendChild(pTitleElement);

    const pGenreElement = document.createElement('p');
    pGenreElement.textContent = `Genre: ${genre}`;
    articleElement.appendChild(pGenreElement);

    const pTextElement = document.createElement('p');
    pTextElement.textContent = storyText;
    articleElement.appendChild(pTextElement);

    liElement.appendChild(articleElement);

    const saveBtnElement = document.createElement('button');
    saveBtnElement.classList.add('save-btn');
    saveBtnElement.textContent = 'Save Story';
    saveBtnElement.addEventListener('click', () => {
      mainDivElement.innerHTML = '';

      const headerElement = document.createElement('h1');
      headerElement.textContent = 'Your scary story is saved!';

      mainDivElement.appendChild(headerElement);
    });
    liElement.appendChild(saveBtnElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('edit-btn');
    editBtnElement.textContent = 'Edit Story';
    editBtnElement.addEventListener('click', () => {
      firstNameInputElement.value = firstName;
      lastNameInputElement.value = lastName;
      ageInputElement.value = age;
      storyTitleInputElement.value = storyTitle;
      genreInputElement.value = genre;
      storyTextInputElement.value = storyText;

      publishBtnElement.removeAttribute('disabled');

      liElement.remove();

      saveBtnElement.setAttribute('disabled', '');
      editBtnElement.setAttribute('disabled', '');
      deleteBtnElement.setAttribute('disabled', '');
    });
    liElement.appendChild(editBtnElement);

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Delete Story';
    deleteBtnElement.addEventListener('click', () => {
      liElement.remove();

      publishBtnElement.removeAttribute('disabled');
    });
    liElement.appendChild(deleteBtnElement);

    return liElement;
  }
}

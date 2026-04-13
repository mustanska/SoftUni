window.addEventListener("load", solve);

function solve() {
  const studentInputElement = document.getElementById('student');
  const universityInputElement = document.getElementById('university');
  const scoreInputElement = document.getElementById('score');

  const previewUlListElement = document.getElementById('preview-list');
  const candidatesUlListElement = document.getElementById('candidates-list');

  const nextBtnElement = document.getElementById('next-btn');
  nextBtnElement.addEventListener('click', addStudentInformationHandler);

  function addStudentInformationHandler(e) {
    e.preventDefault();

    const student = studentInputElement.value;
    const university = universityInputElement.value;
    const score = scoreInputElement.value;

    if (!student || !university || !score) {
      return;
    }

    const liElement = createStudentElement(student, university, score);
    previewUlListElement.appendChild(liElement);

    clearInputValues();

    nextBtnElement.setAttribute('disabled', '');
  }

  function createStudentElement(name, university, score) {
    const liElement = document.createElement('li');
    liElement.classList.add('application');

    const articleElement = document.createElement('article');

    const studentHeaderElement = document.createElement('h4');
    studentHeaderElement.textContent = name;
    articleElement.appendChild(studentHeaderElement);

    const pUniversityElement = document.createElement('p');
    pUniversityElement.textContent = `University: ${university}`;
    articleElement.appendChild(pUniversityElement);

    const pScoreElement = document.createElement('p');
    pScoreElement.textContent = `Score: ${score}`;
    articleElement.appendChild(pScoreElement);

    liElement.appendChild(articleElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('action-btn', 'edit');
    editBtnElement.textContent = 'edit';
    editBtnElement.addEventListener('click', () => {
      liElement.remove();

      studentInputElement.value = name;
      universityInputElement.value = university;
      scoreInputElement.value = score;

      nextBtnElement.removeAttribute('disabled');
    });
    liElement.appendChild(editBtnElement);

    const applyBtnElement = document.createElement('button');
    applyBtnElement.classList.add('action-btn', 'apply');
    applyBtnElement.textContent = 'apply';
    applyBtnElement.addEventListener('click', () => {
      editBtnElement.remove();
      applyBtnElement.remove();

      candidatesUlListElement.appendChild(liElement);

      nextBtnElement.removeAttribute('disabled');
    });
    liElement.appendChild(applyBtnElement);

    return liElement;
  }

  function clearInputValues() {
    studentInputElement.value = '';
    universityInputElement.value = '';
    scoreInputElement.value = '';
  }
}

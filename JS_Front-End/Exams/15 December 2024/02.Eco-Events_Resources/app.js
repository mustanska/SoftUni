window.addEventListener("load", solve);

function solve() {
  const emailInputElement = document.getElementById('email');
  const eventInputElement = document.getElementById('event');
  const locationInputElement = document.getElementById('location');

  const nextBtnElement = document.getElementById('next-btn');
  nextBtnElement.addEventListener('click', getEventHandler);

  const previewListElement = document.getElementById('preview-list');
  const eventListElement = document.getElementById('event-list');

  function getEventHandler(e) {
    e.preventDefault();

    const email = emailInputElement.value;
    const event = eventInputElement.value;
    const location = locationInputElement.value;

    if(!email || !event || !location) {
      return;
    }

    const liElement = createEvent(email, event, location);

    previewListElement.appendChild(liElement);

    nextBtnElement.setAttribute('disabled', '');

    emailInputElement.value = '';
    eventInputElement.value = '';
    locationInputElement.value = '';
  }

  function createEvent(email, event, location) {
    const liElement = document.createElement('li');
    liElement.classList.add('application');

    const articleElement = document.createElement('article');

    const headerElement = document.createElement('h4');
    headerElement.textContent = email;

    const pEventElement = document.createElement('p');
    const strongEventElement = document.createElement('strong');
    strongEventElement.textContent = 'Event:';
    const brEventElement = document.createElement('br');
    pEventElement.append(strongEventElement, brEventElement, event);

    const pLocationElement = document.createElement('p');
    const strongLocationElement = document.createElement('strong');
    strongLocationElement.textContent = 'Location:';
    const brLocationElement = document.createElement('br');
    pLocationElement.append(strongLocationElement, brLocationElement, location);

    articleElement.append(headerElement, pEventElement, pLocationElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('action-btn', 'edit');
    editBtnElement.textContent = 'edit';
    editBtnElement.addEventListener('click', () => {
      liElement.remove();

      emailInputElement.value = email;
      eventInputElement.value = event;
      locationInputElement.value = location;

      nextBtnElement.removeAttribute('disabled');
    })

    const applyBtnElement = document.createElement('button');
    applyBtnElement.classList.add('action-btn', 'apply');
    applyBtnElement.textContent = 'apply';
    applyBtnElement.addEventListener('click', () => {
      eventListElement.appendChild(liElement);
      editBtnElement.remove();
      applyBtnElement.remove();

      nextBtnElement.removeAttribute('disabled');
    })

    liElement.append(articleElement, editBtnElement, applyBtnElement);

    return liElement;
  }
}

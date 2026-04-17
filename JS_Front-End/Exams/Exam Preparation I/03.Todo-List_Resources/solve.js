function attachEvents() {
  const baseUrl = 'http://localhost:3030/jsonstore/tasks';

  let currentTaskId = '';

  const titleInputElement = document.getElementById('title');

  const toDoUlListElement = document.getElementById('todo-list');

  const addBtnElement = document.getElementById('add-button');
  addBtnElement.addEventListener('click', addTaskHandler);

  const loadBtnElement = document.getElementById('load-button');
  loadBtnElement.addEventListener('click', loadTasksHandler);

  async function addTaskHandler(e) {
    e.preventDefault();

    const name = titleInputElement.value;
    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({name})
    });

    loadAllTasks();

    titleInputElement.value = '';
  }

  function loadTasksHandler(e) {
    e.preventDefault();

    loadAllTasks();
  }

  async function loadAllTasks() {
    const tasks = (await getAllTasks()).map(createTaskElement);

    toDoUlListElement.innerHTML = '';
    toDoUlListElement.append(...tasks);
  }

  async function getAllTasks() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
  }

  function createTaskElement(taskInfo) {
    const liElement = document.createElement('li');

    const spanElement = document.createElement('span');
    spanElement.textContent = taskInfo.name;
    liElement.appendChild(spanElement);

    const removeBtnElement = document.createElement('button');
    removeBtnElement.textContent = 'Remove';
    removeBtnElement.addEventListener('click', async () => {
        currentTaskId = taskInfo._id;

        await fetch(`${baseUrl}/${currentTaskId}`, {
            method: 'DELETE',
        });

        loadAllTasks();
    });
    liElement.appendChild(removeBtnElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.textContent = 'Edit';
    editBtnElement.addEventListener('click', () => {
        const inputElement = document.createElement('input');
        inputElement.value = spanElement.textContent;

        spanElement.remove();

        liElement.prepend(inputElement);

        editBtnElement.remove();

        const submitBtnElement = document.createElement('button');
        submitBtnElement.textContent = 'Submit';
        submitBtnElement.addEventListener('click', async () => {
            currentTaskId = taskInfo._id;

            const name = inputElement.value;

            await fetch(`${baseUrl}/${currentTaskId}`, {
                method: 'PATCH',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({name})
            });

            loadAllTasks();
        })
        liElement.appendChild(submitBtnElement);
    })
    liElement.appendChild(editBtnElement);

    return liElement;
  }
}

attachEvents();

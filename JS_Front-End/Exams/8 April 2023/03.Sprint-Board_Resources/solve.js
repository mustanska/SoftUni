function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/tasks';

    let currentTaskId = '';

    const status = {
        'ToDo' : {textContentBtn: 'Move to In Progress', taskId: 'todo'},
        'In Progress' : {textContentBtn: 'Move to Code Review', taskId: 'inProgress'},
        'Code Review' : {textContentBtn: 'Move to Done', taskId: 'codeReview'},
        'Done' : {textContentBtn: 'Close', taskId: 'done'}
    };

    const statusSections = {
        'todo' : (liElement) => toDoSectionElement.appendChild(liElement),
        'inProgress' : (liElement) => inProgressSectionElement.appendChild(liElement),
        'codeReview' : (liElement) => codeReviewSectionElement.appendChild(liElement),
        'done': (liElement) => doneSectionElement.appendChild(liElement)
    };

    const statusActions = {
        'ToDo' : async () => {
            await fetch(`${baseUrl}/${currentTaskId}`, {
                method: 'PATCH',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({status: 'In Progress'})
            })
        },
        'In Progress' : async () => {
            await fetch(`${baseUrl}/${currentTaskId}`, {
                method: 'PATCH',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({status: 'Code Review'})
            })
        },
        'Code Review' : async () => {
            await fetch(`${baseUrl}/${currentTaskId}`, {
                method: 'PATCH',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify({status: 'Done'})
            })
        },
        'Done' : async () => {
            await fetch(`${baseUrl}/${currentTaskId}`, {
                method: 'DELETE',
            })
        } 
    };

    const titleInputElement = document.getElementById('title');
    const descriptionInputElement = document.getElementById('description');

    const toDoSectionElement = document.getElementById('todo-section');
    const inProgressSectionElement = document.getElementById('in-progress-section');
    const codeReviewSectionElement = document.getElementById('code-review-section');
    const doneSectionElement = document.getElementById('done-section');

    const loadBoardBtnElement = document.getElementById('load-board-btn');
    loadBoardBtnElement.addEventListener('click', loadBoardHandler);

    const createTaskBtnElement = document.getElementById('create-task-btn');
    createTaskBtnElement.addEventListener('click', createTaskHandler);

    function loadBoardHandler() {
        loadAllTasks();
    }

    async function createTaskHandler() {
        const title = titleInputElement.value;
        const description = descriptionInputElement.value;
        const status = 'ToDo';

        const taskObj = {
            title,
            description,
            status
        };

        await fetch(baseUrl, {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(taskObj)
        });

        loadAllTasks();

        titleInputElement.value = '';
        descriptionInputElement.value = '';
    }

    async function loadAllTasks() {
        toDoSectionElement.innerHTML = '';
        inProgressSectionElement.innerHTML = '';
        codeReviewSectionElement.innerHTML = '';
        doneSectionElement.innerHTML = '';

        (await getAllTasks()).map((taskInfo) => {
            const liElement = createTaskElement(taskInfo);
            const taskId = liElement.getAttribute('data-id');

            statusSections[taskId](liElement);
        });
    }

    async function getAllTasks() {
        const response = await fetch(baseUrl);
        const data = await response.json();

        return Object.values(data);
    }

    function createTaskElement(taskInfo) {
        const liElement = document.createElement('li');
        liElement.classList.add('task');
        liElement.setAttribute('data-id', status[taskInfo.status].taskId);

        const titleHeaderElement = document.createElement('h3');
        titleHeaderElement.textContent = taskInfo.title;
        liElement.appendChild(titleHeaderElement);

        const pDescriptionElement = document.createElement('p');
        pDescriptionElement.textContent = taskInfo.description;
        liElement.appendChild(pDescriptionElement);

        const buttonElement = document.createElement('button');
        buttonElement.textContent = status[taskInfo.status].textContentBtn;
        buttonElement.addEventListener('click', () => {
            currentTaskId = taskInfo._id;

            statusActions[taskInfo.status]();

            loadAllTasks();
        });
        liElement.appendChild(buttonElement);

        return liElement;
    }
}

attachEvents();
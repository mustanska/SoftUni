window.addEventListener('load', solve);

function solve() {
    let totalPoints = 0;

    const taskIdHiddenInputElement = document.getElementById('task-id');
    const titleInputElement = document.getElementById('title');
    const descriptionInputElement = document.getElementById('description');
    const labelInputElement = document.getElementById('label');
    const estimationPointsInputElement = document.getElementById('points');
    const assigneeInputElement = document.getElementById('assignee');

    const taskSectionElement = document.getElementById('tasks-section');
    const totalPointsElement = document.getElementById('total-sprint-points');

    const createTaskBtnElement = document.getElementById('create-task-btn');
    createTaskBtnElement.addEventListener('click', addTaskHandler);

    const deleteTaskBtnElement = document.getElementById('delete-task-btn');
    deleteTaskBtnElement.addEventListener('click', deleteTaskHandler);

    function addTaskHandler() {
        const title = titleInputElement.value;
        const description = descriptionInputElement.value;
        const label = labelInputElement.value;
        const points = estimationPointsInputElement.value;
        const assignee = assigneeInputElement.value;

        if (!title || !description || !label || !points || !assignee) {
            return;
        }

        totalPoints += Number(points);
        updateTotalPoints(totalPoints);

        const tasksCount = taskSectionElement.querySelectorAll('article').length;

        const articleElement = createTaskElement(tasksCount, title, description, label, points, assignee);
        taskSectionElement.appendChild(articleElement);

        clearInputValues();
    }

    function deleteTaskHandler() {
        const taskId = taskIdHiddenInputElement.value;
        const points = estimationPointsInputElement.value;

        const currentArticleElement = document.getElementById(taskId);
        currentArticleElement.remove();

        totalPoints -= Number(points);
        updateTotalPoints(totalPoints);

        clearInputValues();

        titleInputElement.removeAttribute('disabled');
        descriptionInputElement.removeAttribute('disabled');
        labelInputElement.removeAttribute('disabled');
        estimationPointsInputElement.removeAttribute('disabled');
        assigneeInputElement.removeAttribute('disabled');

        createTaskBtnElement.removeAttribute('disabled');
        deleteTaskBtnElement.setAttribute('disabled', '');
    }

    function createTaskElement(tasksCount, title, description, label, points, assignee) {
        const articleElement = document.createElement('article');
        articleElement.setAttribute('id', `task-${tasksCount + 1}`);
        articleElement.classList.add('task-card');

        const labelDivElement = createTaskLabelElement(label);
        articleElement.appendChild(labelDivElement);

        const titleHeaderElement = document.createElement('h3');
        titleHeaderElement.classList.add('task-card-title');
        titleHeaderElement.textContent = title;
        articleElement.appendChild(titleHeaderElement);

        const pDescriptionElement = document.createElement('p');
        pDescriptionElement.classList.add('task-card-description');
        pDescriptionElement.textContent = description;
        articleElement.appendChild(pDescriptionElement);

        const pointsDivElement = document.createElement('div');
        pointsDivElement.classList.add('task-card-points');
        pointsDivElement.textContent = `Estimated at ${points} pts`;
        articleElement.appendChild(pointsDivElement);

        const assigneeDivElement = document.createElement('div');
        assigneeDivElement.classList.add('task-card-assignee');
        assigneeDivElement.textContent = `Assigned to: ${assignee}`;
        articleElement.appendChild(assigneeDivElement);

        const actionsDivElement = document.createElement('div');
        actionsDivElement.classList.add('task-card-actions');

        const deleteBtnElement = document.createElement('button');
        deleteBtnElement.textContent = 'Delete';
        deleteBtnElement.addEventListener('click', () => {
            taskIdHiddenInputElement.value = `task-${tasksCount + 1}`;

            titleInputElement.value = title;
            titleInputElement.setAttribute('disabled', '');

            descriptionInputElement.value = description;
            descriptionInputElement.setAttribute('disabled', '');

            labelInputElement.value = label;
            labelInputElement.setAttribute('disabled', '');

            estimationPointsInputElement.value = points;
            estimationPointsInputElement.setAttribute('disabled', '');

            assigneeInputElement.value = assignee;
            assigneeInputElement.setAttribute('disabled', '');

            deleteTaskBtnElement.removeAttribute('disabled');
            createTaskBtnElement.setAttribute('disabled', '');
        })
        actionsDivElement.appendChild(deleteBtnElement);

        articleElement.appendChild(actionsDivElement);

        return articleElement;
    }

    function createTaskLabelElement(label) {
        const labelDivElement = document.createElement('div');

        let classLabel = '';
        let iconLabel = '';

        switch (label) {
            case 'Feature':
                classLabel = 'feature';
                iconLabel = '&#8865';
                break;
            case 'Low Priority Bug':
                classLabel = 'low-priority';
                iconLabel = '&#9737';
                break;
            case 'High Priority Bug':
                classLabel = 'high-priority';
                iconLabel = '&#9888';
        }

        labelDivElement.classList.add('task-card-label', classLabel);
        labelDivElement.innerHTML = `${label} ${iconLabel}`;

        return labelDivElement;
    }

    function updateTotalPoints(totalPoints) {
        totalPointsElement.textContent = `Total Points ${totalPoints}pts`;
    }

    function clearInputValues() {
        titleInputElement.value = '';
        descriptionInputElement.value = '';
        labelInputElement.value = '';
        estimationPointsInputElement.value = '';
        assigneeInputElement.value = '';
    }
}
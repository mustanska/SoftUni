const baseUrl = 'http://localhost:3030/jsonstore/tasks';

let currentCourseId = '';

const courseNameInputElement = document.getElementById('course-name');
const courseTypeInputElement = document.getElementById('course-type');
const descriptionInputElement = document.getElementById('description');
const teacherNameInputElement = document.getElementById('teacher-name');

const addCourseBtnElement = document.getElementById('add-course');
addCourseBtnElement.addEventListener('click', addCourseHandler);

const editCourseBtnElement = document.getElementById('edit-course');
editCourseBtnElement.addEventListener('click', editCourseHandler);

const loadCoursesBtnElement = document.getElementById('load-course');
loadCoursesBtnElement.addEventListener('click', loadCoursesHandler);

const courseListDivElement = document.getElementById('list');

function loadCoursesHandler() {
    loadAllCourses();
}

async function addCourseHandler(e) {
    e.preventDefault();

    const courseObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(courseObj)
    });

    loadAllCourses();

    clearInputValues();
}

async function editCourseHandler(e) {
    e.preventDefault();

    const courseObj = getInputValues();

    await fetch(`${baseUrl}/${currentCourseId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(courseObj)
    });

    loadAllCourses();

    clearInputValues();

    addCourseBtnElement.removeAttribute('disabled');
    editCourseBtnElement.setAttribute('disabled', '');
}

async function loadAllCourses() {
    const courses = (await getCourses()).map(createCourseElement);

    courseListDivElement.innerHTML = '';
    courseListDivElement.append(...courses);
}

async function getCourses() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

function createCourseElement(courseInfo) {
    const containerDivElement = document.createElement('div');
    containerDivElement.classList.add('container');

    const courseTitleHeaderElement = document.createElement('h2');
    courseTitleHeaderElement.textContent = courseInfo.title;
    const teacherNameHeaderElement = document.createElement('h3');
    teacherNameHeaderElement.textContent = courseInfo.teacher;
    const courseTypeHeaderElement = document.createElement('h3');
    courseTypeHeaderElement.textContent = courseInfo.type;
    const descriptionHeaderElement = document.createElement('h4');
    descriptionHeaderElement.textContent = courseInfo.description;

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('edit-btn');
    editBtnElement.textContent = 'Edit Course';
    editBtnElement.addEventListener('click', () => {
        currentCourseId = courseInfo._id;

        containerDivElement.remove();

        courseNameInputElement.value = courseInfo.title;
        courseTypeInputElement.value = courseInfo.type;
        descriptionInputElement.value = courseInfo.description;
        teacherNameInputElement.value = courseInfo.teacher;

        addCourseBtnElement.setAttribute('disabled', '');
        editCourseBtnElement.removeAttribute('disabled');
    });

    const finishBtnElement = document.createElement('button');
    finishBtnElement.classList.add('finish-btn');
    finishBtnElement.textContent = 'Finish Course';
    finishBtnElement.addEventListener('click', async () => {
        currentCourseId = courseInfo._id;

        await fetch(`${baseUrl}/${currentCourseId}`, {
        method: 'DELETE',
        });

        loadAllCourses();
    });

    containerDivElement.append(
        courseTitleHeaderElement,
        teacherNameHeaderElement,
        courseTypeHeaderElement,
        descriptionHeaderElement,
        editBtnElement,
        finishBtnElement
    );

    return containerDivElement;
}

function getInputValues() {
    const title = courseNameInputElement.value.trim();
    const type = courseTypeInputElement.value.trim();
    const description = descriptionInputElement.value.trim();
    const teacher = teacherNameInputElement.value.trim();

    return {
        title,
        type,
        description,
        teacher
    };
}

function clearInputValues() {
    courseNameInputElement.value = '';
    courseTypeInputElement.value = '';
    descriptionInputElement.value = '';
    teacherNameInputElement.value = '';
}
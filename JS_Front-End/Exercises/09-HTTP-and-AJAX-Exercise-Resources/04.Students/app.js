const tableBodyElement = document.querySelector('#results tbody');
const formElement = document.getElementById('form');
const inputs = Array.from(document.querySelectorAll('.inputs input'));

getStudents();

formElement.addEventListener('submit', addStudentHandler);
inputs.map(input => input.required = true);

async function getStudents() {
    const response = await fetch('http://localhost:3030/jsonstore/collections/students');
    const data = await response.json();
    const students = Object.values(data)
        .map(createStudentInfoRow);
    
    tableBodyElement.append(...students);
}

async function addStudentHandler() {
    const firstName = document.querySelector('input[name=firstName]').value;
    const lastName = document.querySelector('input[name=lastName]').value;
    const facultyNumber = document.querySelector('input[name=facultyNumber]').value;
    const grade = document.querySelector('input[name=grade]').value;

    const studentInfoObj = {
        firstName,
        lastName, 
        facultyNumber, 
        grade
    };

    const response = await fetch('http://localhost:3030/jsonstore/collections/students', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(studentInfoObj)
    });

    getStudents();
}

function createStudentInfoRow(studentInfo) {
    const trElement = document.createElement('tr');

    const tdFirstNameElement = document.createElement('td');
    tdFirstNameElement.textContent = studentInfo.firstName;

    const tdLastNameElement = document.createElement('td');
    tdLastNameElement.textContent = studentInfo.lastName;

    const tdFacultyNumberElement = document.createElement('td');
    tdFacultyNumberElement.textContent = studentInfo.facultyNumber;

    const tdGradeElement = document.createElement('td');
    tdGradeElement.textContent = studentInfo.grade;

    trElement.append(
        tdFirstNameElement,
        tdLastNameElement,
        tdFacultyNumberElement,
        tdGradeElement
    )

    return trElement;
}
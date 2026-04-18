let currentMovieId = '';

const baseUrl = 'http://localhost:3030/jsonstore/movies';

const movieTitleInputElement = document.getElementById('title');
const directorInputElement = document.getElementById('director');
const yearInputElement = document.getElementById('year');

const movieListDivElement = document.getElementById('movie-list');

const addMovieBtnElement = document.getElementById('add-movie');
addMovieBtnElement.addEventListener('click', addMovieHandler);

const editMovieBtnElement = document.getElementById('edit-movie');
editMovieBtnElement.addEventListener('click', editMovieHandler);

const loadMoviesBtnElement = document.getElementById('load-movies');
loadMoviesBtnElement.addEventListener('click', loadMoviesHandler);

async function addMovieHandler() {
    const movieObj = getInputValues();

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(movieObj)
    });

    loadAllMovies();

    clearInputValues();
}

async function editMovieHandler() {
    const movieObj = getInputValues();

    await fetch(`${baseUrl}/${currentMovieId}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(movieObj)
    });

    loadAllMovies();

    clearInputValues(); 

    addMovieBtnElement.removeAttribute('disabled');
    editMovieBtnElement.setAttribute('disabled', '');
}

function loadMoviesHandler() {
    loadAllMovies();
}

async function loadAllMovies() {
    const movies = (await getAllMovies()).map(createMovieElement);

    movieListDivElement.innerHTML = '';

    movieListDivElement.append(...movies);
}

async function getAllMovies() {
    const response = await fetch(baseUrl);
    const data = await response.json();

    return Object.values(data);
}

function createMovieElement(movieInfo) {
    const movieDivElement = document.createElement('div');
    movieDivElement.classList.add('movie');

    const contentDivElement = document.createElement('div');
    contentDivElement.classList.add('content');

    const pTitleElement = document.createElement('p');
    pTitleElement.textContent = movieInfo.title;

    const pDirectorElement = document.createElement('p');
    pDirectorElement.textContent = movieInfo.director;

    const pYearElement = document.createElement('p');
    pYearElement.textContent = movieInfo.year;

    contentDivElement.append(pTitleElement, pDirectorElement, pYearElement);

    const buttonsContainerDivElement = document.createElement('div');
    buttonsContainerDivElement.classList.add('buttons-container');

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('change-btn');
    editBtnElement.textContent = 'Change';
    editBtnElement.addEventListener('click', () => {
        currentMovieId = movieInfo._id;

        movieDivElement.remove();

        movieTitleInputElement.value = movieInfo.title;
        directorInputElement.value = movieInfo.director;
        yearInputElement.value = movieInfo.year;

        addMovieBtnElement.setAttribute('disabled', '');
        editMovieBtnElement.removeAttribute('disabled');
    });

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Remove';
    deleteBtnElement.addEventListener('click', async () => {
        currentMovieId = movieInfo._id;

        await fetch(`${baseUrl}/${currentMovieId}`, {
            method: 'DELETE',
        });

        loadAllMovies();
    });

    buttonsContainerDivElement.append(editBtnElement, deleteBtnElement);

    movieDivElement.append(contentDivElement, buttonsContainerDivElement);

    return movieDivElement;
}

function getInputValues() {
    const title = movieTitleInputElement.value;
    const director = directorInputElement.value;
    const year = yearInputElement.value;

    return {
        title, 
        director, 
        year
    };
}

function clearInputValues() {
    movieTitleInputElement.value = '';
    directorInputElement.value = '';
    yearInputElement.value = '';
}


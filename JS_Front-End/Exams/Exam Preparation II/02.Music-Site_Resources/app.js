window.addEventListener('load', solve);

function solve() {
    let totalLikes = 0;

    const genreInputElement = document.getElementById('genre');
    const songNameInputElement = document.getElementById('name');
    const authorInputElement = document.getElementById('author');
    const dateInputElement = document.getElementById('date');

    const allHitsContainerDivElement = document.querySelector('.all-hits-container');
    const savedContainerDivElement = document.querySelector('.saved-container'); 

    const totalLikesPElement = document.querySelector('#total-likes p');

    const addBtnElement = document.getElementById('add-btn');
    addBtnElement.addEventListener('click', addSongHandler);

    function addSongHandler(e) {
        e.preventDefault();

        const genre = genreInputElement.value;
        const songName = songNameInputElement.value;
        const author = authorInputElement.value;
        const date = dateInputElement.value;

        if(!genre || !songName || !author || !date) {
            return;
        }

        const hitsInfoDivElement = createSongElement(genre, songName, author, date);
        allHitsContainerDivElement.appendChild(hitsInfoDivElement);

        genreInputElement.value = '';
        songNameInputElement.value = '';
        authorInputElement.value = '';
        dateInputElement.value = '';
    }

    function createSongElement (genre, songName, author, date) {
        const hitsInfoDivElement = document.createElement('div');
        hitsInfoDivElement.classList.add('hits-info');

        const imgElement = document.createElement('img');
        imgElement.setAttribute('src', './static/img/img.png');
        hitsInfoDivElement.appendChild(imgElement);

        const genreHeaderElement = document.createElement('h2');
        genreHeaderElement.textContent = `Genre: ${genre}`;
        hitsInfoDivElement.appendChild(genreHeaderElement);

        const nameHeaderElement = document.createElement('h2');
        nameHeaderElement.textContent = `Name: ${songName}`;
        hitsInfoDivElement.appendChild(nameHeaderElement);

        const authorHeaderElement = document.createElement('h2');
        authorHeaderElement.textContent = `Author: ${author}`;
        hitsInfoDivElement.appendChild(authorHeaderElement);

        const dateHeaderElement = document.createElement('h3');
        dateHeaderElement.textContent = `Date: ${date}`;
        hitsInfoDivElement.appendChild(dateHeaderElement);

        const saveBtnElement = document.createElement('button');
        saveBtnElement.classList.add('save-btn');
        saveBtnElement.textContent = 'Save song';
        saveBtnElement.addEventListener('click', () => {
            saveBtnElement.remove();
            likeBtnElement.remove();

            savedContainerDivElement.appendChild(hitsInfoDivElement);
        });
        hitsInfoDivElement.appendChild(saveBtnElement);

        const likeBtnElement = document.createElement('button');
        likeBtnElement.classList.add('like-btn');
        likeBtnElement.textContent = 'Like song';
        likeBtnElement.addEventListener('click', () => {
            totalLikes += 1;
            totalLikesPElement.textContent = `Total Likes: ${totalLikes}`;
            likeBtnElement.setAttribute('disabled', '');
        });
        hitsInfoDivElement.appendChild(likeBtnElement);

        const deleteBtnElement = document.createElement('button');
        deleteBtnElement.classList.add('delete-btn');
        deleteBtnElement.textContent = 'Delete';
        deleteBtnElement.addEventListener('click', () => {
            hitsInfoDivElement.remove();
        })
        hitsInfoDivElement.appendChild(deleteBtnElement);

        return hitsInfoDivElement;
    }
}
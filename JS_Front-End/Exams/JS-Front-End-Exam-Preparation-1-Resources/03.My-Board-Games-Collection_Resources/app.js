const loadBtnElement = document.getElementById('load-games');
loadBtnElement.addEventListener('click', loadAllGamesHandler);

const addGameBtnElement = document.getElementById('add-game');
addGameBtnElement.addEventListener('click', addGameHandler);

const editGameBtnElement = document.getElementById('edit-game');
editGameBtnElement.addEventListener('click', editGameHandler);

const nameInputElement = document.getElementById('g-name');
const typeInputElement = document.getElementById('type');
const playersInputElement = document.getElementById('players');

const gamesListElement = document.getElementById('games-list');

let currentGameID = '';

async function loadAllGamesHandler(e) {
    await getAllGames();
}

async function addGameHandler(e) {
    const [name, type, players] = getGameInfo();

    if (!name || !type || !players) {
        return;
    }

    const gameObj = {
        name,
        type,
        players
    };

    await fetch('http://localhost:3030/jsonstore/games', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(gameObj)
    });

    clearInputFields();

    await getAllGames();
}

async function editGameHandler(e) {
    const [name, type, players] = getGameInfo();

    const gameObj = {
        name,
        type,
        players
    };

    await fetch(`http://localhost:3030/jsonstore/games/${currentGameID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'aplication/json'
        },
        body: JSON.stringify(gameObj)
    });

    await getAllGames();

    editGameBtnElement.setAttribute('disabled', '');
    addGameBtnElement.removeAttribute('disabled');

    clearInputFields();
}

async function getAllGames() {
    const response = await fetch('http://localhost:3030/jsonstore/games');
    const data = await response.json();
    const games = Object.values(data)
        .map(createGameElement);

    gamesListElement.innerHTML = '';

    gamesListElement.append(...games);
}

function createGameElement(gameInfo) {
    const gameElement = document.createElement('div');
    gameElement.classList.add('board-game');

    const gameContentElement = document.createElement('div');
    gameContentElement.classList.add('content');

    const pNameElement = document.createElement('p');
    pNameElement.textContent = gameInfo.name;
    const pTypeElement = document.createElement('p');
    pTypeElement.textContent = gameInfo.type;
    const pPlayersElement = document.createElement('p');
    pPlayersElement.textContent = gameInfo.players;

    gameContentElement.append(
        pNameElement,
        pTypeElement,
        pPlayersElement
    );

    const buttonsContainerElement = document.createElement('div');
    buttonsContainerElement.classList.add('buttons-container');

    const changeBtnElement = document.createElement('button');
    changeBtnElement.classList.add('change-btn');
    changeBtnElement.textContent = 'Change';
    changeBtnElement.addEventListener('click', () => {
        nameInputElement.value = gameInfo.name;
        typeInputElement.value = gameInfo.type;
        playersInputElement.value = gameInfo.players;

        addGameBtnElement.setAttribute('disabled', '');
        editGameBtnElement.removeAttribute('disabled');

        currentGameID = gameInfo._id;
    })

    const deleteBtnElement = document.createElement('button');
    deleteBtnElement.classList.add('delete-btn');
    deleteBtnElement.textContent = 'Delete';
    deleteBtnElement.addEventListener('click', async () => {
        currentGameID = gameInfo._id;
        
        await fetch(`http://localhost:3030/jsonstore/games/${currentGameID}`, {
        method: 'DELETE',
    });

    await getAllGames();
    });

    buttonsContainerElement.append(
        changeBtnElement,
        deleteBtnElement
    );

    gameElement.append(
        gameContentElement,
        buttonsContainerElement
    );

    return gameElement;
}

function getGameInfo() {
    const name = nameInputElement.value.trim();
    const type = typeInputElement.value.trim();
    const players = playersInputElement.value.trim();

    return [name, type, players];
}

function clearInputFields() {
    nameInputElement.value = '';
    typeInputElement.value = '';
    playersInputElement.value = '';
}



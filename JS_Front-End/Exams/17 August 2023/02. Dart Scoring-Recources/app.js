window.addEventListener("load", solve);

function solve() {
  const playerNameInputElement = document.getElementById('player');
  const scoreInputElement = document.getElementById('score');
  const roundInputElement = document.getElementById('round');

  const dartSureUlListElement = document.getElementById('sure-list');
  const scoreboardUlListElement = document.getElementById('scoreboard-list');

  const addBtnElement = document.getElementById('add-btn');
  addBtnElement.addEventListener('click', addScoreHandler);

  const clearBtnElement = document.querySelector('.clear');
  clearBtnElement.addEventListener('click', clearScoreboard);

  function addScoreHandler() {
    const playerName = playerNameInputElement.value.trim();
    const score = scoreInputElement.value.trim();
    const round = roundInputElement.value.trim();

    if (!playerName || !score || !round) {
      return;
    }

    const liElement = createScoreItemElement(playerName, score, round);
    dartSureUlListElement.appendChild(liElement);

    playerNameInputElement.value = '';
    scoreInputElement.value = '';
    roundInputElement.value = '';

    addBtnElement.setAttribute('disabled', '');
  }

  function clearScoreboard() {
    location.reload();
  }

  function createScoreItemElement(name, score, round) {
    const liElement = document.createElement('li');
    liElement.classList.add('dart-item');

    const articleElement = document.createElement('article');

    const pNameElement = document.createElement('p');
    pNameElement.textContent = name;
    articleElement.appendChild(pNameElement);

    const pScoreElement = document.createElement('p');
    pScoreElement.textContent = `Score: ${score}`;
    articleElement.appendChild(pScoreElement);

    const pRoundElement = document.createElement('p');
    pRoundElement.textContent = `Round: ${round}`;
    articleElement.appendChild(pRoundElement);

    const editBtnElement = document.createElement('button');
    editBtnElement.classList.add('btn', 'edit');
    editBtnElement.textContent = 'edit';
    editBtnElement.addEventListener('click', () => {
      playerNameInputElement.value = name;
      scoreInputElement.value = score;
      roundInputElement.value = round;

      liElement.remove();

      addBtnElement.removeAttribute('disabled');
    });

    const okBtnElement = document.createElement('button');
    okBtnElement.classList.add('btn', 'ok');
    okBtnElement.textContent = 'ok';
    okBtnElement.addEventListener('click', () => {
      editBtnElement.remove();
      okBtnElement.remove();

      scoreboardUlListElement.appendChild(liElement);

      addBtnElement.removeAttribute('disabled');
    });

    liElement.appendChild(articleElement);
    liElement.appendChild(editBtnElement);
    liElement.appendChild(okBtnElement);

    return liElement;
  }
}

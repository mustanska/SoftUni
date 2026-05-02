async function loadCommits() {
    const username = document.getElementById('username').value.trim();
    const repository = document.getElementById('repo').value.trim();

    const ulCommitsElement = document.getElementById('commits');
    ulCommitsElement.innerHTML = '';

    const res = await fetch(`https://api.github.com/repos/${username}/${repository}/commits`);
    const data = await res.json();

    if (!res.ok) {
        const liElement = document.createElement('li');
        liElement.textContent = `Error: ${res.status} (NotFound)`;

        ulCommitsElement.appendChild(liElement);

        return;
    }

    data.forEach(dataObj => {
        const liElement = document.createElement('li');
        liElement.textContent = `${dataObj.commit.author.name}: ${dataObj.commit.message}`;

        ulCommitsElement.appendChild(liElement);
    });
}
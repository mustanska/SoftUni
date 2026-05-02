async function loadRepos() {
	const username = document.getElementById('username').value.trim();
	const ulReposElement = document.getElementById('repos');

	ulReposElement.innerHTML = '';

	const res = await fetch(`https://api.github.com/users/${username}/repos`);
	const data = await res.json();


	try {
		data.forEach(dataObj => {
			const liElement = document.createElement('li');
			const alinkElement = document.createElement('a');
			alinkElement.href = dataObj.html_url;
			alinkElement.textContent = dataObj.full_name;

			liElement.appendChild(alinkElement);
			ulReposElement.appendChild(liElement);
		});
	} catch (err) {
		const liElement = document.createElement('li');
		liElement.textContent = err;

		ulReposElement.appendChild(liElement);
	}

}
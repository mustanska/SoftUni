async function loadRepos() {
   const responseElement = document.getElementById('res');

   const res = await fetch('https://api.github.com/users/testnakov/repos');
   const data = await res.text();

   responseElement.textContent = data;
}
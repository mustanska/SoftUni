function solve() {
   let towns = document.querySelectorAll('#towns li');
   let searchField = document.getElementById('searchText');

   let searchedWord = searchField.value;
   let matches = 0;

   for (const town of towns) {
      if(town.textContent.toLowerCase().includes(searchedWord.toLowerCase())) {
         town.style.textDecoration = 'underline';
         town.style.opacity = 1;
         town.style.fontWeight = 'bold';
         matches ++;
      }
   }

   let result = document.getElementById('result');
   result.textContent = `${matches} matches found`;
} 
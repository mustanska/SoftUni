function solve() {
   let tableRows = document.querySelectorAll('tbody tr');
   let searchField = document.getElementById('searchField');

   let searchedWord = searchField.value;

   tableRows.forEach(tr => tr.classList.remove('select'));

   if (searchedWord.length < 1) {
      return;
   }

   for (const row of tableRows) {
      const isMatch = Array.from(row.children)
         .some(td => td.textContent.toLowerCase().includes(searchedWord.toLowerCase()));

      if(isMatch) {
         row.classList.add('select');
      }
   }
}
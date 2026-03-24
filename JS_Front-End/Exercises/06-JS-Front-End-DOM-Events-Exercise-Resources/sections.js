document.addEventListener('DOMContentLoaded', solve);

function solve() {
   
   const submitBtn = document.querySelector('input[type=submit');
   
   submitBtn.addEventListener('click', handleGenerateButton);

   function handleGenerateButton(e) {
      e.preventDefault();

      const inputValues = document.querySelector('input[type=text').value.split(', ');
      const resultDiv = document.querySelector('#content');

      const sectionElements = inputValues.map((sectionTitle) => {
         const divElement = document.createElement('div');
         const elementTitle = document.createElement('p');
         divElement.appendChild(elementTitle);
         elementTitle.textContent = sectionTitle;
         elementTitle.style.display = 'none';

         return divElement;
      })

      resultDiv.append(...sectionElements);

      sectionElements.forEach((section) => {
         section.addEventListener('click', handeClickDivElement);
      })

      function handeClickDivElement(e) {
         const currentSection = e.currentTarget;
         currentSection.querySelector('p').style.display = 'block';
      }
   }
}
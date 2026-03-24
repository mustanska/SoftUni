document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const addBtn = document.querySelector('input[type=submit]');
    addBtn.addEventListener('click', addElementHandler);

    function addElementHandler(e) {
        e.preventDefault();

        const textInput = document.getElementById('newItemText');
        const valueInput = document.getElementById('newItemValue');

        const selectMenu = document.getElementById('menu');
        const optionElement = document.createElement('option');
        optionElement.textContent = textInput.value;
        optionElement.value = valueInput.value;

        textInput.value = '';
        valueInput.value = '';

        selectMenu.appendChild(optionElement);



    }
}
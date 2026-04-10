window.addEventListener("load", solve);

function solve() {
    const expenseTypeInputElement = document.getElementById('expense');
    const amountInputElement = document.getElementById('amount');
    const dateInputElement = document.getElementById('date');

    const previewUlListElement = document.getElementById('preview-list');
    const expensesUlListElement = document.getElementById('expenses-list');

    const addBtnElement = document.getElementById('add-btn');
    addBtnElement.addEventListener('click', addExpenseHandler);

    const deleteBtnElement = document.querySelector('.delete');
    deleteBtnElement.addEventListener('click', deleteExpensesHandler);

    function addExpenseHandler(e) {
        e.preventDefault();

        const expenseType = expenseTypeInputElement.value;
        const amount = amountInputElement.value;
        const date = dateInputElement.value;

        if(!expenseType || !amount || !date) {
            return;
        }

        const expenseLiElement = createExpenseElement(expenseType, amount, date);

        previewUlListElement.appendChild(expenseLiElement);

        expenseTypeInputElement.value = '';
        amountInputElement.value = '';
        dateInputElement.value = '';

        addBtnElement.setAttribute('disabled', '');
    }

    function deleteExpensesHandler() {
        location.reload();
    }

    function createExpenseElement(expenseType, amount, date) {
        const liElement = document.createElement('li');
        liElement.classList.add('expense-item');

        const articleElement = document.createElement('article');

        const pTypeElement = document.createElement('p');
        pTypeElement.textContent = `Type: ${expenseType}`;
        articleElement.appendChild(pTypeElement);

        const pAmountElement = document.createElement('p');
        pAmountElement.textContent = `Amount: ${amount}$`;
        articleElement.appendChild(pAmountElement);

        const pDateElement = document.createElement('p');
        pDateElement.textContent = `Date: ${date}`;
        articleElement.appendChild(pDateElement);

        const buttonsDivElement = document.createElement('div');
        buttonsDivElement.classList.add('buttons');

        const editBtnElement = document.createElement('button');
        editBtnElement.classList.add('btn', 'edit');
        editBtnElement.textContent = 'edit';
        buttonsDivElement.appendChild(editBtnElement);
        editBtnElement.addEventListener('click', () => {
            expenseTypeInputElement.value = expenseType;
            amountInputElement.value = amount;
            dateInputElement.value = date;

            liElement.remove();

            addBtnElement.removeAttribute('disabled');
        })

        const okBtnElement = document.createElement('button');
        okBtnElement.classList.add('btn', 'ok');
        okBtnElement.textContent = 'ok';
        buttonsDivElement.appendChild(okBtnElement);
        okBtnElement.addEventListener('click', () => {
            buttonsDivElement.remove();

            expensesUlListElement.appendChild(liElement);

            addBtnElement.removeAttribute('disabled');
        });

        liElement.appendChild(articleElement);
        liElement.appendChild(buttonsDivElement);

        return liElement;
    }
}
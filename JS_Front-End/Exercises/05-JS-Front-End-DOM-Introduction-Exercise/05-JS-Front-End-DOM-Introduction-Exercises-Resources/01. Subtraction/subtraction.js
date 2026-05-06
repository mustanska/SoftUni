function subtract() {
    let firstNumberInput = document.getElementById('firstNumber');
    let secondNumberInput = document.getElementById('secondNumber');

    let firstNumber = Number(firstNumberInput.value);
    let secondNumber = Number(secondNumberInput.value);

    let result = document.getElementById('result');
    result.textContent = firstNumber - secondNumber;
}
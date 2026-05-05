function factorialDivision(firstNum, secondNum) {
    let dividedResult = factorial(firstNum) / factorial(secondNum);

    console.log(dividedResult.toFixed(2));
    

    function factorial(number) {
        if (number <= 0) {
            return 1;
        } else {
            return factorial(number - 1) * number;
        }
    }
}

factorialDivision(5, 2);
factorialDivision(6, 2);
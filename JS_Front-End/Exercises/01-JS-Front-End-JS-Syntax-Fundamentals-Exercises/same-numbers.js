function sameNumbers(number) {
    let isSame = 'true';
    let numberAsString = number.toString();
    let sum = Number(numberAsString[0]);

    for (let i = 1; i < numberAsString.length; i++) {
        let previousNumber = numberAsString[i - 1];

        if (!(previousNumber == numberAsString[i])) {
            isSame = 'false';
        }

        sum += Number(numberAsString[i]);
    }

    console.log(isSame);
    console.log(sum);
    
}


sameNumbers(2222222);
sameNumbers(1234);
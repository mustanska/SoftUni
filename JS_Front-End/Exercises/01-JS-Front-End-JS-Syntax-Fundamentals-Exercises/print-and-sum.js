function sumBetweenTwoNumbers(startNumber, endNumber) {
    let numbersAsString = '';
    let count = endNumber - startNumber + 1;
    let sum = 0;

    for(let i = 0; i < count; i++) {
        numbersAsString += (startNumber + i).toString() + " ";
        sum += startNumber + i;
    }

    console.log(numbersAsString);
    console.log(`Sum: ${sum}`);
    
}

sumBetweenTwoNumbers(5, 10);
sumBetweenTwoNumbers(0, 26);
sumBetweenTwoNumbers(50, 60);
function numberModification(number){
    let numberAsString = number.toString();

    let averageValue = getAverageValue(numberAsString);

    while(averageValue <=5){
        numberAsString += '9';

        averageValue = getAverageValue(numberAsString);
    }

    console.log(Number(numberAsString));
    

    function getAverageValue(numberAsString){
        let sum = 0;

        for(let i = 0; i < numberAsString.length; i++){
            sum += Number(numberAsString[i]);
        }

        return sum / numberAsString.length;
    }
    
}

numberModification(101);
numberModification(5835);
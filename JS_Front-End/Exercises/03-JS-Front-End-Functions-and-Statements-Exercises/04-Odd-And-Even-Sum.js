function oddAndEvenSum(number){
    let oddDigitsArray = getOddDigits(number);
    let evenDigitsArray = getEvenDigits(number);

    let oddDigitsSum = sum(oddDigitsArray);
    let evenDigitsSum = sum(evenDigitsArray);

    console.log(`Odd sum = ${oddDigitsSum}, Even sum = ${evenDigitsSum}`);
    

    function getOddDigits(number){
        let oddDigitsAsArray = number
            .toString()
            .split('')
            .filter((number) => number % 2 !== 0)
            .map((character) => Number(character));
            
        return oddDigitsAsArray;
    }

    function getEvenDigits(number){
        let evenDigitsAsArray = number
                                .toString()
                                .split('')
                                .filter((number) => number % 2 === 0)
                                .map((character) => Number(character));
            
        return evenDigitsAsArray;
    }

    function sum(digitsArray){
        let sumDigits = digitsArray.reduce((acc, digit) => digit + acc, 0);

        return sumDigits;
    }
}

oddAndEvenSum(1000435);
oddAndEvenSum(3495892137259234);
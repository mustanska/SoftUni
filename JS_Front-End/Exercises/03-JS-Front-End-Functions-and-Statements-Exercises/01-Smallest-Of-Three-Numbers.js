function smallestOfThreeNumbers(firstNum, secondNum, thirdNum){
    let smallestNumber = findSmallestNumber(firstNum, secondNum, thirdNum);

    console.log(smallestNumber);
    

    function findSmallestNumber(...numbers){
        let smallest = Number.MAX_SAFE_INTEGER;

        for (const number of numbers) {
            if(number < smallest){
                smallest = number;
            }
        }

        return smallest;
    }
}

smallestOfThreeNumbers(2, 5, 3);
smallestOfThreeNumbers(600, 342, 123);
smallestOfThreeNumbers(25, 21, 4);
smallestOfThreeNumbers(2, 2, 2);
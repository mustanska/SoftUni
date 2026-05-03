function printEveryNthArrayElement(array, step){
    let result = array.filter((_, index) => index % step === 0);

    return result;
    
}

console.log(printEveryNthArrayElement(['5',  '20',  '31',  '4',  '20'],  2));
console.log(printEveryNthArrayElement(['dsa', 'asd',  'test',  'tset'],  2));
console.log(printEveryNthArrayElement(['1',  '2', '3',  '4',  '5'],  6));
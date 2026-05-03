function cookingByNumbers(
    numberAsString,
    operation1,
    operation2,
    operation3,
    operation4,
    operation5,
){
    let number = Number(numberAsString);
    number = setOperationToNumber(number, operation1);
    console.log(number);
    
    number = setOperationToNumber(number, operation2);
    console.log(number);

    number = setOperationToNumber(number, operation3);
    console.log(number);

    number = setOperationToNumber(number, operation4);
    console.log(number);

    number = setOperationToNumber(number, operation5);
    console.log(number);

    function setOperationToNumber(number, operation){
        if(operation == 'chop'){
            return number / 2;
        }
        if(operation == 'dice'){
            return Math.sqrt(number);
        }
        if(operation == 'spice'){
            return number + 1;
        }
        if(operation == 'bake'){
            return number * 3;
        }
        if(operation == 'fillet'){
            return number -= number * 0.2;
        }
    }
}

cookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
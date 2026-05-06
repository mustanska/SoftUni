function solve(inputArray) {
    const parking = {}

    for (const row of inputArray) {
        let [direction, carNumber] = row.split(', ');

        if (direction === 'IN') {
            parking[carNumber] = true;
        }else if(direction === 'OUT') {
            delete parking[carNumber];
        }
    }

    const sortedParcingCars = Object.keys(parking)
        .sort((a, b) => a.localeCompare(b));

    if(sortedParcingCars.length > 0) {
        sortedParcingCars.forEach(carNumber => console.log(carNumber));
    } else {
        console.log('Parking Lot is Empty');
        
    }
}

solve([
    'IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU'
]);
solve([
    'IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA',
    'OUT, CA2866HI'
]);
function solve(inputArr) {
    const baristasCount = Number(inputArr.shift());
    const baristas = {};

    for(let i = 0; i < baristasCount; i++) {
        const [baristaName, shift, coffees] = inputArr.shift().split(' ');
        const coffeeTypes = coffees.split(',');

        baristas[baristaName] = {
            shift,
            coffeeTypes
        };
    }

    let commandLine = inputArr.shift();
    while(commandLine !== 'Closed') {
        const [command, baristaName, ...args] = commandLine.split(' / ');

        switch (command) {
            case 'Prepare':
                const [shift, coffeeType] = args;
                
                if(baristas[baristaName].shift === shift && baristas[baristaName].coffeeTypes.includes(coffeeType)) {
                    console.log(`${baristaName} has prepared a ${coffeeType} for you!`);
                } else {
                    console.log(`${baristaName} is not available to prepare a ${coffeeType}.`);
                }

                break;
            case 'Change Shift':
                const newShift = args[0];

                baristas[baristaName].shift = newShift;
                console.log(`${baristaName} has updated his shift to: ${newShift}`);
                
                break;
            case 'Learn':
                const newCoffeeType = args[0];

                if(baristas[baristaName].coffeeTypes.includes(newCoffeeType)) {
                    console.log(`${baristaName} knows how to make ${newCoffeeType}.`);
                } else {
                    baristas[baristaName].coffeeTypes.push(newCoffeeType);
                    console.log(`${baristaName} has learned a new coffee type: ${newCoffeeType}.`);
                }

                break;
        }

        commandLine = inputArr.shift();
    }

    for (const name in baristas) {
        let result = `Barista: ${name}, Shift: ${baristas[name].shift}, `;
        result += `Drinks: ${baristas[name].coffeeTypes.join(', ')}`;

        console.log(result);   
    }
}

solve([
    '3',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / night',
    'Learn / Carol / Latte',
    'Learn / Bob / Latte',
    'Prepare / Bob / night / Latte',
    'Closed'
]);
solve([
    '4',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'David night Espresso',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / day',
    'Learn / Carol / Latte',
    'Prepare / Bob / night / Latte',
    'Learn / David / Cappuccino',
    'Prepare / Carol / day / Cappuccino',
    'Change Shift / Alice / night',
    'Learn / Bob / Mocha',
    'Prepare / David / night / Espresso',
    'Closed'
]);
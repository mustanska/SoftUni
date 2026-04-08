function solve(inputArr) {
    const chemicalsCount = Number(inputArr.shift());

    const chemicals = {}

    for (let i = 0; i < chemicalsCount; i++) {
        const chemicalsInfo = inputArr.shift().split(' # ');
        const name = chemicalsInfo[0];
        const quantity = Number(chemicalsInfo[1]);

        chemicals[name] = {quantity};
    }

    let commandLine = inputArr.shift();
    while(commandLine !== 'End') {
        const [command, chemicalName, ...args] = commandLine.split(' # ');
        let amount = Number.MIN_SAFE_INTEGER;

        switch (command) {
            case 'Mix':
                const secondChemicalName = args[0];
                amount = Number(args[1]);

                if(chemicals[chemicalName].quantity < amount || chemicals[secondChemicalName].quantity < amount) {
                    console.log(`Insufficient quantity of ${chemicalName}/${secondChemicalName} to mix.`);
                    
                    break;
                }

                chemicals[chemicalName].quantity -= amount;
                chemicals[secondChemicalName].quantity -= amount;

                console.log(`${chemicalName} and ${secondChemicalName} have been mixed. ${amount} units of each were used.`);
                
                break;
            case 'Replenish':
                amount = Number(args[0]);
                
                if(!chemicals.hasOwnProperty(chemicalName)) {
                    console.log(`The Chemical ${chemicalName} is not available in the lab.`);
                    
                    break;
                }

                if (chemicals[chemicalName].quantity + amount >= 500) {
                    const addedAmount = 500 - chemicals[chemicalName].quantity;
                    chemicals[chemicalName].quantity = 500;

                    console.log(`${chemicalName} quantity increased by ${addedAmount} units, reaching maximum capacity of 500 units!`);
                } else {
                    chemicals[chemicalName].quantity += amount;

                    console.log(`${chemicalName} quantity increased by ${amount} units!`); 
                }

                break;
            case 'Add Formula':
                const formula = args[0];

                if(!chemicals.hasOwnProperty(chemicalName)) {
                    console.log(`The Chemical ${chemicalName} is not available in the lab.`);
                    
                    break;
                }

                chemicals[chemicalName].formula = formula;
                console.log(`${chemicalName} has been assigned the formula ${formula}.`);
                

                break;
        }

        commandLine = inputArr.shift();
    }

    for (const chemicalName in chemicals) {
        const result = [`Chemical: ${chemicalName}`];
        result.push(`Quantity: ${chemicals[chemicalName].quantity}`);

        if(chemicals[chemicalName].formula) {
            result.push(`Formula: ${chemicals[chemicalName].formula}`);
        }

        console.log(result.join(', '));
    }
}

solve([
    '4',
    'Water # 200',
    'Salt # 100',
    'Acid # 50',
    'Base # 80',
    'Mix # Water # Salt # 50',
    'Replenish # Salt # 150',
    'Add Formula # Acid # H2SO4',
    'End'
]);
solve([
    '3',
    'Sodium # 300',
    'Chlorine # 100',
    'Hydrogen # 200',
    'Mix # Sodium # Chlorine # 200',
    'Replenish # Sodium # 250',
    'Add Formula # Sulfuric Acid # H2SO4',
    'Add Formula # Sodium # Na',
    'Mix # Hydrogen # Chlorine # 50',
    'End'
]);
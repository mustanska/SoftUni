function solve(inputArr) {
    const astronautsCount = Number(inputArr.shift());
    const astronauts = {};

    for (let i = 0; i < astronautsCount; i++) {
        const astonautInfo = inputArr.shift().split(' ');
        const name = astonautInfo[0];
        const oxygenLevel = Number(astonautInfo[1]);
        const reservedEnergy = Number(astonautInfo[2]);

        astronauts[name] = {oxygenLevel, reservedEnergy};
    }

    let commandLine = inputArr.shift();
    while(commandLine !== 'End') {
        const [command, astronautName, amount] = commandLine.split(' - ');

        switch (command) {
            case 'Explore':
                const energyUsed = Number(amount);

                if (astronauts[astronautName].reservedEnergy >= energyUsed) {
                    astronauts[astronautName].reservedEnergy -= energyUsed;

                    console.log(`${astronautName} has successfully explored a new area and now has ${astronauts[astronautName].reservedEnergy} energy!`);
                } else {
                    console.log(`${astronautName} does not have enough energy to explore!`);
                }

                break;
            case 'Refuel':
                const missingEnergy = 200 -  astronauts[astronautName].reservedEnergy;
                const energyForRecovering = Number(amount);

                const recoveredEnergy = Math.min(energyForRecovering, missingEnergy);
                astronauts[astronautName].reservedEnergy += recoveredEnergy;

                console.log(`${astronautName} refueled their energy by ${recoveredEnergy}!`);

                break;
            case 'Breathe':
                const missingOxygen = 100 - astronauts[astronautName].oxygenLevel;
                const oxygenForRecovering = Number(amount);

                const recoveredOxygen = Math.min(oxygenForRecovering, missingOxygen);
                astronauts[astronautName].oxygenLevel += recoveredOxygen;

                console.log(`${astronautName} took a breath and recovered ${recoveredOxygen} oxygen!`);
                
                break;
        }

        commandLine = inputArr.shift();
    } 

    for (const astronautName in astronauts) {
        let result = `Astronaut: ${astronautName}, `;
        result += `Oxygen: ${astronauts[astronautName].oxygenLevel}, `;
        result += `Energy: ${astronauts[astronautName].reservedEnergy}`;

        console.log(result);
    }
}

solve([
    '3',
    'John 50 120',
    'Kate 80 180',
    'Rob 70 150',
    'Explore - John - 50',
    'Refuel - Kate - 30',
    'Breathe - Rob - 20',
    'End'
]);
solve([
    '4',
    'Alice 60 100',
    'Bob 40 80',
    'Charlie 70 150',
    'Dave 80 180',
    'Explore - Bob - 60',
    'Refuel - Alice - 30',
    'Breathe - Charlie - 50',
    'Refuel - Dave - 40',
    'Explore - Bob - 40',
    'Breathe - Charlie - 30',
    'Explore - Alice - 40',
    'End'
]);
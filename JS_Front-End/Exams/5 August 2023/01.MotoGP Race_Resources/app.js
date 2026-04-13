function solve(inputArr) {
    const ridersCount = Number(inputArr.shift());
    const riders = {}

    for (let i = 0; i < ridersCount; i++) {
        const args = inputArr.shift().split('|');
        const rider = args[0];
        const fuelCapacity = Number(args[1]);
        const position = Number(args[2]);

        riders[rider] = {fuelCapacity, position};
    }

    let commandLine = inputArr.shift();

    while(commandLine !== 'Finish') {
        const [command, rider, ...args] = commandLine.split(' - ');

        switch (command) {
            case 'StopForFuel':
                const minimumFuel = Number(args[0]);
                const changedPosition = Number(args[1]);

                if (riders[rider].fuelCapacity < minimumFuel) {
                    riders[rider].position = changedPosition;

                    console.log(`${rider} stopped to refuel but lost his position, now he is ${changedPosition}.`);
                } else {
                    console.log(`${rider} does not need to stop for fuel!`);   
                }
                break;
            case 'Overtaking':
                const secondRider = args[0];
                const firstRiderPosition = riders[rider].position;
                const secondRiderPosition = riders[secondRider].position;

                if (firstRiderPosition >= secondRiderPosition) {
                    break;
                }

                riders[rider].position = secondRiderPosition;
                riders[secondRider].position = firstRiderPosition;

                console.log(`${rider} overtook ${secondRider}!`);

                break;
            case 'EngineFail':
                const lapsLeft = Number(args[0]);
                delete riders[rider];

                console.log(`${rider} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`);
                
                break;
        }
        commandLine = inputArr.shift();
    }

    for (const rider in riders) {
        console.log(`${rider}\n  Final position: ${riders[rider].position}`);
    }
}

solve([
    "3",
    "Valentino Rossi|100|1",
    "Marc Marquez|90|2",
    "Jorge Lorenzo|80|3",
    "StopForFuel - Valentino Rossi - 50 - 1",
    "Overtaking - Marc Marquez - Jorge Lorenzo",
    "EngineFail - Marc Marquez - 10",
    "Finish"
]);
solve([
    "4",
    "Valentino Rossi|100|1",
    "Marc Marquez|90|3",
    "Jorge Lorenzo|80|4",
    "Johann Zarco|80|2",
    "StopForFuel - Johann Zarco - 90 - 5",
    "Overtaking - Marc Marquez - Jorge Lorenzo",
    "EngineFail - Marc Marquez - 10",
    "Finish"
]);

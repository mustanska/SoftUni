function solve(inputArr) {
    const horses = inputArr.shift().split('|');

    let commandLine = inputArr.shift();
    while (commandLine !== 'Finish') {
        const [command, ...args] = commandLine.split(' ');

        const horseName = args[0];
        const horseIndex = horses.indexOf(horseName);

        switch (command) {
            case 'Retake':
                const overtakenHorse = args[1];
                const overtakenHorseIndex = horses.indexOf(overtakenHorse);

                if (horseIndex > overtakenHorseIndex) {
                    break;
                }

                swapElements(horseIndex, overtakenHorseIndex)
                console.log(`${horseName} retakes ${overtakenHorse}.`);

                break;
            case 'Trouble':
                if (horseIndex <= 0) {
                    break;
                }

                swapElements(horseIndex - 1, horseIndex);
                console.log(`Trouble for ${horseName} - drops one position.`);

                break;
            case 'Rage':
                horses.splice(horseIndex, 1);
                horses.splice(horseIndex + 2, 0, horseName);
                console.log(`${horseName} rages 2 positions ahead.`);

                break;
            case 'Miracle':
                const lastHorse = horses.shift();
                horses.push(lastHorse);
                console.log(`What a miracle - ${lastHorse} becomes first.`);
                break;
        }

        commandLine = inputArr.shift();
    }

    console.log(horses.join('->'));
    console.log(`The winner is: ${horses[horses.length - 1]}`);

    function swapElements(firstIndex, secondIndex) {
        [horses[firstIndex], horses[secondIndex]] = [horses[secondIndex], horses[firstIndex]];
    }
}

solve([
    'Bella|Alexia|Sugar',
    'Retake Alexia Sugar',
    'Rage Bella',
    'Trouble Bella',
    'Finish'
]);
solve([
    'Onyx|Domino|Sugar|Fiona',
    'Trouble Onyx',
    'Retake Onyx Sugar',
    'Rage Domino',
    'Miracle',
    'Finish'
]);
solve([
    'Fancy|Lilly',
    'Retake Lilly Fancy',
    'Trouble Lilly',
    'Trouble Lilly',
    'Finish',
    'Rage Lilly'
]);
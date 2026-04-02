function solve(inputArr) {
    const charactersNumber = Number(inputArr.shift());
    const characters = {}

    for (let i = 0; i < charactersNumber; i++) {
        const row = inputArr.shift().split(' ');
        const heroName = row[0];
        const hp = Math.min(Number(row[1]), 100);
        const bullets = Number(row[2]);

        characters[heroName] = {
            hp,
            bullets
        };
    }

    let commandLine = inputArr.shift();

    while (commandLine !== 'Ride Off Into Sunset') {
        const [command, heroName, ...args] = commandLine.split(' - ');

        switch (command) {
            case 'FireShot':
                const target = args[0];
                if (characters[heroName].bullets > 0) {
                    characters[heroName].bullets--;
                    console.log(`${heroName} has successfully hit ${target} and now has ${characters[heroName].bullets} bullets!`);
                } else {
                    console.log(`${heroName} doesn't have enough bullets to shoot at ${target}!`);
                }
                break;
            case 'TakeHit':
                const damage = Number(args[0]);
                const attacker = args[1];

                characters[heroName].hp -= damage;

                if (characters[heroName].hp > 0) {
                    console.log(`${heroName} took a hit for ${damage} HP from ${attacker} and now has ${characters[heroName].hp} HP!`);
                } else {
                    console.log(`${heroName} was gunned down by ${attacker}!`);
                    delete characters[heroName];
                }
                break;
            case 'Reload':
                const bulletsMaxCapacity = 6;
                const reloadedBulletsCount = bulletsMaxCapacity - characters[heroName].bullets;
                if (reloadedBulletsCount > 0) {
                    characters[heroName].bullets = bulletsMaxCapacity;
                    console.log(`${heroName} reloaded ${reloadedBulletsCount} bullets!`);
                } else {
                    console.log(`${heroName}'s pistol is fully loaded!`);
                }
                break;
            case 'PatchUp':
                const amount = Number(args[0]);
                const fullHealth = 100;
                const recoveredAmount = Math.min(fullHealth - characters[heroName].hp, amount);

                if (characters[heroName].hp < fullHealth) {
                    characters[heroName].hp += recoveredAmount;
                    console.log(`${heroName} patched up and recovered ${recoveredAmount} HP!`);
                } else {
                    console.log(`${heroName} is in full health!`);
                }
                break;
        }

        commandLine = inputArr.shift();
    }

    Object.entries(characters)
        .forEach(printCharacter);

    function printCharacter(characterInfo) {
        let result = [];
        result.push(`${characterInfo[0]}`);
        result.push(`  HP: ${characterInfo[1].hp}`);
        result.push(`  Bullets: ${characterInfo[1].bullets}`);

        console.log(result.join('\n'));
    }
}

solve([
    "2",
    "Gus 100 0",
    "Walt 100 6",
    "FireShot - Gus - Bandit",
    "TakeHit - Gus - 100 - Bandit",
    "Reload - Walt",
    "Ride Off Into Sunset"
]);

solve([
    "2",
    "Jesse 100 4",
    "Walt 100 5",
    "FireShot - Jesse - Bandit",
    "TakeHit - Walt - 30 - Bandit",
    "PatchUp - Walt - 20",
    "Reload - Jesse",
    "Ride Off Into Sunset"
]);
solve([
    "2",
    "Gus 100 4",
    "Walt 100 5",
    "FireShot - Gus - Bandit",
    "TakeHit - Walt - 100 - Bandit",
    "Reload - Gus",
    "Ride Off Into Sunset"
]);
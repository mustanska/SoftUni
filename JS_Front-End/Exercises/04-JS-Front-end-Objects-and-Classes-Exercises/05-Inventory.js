function solve(inputArray) {
    const heroes = []
    
    for (const row of inputArray) {
        let [heroName, levelString, items] = row.split(' / ');
        let level = Number(levelString);
        
        const heroObj = {
            heroName,
            level,
            items
        }

        heroes.push(heroObj);
    }

    heroes
        .sort((a, b) => a.level - b.level)
        .forEach(hero => {
            console.log(`Hero: ${hero.heroName}`);
            console.log(`level => ${hero.level}`);
            console.log(`items => ${hero.items}`);
        })
}

solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
]);
solve([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
]);
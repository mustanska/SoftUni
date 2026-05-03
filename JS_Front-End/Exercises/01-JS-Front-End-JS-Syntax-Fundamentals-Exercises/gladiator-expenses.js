function gladiatorExpenses(
    lostFightsCount,
    helmetPrice,
    swordPrice,
    shieldPrice,
    armorPrice,
) {
    let expenses = 0;
    let helmetBrokenCount = 0;
    let swordBrokenCount = 0;
    let shieldBrokenCount = 0;
    let armorBrokenCount = 0;

    for (let i = 1; i <= lostFightsCount; i++) {
        if (i % 2 == 0) {
            helmetBrokenCount += 1;
        }

        if (i % 3 == 0) {
            swordBrokenCount += 1;
        }

        if (i % 2 == 0 && i % 3 == 0) {
            shieldBrokenCount += 1;

            if (!(shieldBrokenCount == 0) && shieldBrokenCount % 2 == 0) {
                armorBrokenCount += 1;
            }
        }
    }

    expenses = helmetBrokenCount * helmetPrice + swordBrokenCount * swordPrice + shieldBrokenCount * shieldPrice + armorBrokenCount * armorPrice;
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);

}

gladiatorExpenses(7, 2, 3, 4, 5);
gladiatorExpenses(23, 12.50, 21.50, 40, 200);
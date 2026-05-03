function pyramidOfKingDjoser(base, increment) {
    let stoneCount = 0;
    let marbleCount = 0;
    let lapisLazuliCount = 0;
    let goldCount = 0;
    let heigth = 0;
    let layers = 0;

    for (let i = base; i > 0; i -= 2) {

        layers += 1;
        heigth += increment;

        if (i - 2 <= 0) {
            goldCount = i * i * increment;
            break;
        }

        stoneCount += (i - 2) * (i - 2) * increment;

        if (layers % 5 === 0) {
            lapisLazuliCount += (i * 4 - 4) * increment;
        } else {
            marbleCount += (i * 4 - 4) * increment;
        }
    }

    console.log(`Stone required: ${Math.ceil(stoneCount)}`);
    console.log(`Marble required: ${Math.ceil(marbleCount)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuliCount)}`);
    console.log(`Gold required: ${Math.ceil(goldCount)}`);
    console.log(`Final pyramid height: ${Math.floor(heigth)}`);

}

pyramidOfKingDjoser(11, 1);
pyramidOfKingDjoser(11, 0.75);
pyramidOfKingDjoser(12, 1);
pyramidOfKingDjoser(23, 0.5);
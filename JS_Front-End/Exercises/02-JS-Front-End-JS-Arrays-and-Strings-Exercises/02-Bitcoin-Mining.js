function bitcoinMining(arrayOfNumbers){
    const bitcoin = 11949.16;
    const oneGramOfGold = 67.51;
    let totalPrice = 0;
    let boughtBitcoins = 0;
    let firstDayOfPurchasedBitcoin = 0;

    for(let i = 1; i < arrayOfNumbers.length + 1; i++){
        if(i % 3 === 0){
            arrayOfNumbers[i - 1] -= arrayOfNumbers[i - 1] * 0.3;
        }

        totalPrice += arrayOfNumbers[i - 1] * oneGramOfGold;

        while(totalPrice >= bitcoin){
            totalPrice -= bitcoin;
            boughtBitcoins += 1;

            if(!firstDayOfPurchasedBitcoin){
                firstDayOfPurchasedBitcoin = i;
            }
        }
    }

    console.log( `Bought bitcoins: ${boughtBitcoins}`);
    if(boughtBitcoins){
        console.log( `Day of the first purchased bitcoin: ${firstDayOfPurchasedBitcoin}`);   
    }
    console.log( `Left money: ${totalPrice.toFixed(2)} lv.`);
    
}

bitcoinMining([100, 200, 300]);
bitcoinMining([50, 100]);
bitcoinMining([3124.15, 504.212, 2511.124]);
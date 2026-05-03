function spiceMustFlow(startingYield){
    let days = 0;
    let spiceTotalAmount = 0;

    while(startingYield >= 100){
        spiceTotalAmount += startingYield - 26;
        startingYield -= 10;
        days += 1;
    }

    if(spiceTotalAmount >= 26){
        spiceTotalAmount -= 26;
    }

    console.log(days);
    console.log(spiceTotalAmount);
    
    
}

spiceMustFlow(111);
spiceMustFlow(450);
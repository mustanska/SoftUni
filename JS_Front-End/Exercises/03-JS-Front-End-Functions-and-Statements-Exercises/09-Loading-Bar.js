function loadingBar(number) {
    let bar = printLoadingBar(number);

    if (number < 100) {
        console.log(`${number}% ${bar}`);
        console.log('Still loading...');
    } else {
        console.log(`${number}% Complete!`);
        console.log(bar);
    }


    function printLoadingBar(number) {
        let completeSteps = number / 10;
        let pendingSteps = 10 - completeSteps;

        return `[${'%'.repeat(completeSteps)}${'.'.repeat(pendingSteps)}]`
    }
}

loadingBar(30);
loadingBar(50);
loadingBar(100);
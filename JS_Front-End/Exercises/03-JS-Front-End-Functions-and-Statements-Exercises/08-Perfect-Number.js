function perfectNumber(number) {
    if (sumDivisors(number) === number) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }

    function sumDivisors(number) {
        let sumDivisors = 0;

        for (i = 1; i <= number / 2; i++) {
            if (number % i === 0) {
                sumDivisors += i;
            }
        }

        return sumDivisors;
    }
}

perfectNumber(6);
perfectNumber(28);
perfectNumber(1236498);
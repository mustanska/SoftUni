function findLeapYear(year) {
    let isLeap = false;

    if ((!(year % 100 == 0) && year % 4 == 0) || year % 400 == 0) {
        isLeap = true;
    }

    if (isLeap) {
        console.log('yes');
    } else {
        console.log('no');

    }

}

findLeapYear(1984);
findLeapYear(2003);
findLeapYear(4);
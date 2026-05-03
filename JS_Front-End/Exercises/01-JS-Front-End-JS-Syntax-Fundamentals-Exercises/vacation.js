function vacation(peopleCount, groupType, weekDay) {
    let singlePrice = getSinglePrice(groupType, weekDay);
    let discount = getDiscount(groupType, peopleCount, singlePrice);
    let totalPrice = peopleCount * singlePrice - discount;

    console.log(`Total price: ${totalPrice.toFixed(2)}`);

    function getSinglePrice(groupType, weekDay) {
        switch (groupType) {
            case 'Students':
                if (weekDay == 'Friday') {
                    return 8.45;
                } else if (weekDay == 'Saturday') {
                    return 9.80;
                } else if (weekDay == 'Sunday') {
                    return 10.46;
                }
            case 'Business':
                if (weekDay == 'Friday') {
                    return 10.90;
                } else if (weekDay == 'Saturday') {
                    return 15.60;
                } else if (weekDay == 'Sunday') {
                    return 16;
                }
            case 'Regular':
                if (weekDay == 'Friday') {
                    return 15;
                } else if (weekDay == 'Saturday') {
                    return 20;
                } else if (weekDay == 'Sunday') {
                    return 22.50;
                }
        }
    }

    function getDiscount(groupType, peopleCount, singlePrice) {
        let discount = 0;


        if (groupType === 'Students' && peopleCount >= 30) {
            discount = peopleCount * singlePrice * 0.15;
        }
        if (groupType === 'Business' && peopleCount >= 100) {
            discount = 10 * singlePrice;
        }
        if (groupType === 'Regular' && peopleCount >= 10 && peopleCount <= 20) {
            discount = peopleCount * singlePrice * 0.05;
        }

        return discount;
    }
}

vacation(30, "Students", "Sunday");
vacation(29, "Students", "Friday");
vacation(31, "Students", "Saturday");
vacation(100, "Business", "Friday");
vacation(99, "Business", "Saturday");
vacation(101, "Business", "Sunday");
vacation(40, "Regular", "Saturday");
vacation(21, "Regular", "Sunday");
vacation(9, "Regular", "Friday");
vacation(15, "Regular", "Saturday");
vacation(20, "Regular", "Saturday");
vacation(10, "Regular", "Saturday");
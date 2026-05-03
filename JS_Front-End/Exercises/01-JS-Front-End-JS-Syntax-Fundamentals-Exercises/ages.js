function ages(age) {
    let person = '';

    if (age > 65) {
        person = 'elder';
    } else if (age > 19) {
        person = 'adult';
    } else if (age > 13) {
        person = 'teenager';
    } else if (age > 2) {
        person = 'child';
    } else if (age >= 0) {
        person = 'baby';
    } else {
        person = 'out of bounds';
    }

    return console.log(person);
}

ages(20);
ages(1);
ages(100);
ages(-1);
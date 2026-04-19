function solve(inputArr) {
    const products = inputArr.shift().split('!');

    let commandLine = inputArr.shift();

    while (commandLine !== 'Go Shopping!') {
        const [command, item, ...args] = commandLine.split(' ');
        const indexItem = products.indexOf(item);

        switch (command) {
            case 'Urgent':
                if (products.includes(item)) {
                    break;
                }

                products.unshift(item);

                break;
            case 'Unnecessary':
                if (!products.includes(item)) {
                    break;
                }

                products.splice(indexItem, 1);
                break;
            case 'Correct':
                const newItem = args[0];

                if (!products.includes(item)) {
                    break;
                }

                products.splice(indexItem, 1, newItem);

                break;
            case 'Rearrange':
                if (!products.includes(item)) {
                    break;
                }

                products.push(products.splice(indexItem, 1));

                break;
        }

        commandLine = inputArr.shift();
    }

    console.log(products.join(', '));
    
}

solve([
    "Tomatoes!Potatoes!Bread",
    "Unnecessary Milk",
    "Urgent Tomatoes",
    "Go Shopping!"
]);
solve([
    "Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Unnecessary Grapes",
    "Correct Pepper Onion",
    "Rearrange Grapes",
    "Correct Tomatoes Potatoes",
    "Go Shopping!"
]);
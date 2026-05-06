function solve(input) {
    let elements = input.split(' ');
    const occurrences = {};
    let result = [];

    for (const currentElement of elements) {
        let element = currentElement.toLowerCase();

        if (occurrences.hasOwnProperty(element)) {
            occurrences[element] += 1;
        } else {
            occurrences[element] = 1;
        }
    }

    Object.entries(occurrences)
        .filter(element => element[1] % 2 != 0)
        .sort((a, b) => b[1] - a[1])
        .forEach(element => result.push(element[0]));

    console.log(result.join(' '));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');
function solve(inputArr) {
    const piecesCount = Number(inputArr.shift());
    const pieces = {}

    for (let i = 0; i < piecesCount; i++) {
        const [piece, composer, key] = inputArr.shift().split('|');
        pieces[piece] = {composer, key};
    }

    let commandLine = inputArr.shift();
    while(commandLine !== 'Stop') {
        const [command, piece, ...args] = commandLine.split('|');

        switch (command) {
            case 'Add':
                const [composer, key] = args;

                if (pieces.hasOwnProperty(piece)) {
                    console.log(`${piece} is already in the collection!`);
                    break;
                }

                pieces[piece] = {composer, key};
                console.log(`${piece} by ${composer} in ${key} added to the collection!`);
                break;
            case 'Remove':
                if (!pieces.hasOwnProperty(piece)) {
                    console.log(`Invalid operation! ${piece} does not exist in the collection.`);
                    break;
                }

                delete pieces[piece];
                console.log(`Successfully removed ${piece}!`);
                break;
            case 'ChangeKey':
                const newKey = args[0];

                if (!pieces.hasOwnProperty(piece)) {
                    console.log(`Invalid operation! ${piece} does not exist in the collection.`);
                    break;
                }

                pieces[piece].key = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`);
                break;
        }

        commandLine = inputArr.shift();
    }

    for (const piece in pieces) {
        console.log(`${piece} -> Composer: ${pieces[piece].composer}, Key: ${pieces[piece].key}`);
    }
}

solve([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'
]);
solve([
    '4',
    'Eine kleine Nachtmusik|Mozart|G Major',
    'La Campanella|Liszt|G# Minor',
    'The Marriage of Figaro|Mozart|G Major',
    'Hungarian Dance No.5|Brahms|G Minor',
    'Add|Spring|Vivaldi|E Major',
    'Remove|The Marriage of Figaro',
    'Remove|Turkish March',
    'ChangeKey|Spring|C Major',
    'Add|Nocturne|Chopin|C# Minor',
    'Stop'
]);
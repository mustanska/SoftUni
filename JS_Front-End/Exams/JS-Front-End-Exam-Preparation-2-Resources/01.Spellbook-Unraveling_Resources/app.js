function solve(inputArr) {
    let mysteriousSpellWord = inputArr.shift();

    let commandLine = inputArr.shift();


    while(commandLine !== 'End') {
        const [command, ...args] = commandLine.split('!');
        let hasErrorMessage = false;

        switch (command) {
            case 'RemoveEven':
                mysteriousSpellWord = Array.from(mysteriousSpellWord)
                    .filter((element, index) => index % 2 === 0)
                    .join('');
                break;
            case 'TakePart':
                const startIndex = Number(args[0]);
                const endIndex = Number(args[1]);

                mysteriousSpellWord = mysteriousSpellWord.substring(startIndex, endIndex);
                break;
            case 'Reverse':
                const substring = args[0];
                const reversedSubstring = Array.from(substring).reverse().join('');

                if(mysteriousSpellWord.includes(substring)) {
                    mysteriousSpellWord = mysteriousSpellWord.split(substring).join('');
                    mysteriousSpellWord += reversedSubstring;
                } else {
                    console.log('Error');
                    hasErrorMessage = true;
                }
                break;
        }
    
    if(!hasErrorMessage) {
        console.log(mysteriousSpellWord);
    }
    
    commandLine = inputArr.shift();
    }

    console.log(`The concealed spell is: ${mysteriousSpellWord}`); 
}

solve([
    "asAsl2adkda2mdaczsa",
    "RemoveEven",
    "TakePart!1!9",
    "Reverse!maz",
    "End"
]);
solve([
    "hZwemtroiui5tfone1haGnanbvcaploL2u2a2n2i2m",
    "TakePart!31!42",
    "RemoveEven",
    "Reverse!anim",
    "Reverse!sad",
    "End"
]);
function printDNA(helixLength){
    let sequence = getSequenceWithCurrentLength(helixLength * 2);
    let pairsOfLettersArray = getArrayWithPairsOfLetters(sequence);
    let currentRow = 0;
    let seriesOfRows = 4;

    while(currentRow < helixLength){
        currentRow += 1;
        seriesOfRows += 1;

        if(seriesOfRows > 4){
            seriesOfRows = 1;
        }

        if(seriesOfRows % 2 === 0){
            console.log(`*${pairsOfLettersArray[currentRow-1][0]}--${pairsOfLettersArray[currentRow-1][1]}*`);
        } else if(seriesOfRows % 3 === 0){
            console.log(`${pairsOfLettersArray[currentRow-1][0]}----${pairsOfLettersArray[currentRow-1][1]}`);            
        }else{
            console.log(`**${pairsOfLettersArray[currentRow-1][0]}${pairsOfLettersArray[currentRow-1][1]}**`);
            
        }
    }

    function getSequenceWithCurrentLength(currentLength){
        let sequence ='ATCGTTAGGG';
        let newSequence = '';

        while (newSequence.length < currentLength){
            for(let i = 0; i < sequence.length; i++){
                if(newSequence.length === currentLength){
                    break;
                }

                newSequence += sequence[i];
            }
        }

        return newSequence;
    }

    function getArrayWithPairsOfLetters(sequence){
        return sequence.match(/.{1,2}/g);
    }
}

printDNA(4);
printDNA(10);
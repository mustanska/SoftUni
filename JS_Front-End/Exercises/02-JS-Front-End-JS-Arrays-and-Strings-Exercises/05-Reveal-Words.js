// function revealWords(stringOfWords, text){
//     let wordsArray = stringOfWords.split(', ');
//     let textArray = text.split(' ');

//     wordsArray.forEach(word => {
//         let searchedWord = '*'.repeat(word.length);
        
//         textArray.forEach((element, index) =>{
//             if(searchedWord === element) {
//                 textArray[index] = word; 
//             }
//         })

//     });

//     console.log(textArray.join(' '));
// }

function revealWords(stringOfWords, text){
    let wordsArray = stringOfWords.split(', ');
    let newText = text;

    wordsArray.forEach(word => {
        let searchedWord = '*'.repeat(word.length);
        
        newText = newText.replace(searchedWord, word);

    });

    console.log(newText);
}

revealWords('great','softuni is ***** place for learning new programming languages');
revealWords('great, learning', 'softuni is ***** place for ******** new programming languages');
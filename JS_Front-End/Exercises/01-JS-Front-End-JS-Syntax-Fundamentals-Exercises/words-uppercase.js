function wordsUppercase(string){
    const wordsAsArray = string.match(/\b\w+\b/g);
    let wordsAsString = '';

    for(let i = 0; i < wordsAsArray.length; i++){
        wordsAsString += wordsAsArray[i].toUpperCase();

        if(i<wordsAsArray.length - 1){
            wordsAsString += ', ';
        }
    }

    console.log(wordsAsString);
}   

wordsUppercase('Hi, how are you?');
wordsUppercase('hello');
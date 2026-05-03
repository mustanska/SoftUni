function stringSubstring(word, text){
    let pattern = RegExp(`\\b${word}\\b`, 'g');

    if(pattern.test(text.toLowerCase())){
        return console.log(word);
    }

    console.log(`${word} not found!`);
    
}

stringSubstring('javascript', 'JavaScript is the best programming language');
stringSubstring('python', 'JavaScript is the best programming language');
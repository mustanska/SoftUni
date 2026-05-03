function reversedChars(character1, character2, character3){
    let string = character1 + character2 + character3;
    let reversedString = '';

    for(let i = 2; i >= 0; i--){
        reversedString += string[i] + ' ';
    }

    console.log(reversedString.trim());
    
}

reversedChars('A', 'B', 'C');
reversedChars('1', 'L', '&');
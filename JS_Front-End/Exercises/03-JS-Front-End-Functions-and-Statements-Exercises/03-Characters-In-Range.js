function charactersInRange(firstChar, secondChar){
    let firstCharCode = firstChar.charCodeAt(0);
    let secondCharCode = secondChar.charCodeAt(0);

    [firstCharCode, secondCharCode] = characterBoundary(firstCharCode, secondCharCode);
    const characters = [];

    for(let i = firstCharCode + 1; i < secondCharCode; i++){
        characters.push(String.fromCharCode(i));
    }

    console.log(characters.join(' '));
    
        
    
    function characterBoundary(...characters){
        characters.sort((a, b) => a - b);
        
        return characters;
    }
}

charactersInRange('a', 'd');
charactersInRange('#', ':');
charactersInRange('C', '#');
function pascalCaseSplitter(string){
    const pattern = /[A-Z][a-z]*/g;

    const matches = Array.from(string.matchAll(pattern)).map(match => match[0]);
    console.log(matches.join(', '));
    
}

pascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCaseSplitter('HoldTheDoor');
pascalCaseSplitter('ThisIsSoAnnoyingToDo');
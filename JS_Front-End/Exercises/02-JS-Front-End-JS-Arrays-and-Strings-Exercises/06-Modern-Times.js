function modernTimes(string){
    const pattern = /#(?<specialWord>[a-zA-Z]+)/g;

    const matches = string.matchAll(pattern);

    for (const match of matches) {
        console.log(match.groups.specialWord);
        // console.log(match[1]); 
    }
}

modernTimes('Nowadays everyone uses # to tag a #special word in #socialMedia');
modernTimes('The symbol # is known #variously in English-speaking #regions as the #number sign');
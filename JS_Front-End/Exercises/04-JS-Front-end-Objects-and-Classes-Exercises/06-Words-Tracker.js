function solve(words) {
    let searchedWords = words.shift().split(' ');
    const occurrences = {}

    for (const word of searchedWords) {
        occurrences[word] = 0;
    }

    for (const word of words) {
        if(occurrences.hasOwnProperty(word)) {
            occurrences[word] += 1;
        }
    }

    const entries = Object.entries(occurrences);
    entries
        .sort((a, b) => b[1] - a[1])
        .forEach(word => console.log(`${word[0]} - ${word[1]}`))
}

solve([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
]);
solve([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'
]);
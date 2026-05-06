function solve() {
  let wordsInput = document.getElementById('text');
  let typeInput = document.getElementById('naming-convention');

  let words = wordsInput.value.toLowerCase().split(' ');
  let type = typeInput.value;

  let result = '';

  if(type === 'Camel Case') {
    result = toCamelCase(words);
  } else if(type === 'Pascal Case') {
    result = toPascalCase(words);
  } else {
    result = 'Error!';
  }

  let resultField = document.getElementById('result');
  resultField.textContent = result;

  function toCamelCase(words) {
    let convertedWords = words.map((word, index) => index === 0 ? word : capitalize(word));

    return convertedWords.join('');
  }

  function toPascalCase(words) {
    let convertedWords = words.map(word => capitalize(word));

    return convertedWords.join('');
  }

  function capitalize(word) {
    return `${word[0].toUpperCase()}${word.substring(1)}`;
  }
}
function solve() {
  const sentences = document.getElementById('input').value.split('.');

  let singleParagraph = '';
  let sentencesCountInParagraph = 0;

  for (i = 0; i < sentences.length; i++) {
    if (sentencesCountInParagraph === 3 || i === sentences.length - 1) {
      let paragraph = document.createElement('p');
      paragraph.textContent = singleParagraph.trim();
      document.getElementById('output').appendChild(paragraph);
      

      singleParagraph = '';
      sentencesCountInParagraph = 0;
    }

    singleParagraph += sentences[i] + '. ';
    sentencesCountInParagraph++;
  }
}
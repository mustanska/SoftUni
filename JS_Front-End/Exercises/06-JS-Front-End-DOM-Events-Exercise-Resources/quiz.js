document.addEventListener('DOMContentLoaded', solve);

function solve() {
  const questionsWithAnswers = {
    'Question #1:': 'onclick',
    'Question #2:': 'JSON.stringify()',
    'Question #3:': 'A programming API for HTML and XML documents'
  }

  let correctAnswers = 0;

  const questionElements = document.querySelectorAll('.question');
  const answers = document.querySelectorAll('.quiz-answer');

  answers.forEach(answer => answer.addEventListener('click', getResultOfQuestionHandler));

  function getResultOfQuestionHandler(e) {
    const selectedAnswer = e.currentTarget;
    const currentQuestion = selectedAnswer.closest('.question');
    const questionNumber = currentQuestion.querySelector('h2 span').textContent;

    if (questionsWithAnswers[questionNumber] === selectedAnswer.textContent) {
      correctAnswers++;
    }

    currentQuestion.classList.add('hidden');
    const nextQuestion = currentQuestion.nextElementSibling;
    const resultElement = document.getElementById('results');

    if (nextQuestion.classList.contains('question')) {
      nextQuestion.classList.remove('hidden');
    } else {
      if (correctAnswers === questionElements.length) {
        resultElement.textContent = 'You are recognized as top JavaScript fan!';
      } else if(correctAnswers === 1) {
        resultElement.textContent = 'You have 1 right answer';
      } else {
        resultElement.textContent = `You have ${correctAnswers} right answers`;
      }
    }
  }
}
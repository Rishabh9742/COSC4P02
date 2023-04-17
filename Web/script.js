let lineNum = 0;
let data;

async function showData(line_num) {
  const response = await fetch('https://raw.githubusercontent.com/Rishabh9742/COSC4P02/main/Web/test.json');
  const jsonData = await response.json();
  data = jsonData;

  try {
    const { title, description, image_url } = data[line_num];

    document.getElementById('label_title').textContent = title;
    document.getElementById('label_description').textContent = description;

    const image = await loadImage(image_url);
    document.getElementById('label_image').src = image.src;

    const line_text = `Line ${line_num + 1} of ${data.length}`;
    document.getElementById('label_line').textContent = line_text;
  } catch (error) {
    console.error(error);
  }

  // Refreshes the questions based on the JSON file
  const question = data[line_num].question; 
  const choices = data[line_num].choices; 

// //Refreshes the question and choices in the HTML
// document.querySelector('#quizForm label').textContent = question;
// if (choices) {
//   choices.forEach((choice, index) => {
//     const input = document.querySelector(`#quizForm input[name="q${i}"]:nth-child(${index * 2 + 2})`);
//     const label = input.nextElementSibling;
//     input.value = choice.slice(0, 1); 
//     label.textContent = ` ${choice}`;
//   });
// }


  // Reset the question and answer
  document.getElementById('quizForm').reset();
  document.getElementById('quizResult').textContent = '';

}

function loadImage(url) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => reject(new Error(`Failed to load image from ${url}`));
    image.src = url;
  });
}

function nextLine() {
  lineNum = (lineNum + 1) % data.length; // Cycle back when reaching the last image
  document.getElementById('quizForm').reset();
  showData(lineNum);
}

function previousLine() {
  lineNum = (lineNum - 1 + data.length) % data.length; // Cycle forward when reaching the first image
  document.getElementById('quizForm').reset();
  showData(lineNum);
}

function jumpToLine() {
  const input = document.getElementById('jumpToLine');
  const newLineNum = parseInt(input.value) - 1;
  if (!isNaN(newLineNum)) {
    lineNum = newLineNum;
    showData(lineNum);
    input.value = '';
  }
}

function lightMode() {
  const modeButton = document.querySelector('#mode');
  const body = document.querySelector('body');

  modeButton.addEventListener('click', function() {

    body.classList.toggle('light-mode');//Toggles the light/dark mode

    if (body.classList.contains('light-mode')){//changes button text
      modeButton.textContent = 'Dark Mode';
    } else {
      modeButton.textContent = 'Light Mode';
    }
  });
  
}

const getAnswer = (i) => {
  const radioInput = document.querySelector('input[type="radio"]');
  const value = radioInput.getAttribute('value').trim();
  return value.trim();
};



function handleQuizSubmission() {
  // Get the correct answer and the form
  const form = document.getElementById('quizForm');
  const quizResult = document.getElementById('quizResult');
  const correctAnswer = data[lineNum].correct_answer;

  // Get the selected answer
  let selectedAnswer = Array.from(form.elements).find((element) => element.checked);
  selectedAnswer = selectedAnswer.value


  // Verify that an answer was selected
  if (!selectedAnswer) {
    quizResult.textContent = 'Please select an answer.';
    return;
  }

  // Inform if the answer is correct or incorrect
  if (selectedAnswer === correctAnswer) {
    quizResult.textContent = 'Correct!';
  } else {
    quizResult.textContent = 'Incorrect. Try again.';
  }
  // console.log(getAnswer(selectedAnswer), correctAnswer)
}

document.getElementById('previous').addEventListener('click', previousLine);
document.getElementById('goToLine').addEventListener('click', jumpToLine);
document.getElementById('next').addEventListener('click', nextLine);
document.getElementById('submitAnswer').addEventListener('click', handleQuizSubmission);

showData(lineNum);

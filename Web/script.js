let lineNum = 0;
let data;

async function showData(line_num) {
  const response = await fetch('https://raw.githubusercontent.com/Rishabh9742/COSC4P02/1462781a76cba0714f67640547ab6947599f5402/Web/test.json');
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
  if (lineNum < data.length - 1) {
    lineNum++;
    showData(lineNum);
  }
}

function previousLine() {
  if (lineNum > 0) {
    lineNum--;
    showData(lineNum);
  }
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

document.getElementById('previous').addEventListener('click', previousLine);
document.getElementById('goToLine').addEventListener('click', jumpToLine);
document.getElementById('next').addEventListener('click', nextLine);

showData(lineNum);

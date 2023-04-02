let lineNum = 0;
let data;

async function showData(line_num) {
  const response = await fetch('https://raw.githubusercontent.com/Rishabh9742/COSC4P02/main/test.json');
  const jsonData = await response.json();
  data = jsonData.slice(0, -1);

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

document.getElementById('previous').addEventListener('click', previousLine);
document.getElementById('goToLine').addEventListener('click', jumpToLine);
document.getElementById('next').addEventListener('click', nextLine);

showData(lineNum);
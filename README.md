4P02 Museum Project
====================

# Live Product and Sprint Backlogs
[Backlogs Sheet](https://docs.google.com/spreadsheets/d/1FwdKNZmc1wWEivzn2ezl59bVdrNpcElhstLYFrKzrvw/edit?usp=sharing)

# View the live HTML page for index.html
[Webpage](https://htmlpreview.github.io/?https://github.com/Rishabh9742/COSC4P02/blob/main/Web/index.html)

# Group Members

<ul>
  <li>Goktug Cirag (gc19cy@brocku.ca) ID: 6776678</li>
  <li>Alex Duclos (ad19ua@brocku.ca) ID: 6738884</li>
  <li>Eduardo Saldana (es18za@brocku.ca) ID: 6612626</li>
  <li>Rishabh Rai (rr19pa@brocku.ca) ID: 6847156</li>
  <li>Jashan Pannu (jp18jj@brocku.ca) ID: 6505861</li>
</ul>

# Roles
<ul>
  <li>Scrum Master: Rishabh Rai</li>
  <li>Product Owner: Alex Duclos</li>
  <li>Product Manager: Eduardo Saldana</li>
  <li>Development Team: Gokutg Cirag, Jashan Pannu, Rishabh Rai, Alex Duclos, Eduardo Saldana</li>
</ul>

# Description
This project is for the development of a virtual museum for the COSC 4P02 class at Brock University. The goal of the project is to create an interactive, immersive and educational digital timeline for users to learn about various historical events. The museum will feature a variety of virtual exhibits and interactive elements to engage visitors. The planned project will involve a traversable interactive timeline for visitors to be able to have a more immersive experience.

# Features
<ul>
  <li> Traversable interactive timeline of history shared in museum </li>
  <li> Virtual tours of virtual exhibits </li>
  <li> Detailed historical information events and historical figures </li>
  <li> Interactive elements such as quizzes and games </li>
  <li> Search functionality to easily find information on events and artifacts </li>
</ul>

# Technologies Used
<ul>
  <li> Python </li>
  <li> Tkinter </li>
</ul>

# Software Engineering Method
Scrum method, the reason we believe this is the superior method for our project is that it will all build from the previous submissions. It all simply continues to continiously grow and expand.

## Documentation

# Json
- `"title"`: a string representing the title of the item.
- `"description"`: a string describing the item in detail.
- `"image_url"`: a string containing the URL of an image of the item.
- `"question"`: a string representing a sample question related to the item.
- `"choices"`: an array of strings representing the different answer choices for the sample question.
- `"correct_answer"`: a string representing the correct answer for the sample question.

# Example
```  
  {
        "title": "Quilt",
        "description": "The Log Cabin quilt is another patchwork style quilt that has a distinctive design and is very versatile with many variations. Strips of fabric, or 'logs,' are stitched around a square 'hearth' to form a block, or 'cabin.' Depending on how logs are pieced, and blocks arranged, a Log Cabin can take varied forms, such as Barn Raising, Straight Furrow, Sunshine and Shadow, and Pineapple. In the nineteenth century, the Log Cabin quilt pattern was described as 'Canadian patchwork,' evoking the colonial homestead. In traditional Log Cabin blocks, one half is made of dark fabrics and the other half light.",
        "image_url": "https://s3.amazonaws.com/pastperfectonline/images/museum_74/086/thumbs/9776.jpg",
        "question": "Sample question",
        "choices": ["a) Choice 1", "b) Choice 2", "c) Choice 3", "d) Choice 4"],
        "correct_answer": "a) Choice 1"
  }
  {
        "title": "Quilt",
        "description": "The Log Cabin quilt is another patchwork style quilt that has a distinctive design and is very versatile with many variations. Strips of fabric, or 'logs,' are stitched around a square 'hearth' to form a block, or 'cabin.' Depending on how logs are pieced, and blocks arranged, a Log Cabin can take varied forms, such as Barn Raising, Straight Furrow, Sunshine and Shadow, and Pineapple. In the nineteenth century, the Log Cabin quilt pattern was described as 'Canadian patchwork,' evoking the colonial homestead. In traditional Log Cabin blocks, one half is made of dark fabrics and the other half light.",
        "image_url": "https://s3.amazonaws.com/pastperfectonline/images/museum_74/086/thumbs/9776.jpg",
        "question": "Sample question",
        "choices": ["a) Choice 1", "b) Choice 2", "c) Choice 3", "d) Choice 4"],
        "correct_answer": "a"
    }
    
 
```

# JSON Edit

### Importing Modules
- `tkinter` and `tkinter.ttk` for GUI elements and widgets
- `tkinter.messagebox` for showing message boxes
- `csv` for reading and writing CSV files
- `PIL.Image` and `PIL.ImageTk` for working with images
- `urllib.request` for opening URLs
- `tkinter.filedialog` for selecting files from the file system
- `json` for reading and writing JSON files

### Functions
We use the following functions.

#### `select_json_file()`
This function opens a file dialog for the user to select a JSON file. The selected file path is then displayed in a label widget.

#### `append_to_json()`
This function appends a new row of data to the selected JSON file. The data is taken from the text fields for `title`, `description`, and `image_url`. If the selected JSON file is empty, the function creates a new list to hold the data. If an error occurs during the operation, a message box is displayed with the error message.

#### `delete_from_json()`
This function deletes a row from the selected JSON file. The row to be deleted is specified by the user input in the `rowDel` entry field. If an error occurs during the operation, a message box is displayed with the error message.

#### `clear_text()`
This function clears the text fields for `title`, `description`, and `image_url`.

### GUI Elements
The code defines the following GUI elements:
- A main window with the title "CSV Data Appender"
- A label widget for displaying the text "Select a JSON file:"
- A label widget for displaying the path to the selected JSON file
- A button widget for browsing for a JSON file
- A label widget for displaying the text "Title:"
- An entry widget for inputting the `title` data
- A label widget for displaying the text "Description:"
- An entry widget for inputting the `description` data
- A label widget for displaying the text "Image URL:"
- An entry widget for inputting the `image_url` data
- A button widget for clearing the text fields
- A button widget for appending data to the selected JSON file
- A button widget for deleting a row from the selected JSON file
- An entry widget for specifying the row to delete

### Execution
The GUI is launched and runs until the user closes the window.```

# Contact
If you have any questions or issues, please contact any of the group members or send an email to any or all group members. 

# License
This project is licensed under the MIT License



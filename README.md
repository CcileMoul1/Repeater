# Repeater
Learn your lessons by being asked about it.
Every lesson you can write as a table could be studied with `repeater`. It will randomly select an element of the table and ask you to complete the row. `repeater`could be use to learn vocabulary, historical dates etc.

Based on the use of flashcards to learn, this program improves this method by 
- checking your answers automatically (useful to be precise)
- being able to create multi-sided flashcards
- having a user-friendly input file

Other programs having these features (and more) may exist, but this program is also a way for me to practice and learn how to code.

# Usage
## How to launch the program
For now, everything is directly written in the code. This will be changed at some point.

1. Write the lesson you want to study in a csv file.
2. Change the path to the file in the code (`csv_file = ...`)
3. Run the code with python (open a terminal, go to the repertory of the code and run `python main.py`)

## Dependencies
The following libraries are used
- random
- pandas
- difflib

# Features
## Currently

Reads a csv file, randomly selects a row and a column and asks the user to complete every other elements of the row. For every given answer, tells if it is correct or wrong. Repeats this 20 times before asking to stop or continue.
At the start, it is possible to ask the program to highlight the differences when the answer is wrong.
For each session (for now, 20 questions), the questions are unique. 

## Future
This list is not ordered.
- ~~Highlighting the differences between the given answer and the solution~~
- ~~No repeated questions in one session~~
- Known-score and selection of rows based on this score (no saving)
- (with saving)
- Time without asking reduce the score
- option to be more flexible about wrong answers
- inputs not written in the code
- GUI
- optional overview at the end

# Comment
Any advice on how to improve this readme or the programm (code or features) is welcomed

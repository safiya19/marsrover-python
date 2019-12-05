# marsrover-python
This navigation problem is based on the Mars Rover challenge.
The objective of the project is to design a program which takes an 
input textfile containing the instructions required for the rover
to navigate a grid. Upon completion of navigation, the console
must display the new coordinates and direction of the the rover. 

Technical Specifications:
- The program is written in Python version 3.7.1
- The MarsRover folder must contain 4 items
	* The input file (input.txt)
	* The main python file (main.py)
	* The instruction file (README.txt)
	* The marsrover folder containing 3 class files

To run the program: 
1. Ensure that the text file containing the rover instructions is
   named "input", and place it in the same directory as main.py
2. Open the command prompt within the folder in which main.py is contained.
3. From the command prompt, run "main.py" 
The output will be displayed on the console

Unit Testing:

Zone size, start coordinate position, start cardinal direction,
and rover movement goes through unit testing in test.py

Design decision:
- Each line of the the input text file was placed into a list in order
to separate the commands. Item 1 of list refers to the zone size,
Item 2 the starting point of the rover, and Item 3 the movement.The 
items were then converted into logical parameters in order for 
the rover processes to be executed.
- Each cardinal point was assigned its own numerical value for the
rover to interpret. The heading of the rover was determined by
positionig the x y coordinates, where N and S changes the y position,
while E and W changes the x position. If the x and y integers add 
up to values beyond the zone, the rover is flagged as going off
the grid, however the end point of the rover will still be provided. 
- Warning messages print out if:
  1) Rover has moved out of grid bounds
  2) An invalid character has been placed in the input file

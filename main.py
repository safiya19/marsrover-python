#CLASS IMPORTS
from marsrover import Zone
from marsrover import Position
from marsrover import Rover


def main():
#OPEN AND STORE LINES WITHIN INPUT FILE INTO A LIST
    input_lines = []
    input_file = "input.txt"
    file = open(input_file, "r")
    with open(input_file, 'rt') as file:
        for line in file:
            input_lines.append(line)

#CONVERT EACH INDEX VALUE OF LIST TO A STRING
    grid_size = input_lines[0]
    grid_size = str(grid_size) 
    start_point = input_lines[1]
    start_point = str(start_point) 
    movement = input_lines[2]
    movement = str(movement)  #converted to string

#CONVERT GRID VALUES TO INTEGERS
    integers1 = [int(i) for i in grid_size.split(' ')]
    grid_x = integers1[0]
    grid_y = integers1[1]
	
#CONVERT ROVER START COORDINATES TO INTEGERS
    start_x = " ".join(start_point.split(" ", 2)[0])
    start_x = int(start_x)
    start_y = " ".join(start_point.split(" ", 2)[1])
    start_y = int(start_y)
    start_dir = " ".join(start_point.split(" ", 2)[2])
	
#CONVERT START DIRECTION INTO AN INPUT CHARACTER FOR MARSROVER
    start_dir = list(start_dir)
    dir_char = start_dir[0]
	
#CREATE MARSROVER INSTANCE FOR PROCESSING	
    zone = Zone(grid_x, grid_y)
    position = Position(start_x, start_y)
    rover = Rover(zone, position, Rover.DIRECTIONS.get(dir_char)) 
    rover.process(movement)
    print(rover) 


if __name__ == "__main__":
    main()

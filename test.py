import unittest
from marsrover import *

#Read from input file
input_lines = []
input_file = "input.txt"
file = open(input_file, "r")
with open(input_file, 'rt') as file:
    for line in file:
        input_lines.append(line)
		
#zone size
grid_size = input_lines[0]
grid_size = str(grid_size)	
integers1 = [int(i) for i in grid_size.split(' ')]
grid_x = integers1[0]
grid_y = integers1[1]

#coordinate position
start_point = input_lines[1]
start_point = str(start_point) 	
start_x = " ".join(start_point.split(" ", 2)[0])
start_x = int(start_x)
start_y = " ".join(start_point.split(" ", 2)[1])
start_y = int(start_y)
		
#direction of movement
movement = input_lines[2]
start_dir = " ".join(start_point.split(" ", 2)[2])
start_dir = list(start_dir)
dir_char = start_dir[0]


class TestZone(unittest.TestCase):
    def testing(self):				
        zone = Zone(grid_x, grid_y)
        self.assertEqual(zone.width, 8)
        self.assertEqual(zone.height, 10)	


class TestPosition(unittest.TestCase):
    def testing(self):               
        direction = Rover.DIRECTIONS.get(dir_char)
        position = Position(start_x, start_y)
        zone = Zone(grid_x, grid_y)		
        
        rover = Rover(zone, position, direction)
        self.assertEqual(Position(1, 2), rover.position)


class TestDirection(unittest.TestCase):
    def testing(self):          
        direction = Rover.DIRECTIONS.get(dir_char)   
        self.assertEqual(direction, 2) #'N' : 1 , 'E': 2 , 'S': 3 , 'W': 4,


class TestMovement(unittest.TestCase):
    def testing(self):
            movement1 = str(movement)
            self.assertEqual(movement1, 'MMLMRMMRRMML')


if __name__ == '__main__':
    unittest.main()

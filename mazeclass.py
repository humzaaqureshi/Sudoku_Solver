"""  
Program name: EECS210_Assignment 6
Brief Description: The main point of this project is to solve a Sudoku puzzle with Depth-First search Algorithm
Inputs: There are no inputs 
Output: 5 different outputs
All collaborators: Youtube(inside coder)
Author's full name: Humza Ahmed Qureshi
Creation date: 11-08-2023

"""
class MAZE: # Initialze a class named MAZE to call object later
    def __init__(self, filename):# initlizie attributes of class; only filename will be used
        self.filename = filename # so filename can be used later down in other methods of the class
        maze_file = open(self.filename, "r")# Basic file I/O 
        self.maze = []#saving the maze to a list
        for line in maze_file:# iterate through the maze file
            line = line.split()# split the line to create a 2d list
            self.maze.append(line)# append the lines to the maze, creating a 2d list

    def print_maze(self):# printing the maze for formatting purposes
        for i in range(len(self.maze)):# formatting
            for j in range(len(self.maze)):# formatting
                print(self.maze[i][j], end= " ")# formatting
            print()# formatting
    def puzzle_filename(self):
        return self.filename

    def clean_puzzle(self):# a method that was created to convert the string of the list into numerical values to work with
        for i in range(len(self.maze)):# iterating through the len of the rows
            for j in range(len(self.maze[0])):# iterating through the len of the col
                if self.maze[i][j] == "_":# if somewhere in the puzzle there is a "_", then ...
                    self.maze[i][j] = 0#... make sure that you changed that to a 0
                if self.maze[i][j] == str(self.maze[i][j]):# this is basic type conversion...
                    self.maze[i][j] = int(self.maze[i][j])# if the element in the list is a string, convert it to a integer
    
    def is_valid(self, guess, row, col):# checking to see which of the values of the list are candatites to be changed or converted
        # this is a helper function
        row_values = self.maze[row]# saving all of the values of the rows into row values
        if guess in row_values:#if the guess ends up being in the row_values...
            return False# then it will be false; this is part of the sudoku game
        
        for i in range(len(self.maze)):# part of the sudoku rules
            if self.maze[i][col] == guess:
                return False
        
        cube_row = (row // 3)*3
        cube_col = (col // 3)*3

        for i in range(cube_row, cube_row + 3):
            for j in range(cube_col, cube_col + 3):
                if self.maze[i][j] == guess:
                    return False
        return True
    
    def solve(self, r = 0, c = 0):
        if r == 9:# this is the base case for the solver; if the solver gets to the last element of the list 
            # then it means that the rest of the algorithm has past all of the columns and is in the final row
            return True# will return true as it is done with the algo
        elif c == 9:# if the solver is at col 9, then it must go to the next row
            return self.solve(r+1,0)
        elif self.maze[r][c] != 0:
            return self.solve(r, c+1)
        else:
            for num in range(1,10):
                if self.is_valid(num, r, c):
                    self.maze[r][c] = num

                    if self.solve(r, c+1):
                        return True
                self.maze[r][c] = 0
            
            return False
    def __str__(self):
        output = f'{self.filename}'
        return output

    def run(self):
        print("-" *20)
        print(f'{self.filename} Unsolved')
        print("                         ")
        self.print_maze()
        self.clean_puzzle()
        self.solve()
        print("-" *20)
        print(f'{self.filename} Solved')
        print("                       ")
        self.print_maze()
        print("-" *20)







    

        



        
        

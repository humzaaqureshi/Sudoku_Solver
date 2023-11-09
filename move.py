"""  
Program name: EECS210_Assignment 6
Brief Description: The main point of this project is to solve a Sudoku puzzle with Depth-First search Algorithm
Inputs: There are no inputs 
Output: 5 different outputs
All collaborators: Youtube(inside coder)
Author's full name: Humza Ahmed Qureshi
Creation date: 11-08-2023

"""
from mazeclass import MAZE# from the mazeclass, we will import the maze module

objectlist = []# create a list to store the objects
puzzlelist = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt", "puzzle4.txt", "puzzle5.txt"]
#(Above Code) list all of the puzzles text files into the list to iterate through later on
# ease of formatting issue
for line in puzzlelist:# for every single line in the puzzle list (for every text file in the list)
    objectlist.append(MAZE(line))# make an object of that text file (pass it through the MAZE object)
    #(Above Code) This will create a maze object and store all of the objects into a list

for ob in objectlist:# for all of the objects in the list
    ob.run()# you will call the .run() method from the mazeclass and it will run everything that is needed; solver, clean puzzle, etc. 
    if ob.solve() == False:
        print(f'{ob.filename} is Unsolvable')
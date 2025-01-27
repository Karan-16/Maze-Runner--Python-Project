# Maze Solver Project

This project involves solving a maze using Python, with functionalities to generate a random maze and find a valid zigzag path from the source to the destination. The project is divided into four assignments that progressively build the maze-solving logic and handle different aspects of the problem.

## Project Structure

- **Assignment 1**: Generate a random maze and extract the coordinates of the source and destination cells.
- **Assignment 2**: Compute a conditional valid zigzag path between the source and the destination cells.
- **Assignment 3**: Implement a path computation function that adheres to a set of constraints (zigzag motion, moving forward only, etc.).
- **Assignment 4**: Print the computed path or display an error message if no valid path exists.

## Dependencies

- `mazeSmart.py`: A maze generator module that provides functions to create random mazes, extract source and destination coordinates, and display the maze.

## Features

- **Maze Generation**: The program creates a maze of size `n x n` where `n >= 3`.
- **Path Calculation**: The program computes a valid zigzag path from the source to the destination, if it exists.
- **Input Validation**: The program validates the maze size (`n > 2`) before proceeding with the maze creation.
- **Path Constraints**: The path follows a set of rules such as moving row-wise, zigzag movement, and only through accessible cells.

## How to Use

1. **Install Dependencies**:
   Ensure that the `mazeSmart.py` file is placed in the same directory as your `main.py` file.

2. **Running the Program**:
   - The program will first prompt for the maze size `n`. If the size is less than or equal to 2, it will prompt again until a valid value is entered.
   - The program will then generate the maze and extract the source and destination coordinates.
   - The path computation will then be attempted based on the zigzag rules, and the result will be printed.

## Example

### Sample Output:

Please enter another value that is greater than 2: 5 Generated Maze: G G R G G R G R R G G G G G R R G R G G G R G G G

Source: (0, 0) Destination: (4, 4) Valid Zigzag Path: (0,0)->(1,1)->(2,2)->(3,3)->(4,4)


## How It Works

1. The program starts by prompting for the maze size and generates a random maze using the `mazeSmart.py` module.
2. The coordinates of the source and destination cells are extracted.
3. A zigzag path is computed based on specific movement rules: 
   - Move only to the next row.
   - Move forward in columns, alternating between staying in the same column or moving to the next column.

## Files

- **main.py**: The main Python script that drives the program.
- **mazeSmart.py**: The maze generator module used to create the maze and extract coordinates.

# SebDaBaBo's Game of Life

## Overview
SebDaBaBo's Game of Life is an implementation of Conway's Game of Life using Python and the Pygame library. This application provides an interactive grid where users can create and evolve patterns based on simple rules.

## Features
- **Interactive Grid**: Draw and erase cells with mouse clicks.
- **Simulation Control**: Start and stop the simulation.
- **Reset Functionality**: Clear the grid to start anew.
- **Real-Time Updates**: See the grid evolve in real-time based on Conway's rules.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sebdababo/Game-of-Life.git
    cd Game-of-Life
    ```

2. **Install Pygame**:
    ```bash
    pip install pygame
    ```

3. **Run the Application**:
    ```bash
    python main.py
    ```

## Usage
1. **Starting the Application**:
   - Run `python main.py` to start the Game of Life.

2. **Drawing and Erasing Cells**:
   - **Left Click**: Draw cells on the grid.
   - **Right Click**: Erase cells from the grid.
   - Drag the mouse while holding down the left or right button to draw or erase multiple cells.

3. **Simulation Controls**:
   - **Start/Stop Button**: Toggle the simulation on and off.
   - **Reset Button**: Clear the grid and stop the simulation.

## Simulation Rules
1. **Any live cell with two or three live neighbors survives.**
2. **Any dead cell with three live neighbors becomes a live cell.**
3. **All other live cells die in the next generation. Similarly, all other dead cells stay dead.**

## Example Start
![Game of Life ouput 1](https://github.com/user-attachments/assets/efa01c47-d0ce-47ce-b5a9-a1a7df9c2856)

## Example Simulation End
![Game of Life output 2](https://github.com/user-attachments/assets/2b060789-ab17-4c69-8a6c-5ef435a538f0)

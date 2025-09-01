# 3D Soccer Formation Viewer

A lightweight Python application that visualizes football (soccer) formations on a realistic 3D soccer field. This tool allows users to input the number of players and their formation, and then generates an interactive 3D visualization of the formation on a proper soccer pitch.

## Features

- Realistic soccer field with standard dimensions (105 × 68 meters).  
- Full pitch markings: outer boundaries, halfway line, center circle, penalty areas, and goal boxes.  
- Interactive 3D view with rotation, zoom, and pan capabilities.  
- Automatic generation of player positions based on user-provided formations (e.g., 4-3-3).  
- Player numbers annotated on the field for easy reference.  
- Lightweight and suitable for running on low-spec laptops.  
- Fully coded in Python using Matplotlib.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Install required dependencies:
   ```
   pip install matplotlib
   ```

 ## Usage 

 1. Run the script:
    ```
    python main.py
    ```
    A 3D soccer field appears with 11 players arranged in the specified formation, including goalkeepers, defenders, midfielders, and forwards. You can rotate, zoom, and pan the field to view the formation from different angles.


## Potential Enhancements

Color-coded tactical zones (defense, midfield, attack).

Custom player names or positions instead of default numbering.

Export the 3D formation as an image or video.

Real-time formation editing with drag-and-drop functionality.

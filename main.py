# Realistic 3D Soccer Field with Formation
# Requirements: matplotlib
# Run: pip install matplotlib

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Real soccer pitch dimensions (meters)
PITCH_LENGTH = 105
PITCH_WIDTH = 68

def parse_formation(formation_str):
    """Convert formation string '4-3-3' into list of player counts per line."""
    try:
        return [int(x) for x in formation_str.strip().split('-')]
    except ValueError:
        print("Invalid formation format. Use format like '4-3-3'.")
        return []

def generate_positions(formation):
    """Generate X, Y, Z coordinates for players on the pitch."""
    positions = []
    num_lines = len(formation)
    depth_step = (PITCH_LENGTH - 10) / (num_lines + 1)  # leave 5m from each goal line
    
    # Goalkeeper
    positions.append((PITCH_WIDTH/2, 5, 0))
    
    # Field lines (defenders, midfielders, forwards)
    for i, players_in_line in enumerate(formation):
        y = 5 + depth_step * (i + 1)
        if players_in_line == 1:
            xs = [PITCH_WIDTH/2]
        else:
            spacing = PITCH_WIDTH / (players_in_line + 1)
            xs = [spacing * (j + 1) for j in range(players_in_line)]
        for x in xs:
            positions.append((x, y, 0))
    return positions

def plot_3d_field(positions):
    """Plot realistic soccer field and players in 3D."""
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw pitch green background
    ax.plot([0, PITCH_WIDTH, PITCH_WIDTH, 0, 0],
            [0, 0, PITCH_LENGTH, PITCH_LENGTH, 0],
            [0,0,0,0,0], color='green', linewidth=4)
    
    # Draw outer lines
    ax.plot([0, PITCH_WIDTH, PITCH_WIDTH, 0, 0],
            [0,0,PITCH_LENGTH,PITCH_LENGTH,0],
            [0,0,0,0,0], color='white', linewidth=2)
    
    # Halfway line
    ax.plot([0, PITCH_WIDTH],[PITCH_LENGTH/2, PITCH_LENGTH/2],[0,0], color='white', linewidth=2)
    
    # Center circle
    theta = np.linspace(0, 2*np.pi, 100)
    r = 9.15  # 9.15m radius
    x_circle = PITCH_WIDTH/2 + r*np.cos(theta)
    y_circle = PITCH_LENGTH/2 + r*np.sin(theta)
    ax.plot(x_circle, y_circle, np.zeros_like(theta), color='white', linewidth=1.5)
    
    # Penalty areas
    penalty_width = 40.3  # meters
    penalty_depth = 16.5
    # Bottom penalty area
    ax.plot([PITCH_WIDTH/2 - penalty_width/2, PITCH_WIDTH/2 + penalty_width/2, 
             PITCH_WIDTH/2 + penalty_width/2, PITCH_WIDTH/2 - penalty_width/2, PITCH_WIDTH/2 - penalty_width/2],
            [0,0,penalty_depth,penalty_depth,0],[0,0,0,0,0], color='white', linewidth=1.5)
    # Top penalty area
    ax.plot([PITCH_WIDTH/2 - penalty_width/2, PITCH_WIDTH/2 + penalty_width/2, 
             PITCH_WIDTH/2 + penalty_width/2, PITCH_WIDTH/2 - penalty_width/2, PITCH_WIDTH/2 - penalty_width/2],
            [PITCH_LENGTH - penalty_depth, PITCH_LENGTH - penalty_depth, PITCH_LENGTH, PITCH_LENGTH, PITCH_LENGTH - penalty_depth],
            [0,0,0,0,0], color='white', linewidth=1.5)
    
    # Goal boxes
    goal_width = 7.32
    goal_depth = 5.5
    # Bottom
    ax.plot([PITCH_WIDTH/2 - goal_width/2, PITCH_WIDTH/2 + goal_width/2,
             PITCH_WIDTH/2 + goal_width/2, PITCH_WIDTH/2 - goal_width/2, PITCH_WIDTH/2 - goal_width/2],
            [0,0,goal_depth,goal_depth,0],[0,0,0,0,0], color='white', linewidth=1)
    # Top
    ax.plot([PITCH_WIDTH/2 - goal_width/2, PITCH_WIDTH/2 + goal_width/2,
             PITCH_WIDTH/2 + goal_width/2, PITCH_WIDTH/2 - goal_width/2, PITCH_WIDTH/2 - goal_width/2],
            [PITCH_LENGTH - goal_depth, PITCH_LENGTH - goal_depth, PITCH_LENGTH, PITCH_LENGTH, PITCH_LENGTH - goal_depth],
            [0,0,0,0,0], color='white', linewidth=1)
    
    # Players
    xs, ys, zs = zip(*positions)
    ax.scatter(xs, ys, zs, color='red', s=100)
    
    # Annotate players
    for idx, (x, y, z) in enumerate(positions, start=1):
        ax.text(x, y, z+0.5, str(idx), color='white', ha='center', va='bottom', fontsize=9, weight='bold')
    
    # Labels and limits
    ax.set_xlim(0, PITCH_WIDTH)
    ax.set_ylim(0, PITCH_LENGTH)
    ax.set_zlim(0, 5)
    ax.set_xlabel('Width (m)')
    ax.set_ylabel('Length (m)')
    ax.set_zlabel('Height (m)')
    ax.set_title('3D Soccer Field with Formation')
    
    plt.tight_layout()
    plt.show()

def main():
    print("=== 3D Soccer Field Viewer ===")
    num_players = input("Enter number of players (default 11): ").strip()
    num_players = int(num_players) if num_players else 11
    formation_str = input("Enter formation (e.g., 4-3-3): ").strip()
    
    formation = parse_formation(formation_str)
    if sum(formation) + 1 != num_players:
        print(f"Warning: Formation does not match number of players. Adjusting players to {sum(formation)+1}.")
        num_players = sum(formation) + 1
    
    positions = generate_positions(formation)
    plot_3d_field(positions)

if __name__ == "__main__":
    main()

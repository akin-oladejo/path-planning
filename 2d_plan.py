from raylib.colors import *
from raylib import rl, ffi

# Initialize window

# Initialize window
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 700
rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"Floor Plan")
rl.SetTargetFPS(60)

# Define colors
WALL_COLOR = BLACK
FLOOR_COLOR = LIGHTGRAY
DOOR_COLOR = BROWN

# Define walls and rooms
walls = [
    # Outer walls
    (50, 50, 1604, 4),   # Top
    (50, 50, 4, 600),   # Left
    (1650, 50, 4, 600),  # Right
    (50, 650, 1604, 4),  # Bottom

    # Vertical inner walls
    (450, 50, 7, 50),
    (450, 200, 7, 450),

    (950, 50, 7, 350),

    (1250, 50, 7, 450),
    (1250, 600, 7, 50),

    # Horizontal inner walls
    (950, 250, 150, 7),
    (1200, 250, 50, 7),

    (950, 400, 110, 7),
]

# Define doors
# doors = [
#     (355, 200, 10, 60),  # Door between left rooms
#     (500, 305, 60, 10),  # Door to bottom right room
# ]

# Convert walls and doors to Rectangle structs
c_walls = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in walls]
# c_doors = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in doors]

# Main game loop
while not rl.WindowShouldClose():
    rl.BeginDrawing()
    rl.ClearBackground(WHITE)

    # Draw floors
    rl.DrawRectangle(50, 50, 1600, 600, FLOOR_COLOR)

    # Draw walls
    for wall in c_walls:
        rl.DrawRectangleRec(wall[0], WALL_COLOR)

    # Draw doors
    # for door in c_doors:
    #     rl.DrawRectangleRec(door[0], DOOR_COLOR)

    # Add labels to rooms
    rl.DrawText(b"Bedroom 1", 100, 200, 20, RED)
    rl.DrawText(b"Bedroom 2", 1400, 400, 20, RED)
    rl.DrawText(b"Living Room", 550, 150, 20, RED)
    rl.DrawText(b"Kitchen", 550, 500, 20, RED)
    rl.DrawText(b"Bathroom", 1000, 200, 20, RED)
    rl.DrawText(b"Laundry", 1000, 300, 20, RED)

    rl.EndDrawing()

rl.CloseWindow()
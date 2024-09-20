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
FURNITURE_COLOR = PINK

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

furniture = [
    # bedroom 1
    (54, 225, 40, 50), # bedside drawer 1
    (54, 280, 220, 150), # bed
    (54, 435, 40, 50), # bedside drawer 2
    (300, 600, 150, 50), # wardrobe 1

    # kitchen
    (458, 500, 50, 150), # cabinet 1
    (510, 590, 130, 60), # cabinet 2

    # bathroom
    (1176, 54, 70, 60), # wc
    (960, 186, 100, 60), # tub

    # laundry
    (960, 260, 50, 70), # washer

    # bedroom 2
    (1337, 54, 50, 40), # bedside drawer 1
    (1390, 54, 150, 220), # bed
    (1544, 54, 50, 40), # bedside drawer 2
    (1500, 600, 150, 50), # wardrobe 1
]

# Define doors
# doors = [
#     (355, 200, 10, 60),  # Door between left rooms
#     (500, 305, 60, 10),  # Door to bottom right room
# ]

# Convert walls and furniture to Rectangle structs
c_walls = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in walls]
c_furniture = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in furniture]

# living room table is a cirle
# center_table = [ffi.new("Circle *", [700, 300, 100])]
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

    # Draw walls
    for furniture in c_furniture:
        rl.DrawRectangleRec(furniture[0], FURNITURE_COLOR)

    # for i in center_table:
    rl.DrawCircle(700, 300, 100, FURNITURE_COLOR)
    # Draw doors
    # for door in c_doors:
    #     rl.DrawRectangleRec(door[0], DOOR_COLOR)

    # Add labels to rooms
    rl.DrawText(b"Bedroom 1", 200, 450, 20, RED)
    rl.DrawText(b"Bedroom 2", 1400, 400, 20, RED)
    rl.DrawText(b"Living Room", 650, 150, 20, RED)
    rl.DrawText(b"Kitchen", 550, 530, 20, RED)
    rl.DrawText(b"Bathroom", 1050, 150, 20, RED)
    rl.DrawText(b"Laundry", 1050, 320, 20, RED)

    rl.EndDrawing()

rl.CloseWindow()
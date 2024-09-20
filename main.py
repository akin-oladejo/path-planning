# from raylib.colors import *
# from raylib import rl, ffi

# # Initialize window

# # Initialize window
# SCREEN_WIDTH = 1700
# SCREEN_HEIGHT = 700
# rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"Floor Plan")
# rl.SetTargetFPS(60)

# # Define colors
# WALL_COLOR = GRAY
# FLOOR_COLOR = LIGHTGRAY
# DOOR_COLOR = BROWN

# # Define walls and rooms
# walls = [
#     # Outer walls
#     (50, 50, 700, 20),   # Top
#     (50, 50, 20, 500),   # Left
#     (730, 50, 20, 500),  # Right
#     (50, 530, 700, 20),  # Bottom

#     # Inner walls
#     (350, 50, 20, 250),  # Vertical divider
#     (50, 300, 320, 20),  # Horizontal divider left
#     (370, 300, 380, 20), # Horizontal divider right
# ]

# # Define doors
# doors = [
#     (355, 200, 10, 60),  # Door between left rooms
#     (500, 305, 60, 10),  # Door to bottom right room
# ]

# # Convert walls and doors to Rectangle structs
# c_walls = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in walls]
# c_doors = [ffi.new("Rectangle *", [x, y, w, h]) for x, y, w, h in doors]

# # Main game loop
# while not rl.WindowShouldClose():
#     rl.BeginDrawing()
#     rl.ClearBackground(WHITE)

#     # Draw floors
#     rl.DrawRectangle(70, 70, 660, 460, FLOOR_COLOR)

#     # Draw walls
#     for wall in c_walls:
#         rl.DrawRectangleRec(wall[0], WALL_COLOR)

#     # Draw doors
#     for door in c_doors:
#         rl.DrawRectangleRec(door[0], DOOR_COLOR)

#     # Add labels to rooms
#     rl.DrawText(b"Living Room", 100, 150, 20, BLACK)
#     rl.DrawText(b"Kitchen", 500, 150, 20, BLACK)
#     rl.DrawText(b"Bedroom", 100, 400, 20, BLACK)
#     rl.DrawText(b"Bathroom", 500, 400, 20, BLACK)

#     rl.EndDrawing()

# rl.CloseWindow()

# from raylib.colors import *
# from raylib import ffi, rl
# import math

# # Initialize window
# SCREEN_WIDTH = 1700
# SCREEN_HEIGHT = 700
# rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"3D Floor Plan")
# rl.SetTargetFPS(60)

# # Define colors
# WALL_COLOR = GRAY
# FLOOR_COLOR = LIGHTGRAY
# CEILING_COLOR = WHITE

# # Define camera
# camera = ffi.new("Camera3D *", [
#     [0.0, 10.0, 10.0],   # position
#     [0.0, 0.0, 0.0],     # target
#     [0.0, 1.0, 0.0],     # up
#     45.0,                # fov
#     rl.CAMERA_PERSPECTIVE
# ])

# # Define walls (x, z, width, height)
# walls = [
#     # Outer walls
#     (0, 0, 10, 3),     # Front
#     (0, 0, 3, 10),     # Left
#     (10, 0, 3, 10),    # Right
#     (0, 10, 10, 3),    # Back

#     # Inner walls
#     (5, 0, 3, 5),      # Vertical divider
#     (0, 5, 5, 3),      # Horizontal divider left
#     (5, 5, 5, 3),      # Horizontal divider right
# ]

# # Main game loop
# while not rl.WindowShouldClose():
#     # Update camera
#     rl.UpdateCamera(camera, rl.CAMERA_ORBITAL)

#     rl.BeginDrawing()
#     rl.ClearBackground(RAYWHITE)

#     rl.BeginMode3D(camera[0])

#     # Draw floor
#     rl.DrawPlane((5.0, 0.0, 5.0), (10.0, 10.0), FLOOR_COLOR)

#     # Draw ceiling
#     rl.DrawPlane((5.0, 3.0, 5.0), (10.0, 10.0), CEILING_COLOR)

#     # Draw walls
#     for wall in walls:
#         x, z, width, height = wall
#         rl.DrawCube((x + width/2, 1.5, z + height/2), width, 3.0, height, WALL_COLOR)
#         rl.DrawCubeWires((x + width/2, 1.5, z + height/2), width, 3.0, height, DARKGRAY)

#     # Draw room labels
#     rl.DrawCube((2.5, 0.01, 2.5), 0.1, 0.1, 0.1, BLACK)  # Living Room marker
#     rl.DrawCube((7.5, 0.01, 2.5), 0.1, 0.1, 0.1, BLACK)  # Kitchen marker
#     rl.DrawCube((2.5, 0.01, 7.5), 0.1, 0.1, 0.1, BLACK)  # Bedroom marker
#     rl.DrawCube((7.5, 0.01, 7.5), 0.1, 0.1, 0.1, BLACK)  # Bathroom marker

#     rl.EndMode3D()

#     # Draw room labels in 2D
#     rl.DrawText(b"Living Room", 10, 40, 20, BLACK)
#     rl.DrawText(b"Kitchen", 10, 70, 20, BLACK)
#     rl.DrawText(b"Bedroom", 10, 100, 20, BLACK)
#     rl.DrawText(b"Bathroom", 10, 130, 20, BLACK)

#     rl.DrawFPS(10, 10)

#     rl.EndDrawing()

# rl.CloseWindow()

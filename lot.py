from raylib.colors import *
from raylib import rl, ffi

def main():
    # Define colors
    EGO_COLOR = LIME

    # Initialize window
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 900
    rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"Parking Lot")
    rl.SetTargetFPS(60)

    # Load texture
    car = rl.LoadTexture(b"assets/car.png")

    # CAR arguments
    CAR_SPEED = 7.0
    ACCELERATION = 0.3
    # CAR_SIZE = 15
    CAR_POS = ffi.new("Vector2 *")
    CAR_POS.x = SCREEN_WIDTH/2
    CAR_POS.y = SCREEN_HEIGHT/2
    CAR_WIDTH = 40
    CAR_HEIGHT = 60
    CAR_STEER_ANGLE = 0

    # Main game loop
    while not rl.WindowShouldClose():
        rl.BeginDrawing()
        rl.ClearBackground(WHITE)

        # Update triangle position based on key presses
        if rl.IsKeyDown(rl.KEY_RIGHT):
            CAR_POS.x += CAR_SPEED
        if rl.IsKeyDown(rl.KEY_LEFT):
            CAR_POS.x -= CAR_SPEED
        if rl.IsKeyDown(rl.KEY_DOWN):
            CAR_POS.y += CAR_SPEED
        if rl.IsKeyDown(rl.KEY_UP):
            CAR_POS.y -= CAR_SPEED

        # Keep the triangle within the screen bounds
        CAR_POS.x = max(0, min(SCREEN_WIDTH - car.width, CAR_POS.x))
        CAR_POS.y = max(150, min(SCREEN_HEIGHT - car.height, CAR_POS.y))
        # CAR_X = 50
        # CAR_Y = 50

        # Draw map area
        rl.DrawRectangle(0, 150, 1300, 750, RAYWHITE)

        # # Draw walls
        # for wall in c_walls:
        #     rl.DrawRectangleRec(wall[0], WALL_COLOR)

        # # Draw walls
        # for furniture in c_furniture:
        #     rl.DrawRectangleRec(furniture[0], FURNITURE_COLOR)

        # Draw the CAR
        # rl.DrawRectangle(CAR_POS.x, CAR_POS.y, CAR_WIDTH, CAR_HEIGHT, EGO_COLOR)

        # Draw the car texture
        rl.DrawTextureV(car, CAR_POS[0], WHITE)


        # for i in center_table:
        # rl.DrawCircle(700, 300, 50, FURNITURE_COLOR)

        # Draw doors
        # for door in c_doors:
        #     rl.DrawRectangleRec(door[0], DOOR_COLOR)

        

        # Add labels
        steer_angle = f"Steering Angle: {CAR_STEER_ANGLE}".encode('utf-8')
        rl.DrawText(steer_angle, 20, 20, 20, BLACK)

        speed = f"Speed: {CAR_SPEED}".encode('utf-8')
        rl.DrawText(speed, 20, 50, 20, BLACK)

        # rl.DrawText(b"Bathroom", 1050, 150, 20, RED)
        # rl.DrawText(b"Laundry", 1050, 320, 20, RED)

        rl.EndDrawing()

    # de-initialization
    rl.UnloadTexture(car)
    rl.CloseWindow()

if __name__ == '__main__':
    main()
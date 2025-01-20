from raylib.colors import *
from raylib import rl, ffi

def main():
    # Define colors
    EGO_COLOR = LIME

    # Initialize window
    SCREEN_WIDTH = 735
    SCREEN_HEIGHT = 980
    rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b"Vacuum bot")
    rl.SetTargetFPS(60)

    # Load textures
    # ego = rl.LoadTexture(b"assets/ego.png")
    # vehicle = rl.LoadTexture(b"assets/car2.png")
    bg = rl.LoadTexture(b'assets/floor-plan.png')

    # Rotation angle (in degrees)
    rotation = 30.0

    # Scale (1.0 = original size)
    scale = 1.0

    # ego arguments
    EGO_SPEED = 7.0
    ACCELERATION = 0.3
    EGO_POS = ffi.new("Vector2 *")
    EGO_POS.x = 0
    EGO_POS.y = SCREEN_HEIGHT
    EGO_STEER_ANGLE = 0
    

    # Main game loop
    while not rl.WindowShouldClose():
        # Update rotation
        # rotation += 1.0  # Rotate 1 degree per frame
        # if rotation >= 360.0:
        #     rotation -= 360.0

        rl.BeginDrawing()
        rl.ClearBackground(WHITE)

        

        # Update triangle position based on key presses
        if rl.IsKeyDown(rl.KEY_RIGHT):
            # EGO_STEER_ANGLE += .1
            EGO_POS.x += EGO_SPEED

        if rl.IsKeyDown(rl.KEY_LEFT):
            # EGO_STEER_ANGLE -= .1
            EGO_POS.x -= EGO_SPEED
        if rl.IsKeyDown(rl.KEY_DOWN):
            EGO_POS.y += EGO_SPEED
            # EGO_POS.x += EGO_STEER_ANGLE
            # EGO_POS.y -= EGO_SPEED * math.cos(rotation + EGO_STEER_ANGLE)
            # EGO_POS.x += EGO_SPEED * math.sin(rotation + EGO_STEER_ANGLE)
        if rl.IsKeyDown(rl.KEY_UP):
            EGO_POS.y -= EGO_SPEED
            # EGO_POS.y += EGO_SPEED * math.cos(rotation + EGO_STEER_ANGLE)
            # EGO_POS.x -= EGO_SPEED * math.sin(rotation + EGO_STEER_ANGLE)

        # Keep the ego within the screen bounds
        EGO_POS.x = max(0, min(SCREEN_WIDTH - ego.width, EGO_POS.x))
        EGO_POS.y = max(150, min(SCREEN_HEIGHT - ego.height, EGO_POS.y))

        # Clip the steering angle within +/_ 20 degrees
        EGO_STEER_ANGLE = max(-20.0, min(20.0, EGO_STEER_ANGLE))


        # EGO_X = 50
        # EGO_Y = 50

        # Draw map area
        rl.DrawRectangle(0, 150, 1300, 750, RAYWHITE)

        rl.DrawTextureEx(bg, (0,0), 0.0, 0.6, WHITE)

        # rl.Draw

        # Draw the ego
        # rl.DrawRectangle(EGO_POS.x, EGO_POS.y, EGO_WIDTH, EGO_HEIGHT, EGO_COLOR)

        # Draw the ego texture
        # rl.DrawTextureEx(ego, EGO_POS[0], rotation + EGO_STEER_ANGLE, scale, WHITE)
        # rl.DrawTextureEx(ego, (EGO_POS[0].x + ego.width//2, EGO_POS[0].y + ego.height//2,), EGO_STEER_ANGLE, scale, WHITE)


        # for i in range(100, 500, 100):
        #     rl.DrawTextureEx(vehicle, (i, 200), 0.0, scale, WHITE)


        # for i in center_table:
        # rl.DrawCircle(700, 300, 50, FURNITURE_COLOR)

        # Draw doors
        # for door in c_doors:
        #     rl.DrawRectangleRec(door[0], DOOR_COLOR)

        # Add labels
        steer_angle = f"Steering Angle: {EGO_STEER_ANGLE}".encode('utf-8')
        rl.DrawText(steer_angle, 20, 20, 20, BLACK)

        speed = f"Speed: {EGO_SPEED}".encode('utf-8')
        rl.DrawText(speed, 20, 50, 20, BLACK)

        rotation_b = f"Rotation: {rotation}".encode('utf-8')
        rl.DrawText(rotation_b, 20, 80, 20, BLACK)

        rl.DrawText(b'Plan from https://dolive.media/496/', 20, 940, 15, RED)
        # rl.DrawText(b"Bathroom", 1050, 150, 20, RED)
        # rl.DrawText(b"Laundry", 1050, 320, 20, RED)

        rl.EndDrawing()

    # de-initialization
    rl.UnloadTexture(ego)
    rl.UnloadTexture(vehicle)
    rl.CloseWindow()

if __name__ == '__main__':
    main()
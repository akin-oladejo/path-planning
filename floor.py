from pyray import *

# Initialization
SCREEN_WIDTH = 735
SCREEN_HEIGHT = 980

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "House Bot") # create window
set_target_fps(60) # game runs at 60fps

# house plan
house_img = load_image(b"assets/floor-plan.png")
house = load_texture_from_image(house_img)


# vacuum bot
bot_img = load_image(b"assets/bot.png")
bot = load_texture_from_image(bot_img)

# eject images from memnory
unload_image(house_img)
unload_image(bot_img)


# bot position
pos = Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
SPEED = 2.0
rot = 0


# Update rotation
        # rotation += 1.0  # Rotate 1 degree per frame
        # if rotation >= 360.0:
        #     rotation -= 360.0

while not window_should_close():
    # keyboard input
    if is_key_down(KeyboardKey.KEY_D):
        pos.x += SPEED
    if is_key_down(KeyboardKey.KEY_A):
        pos.x -= SPEED
    if is_key_down(KeyboardKey.KEY_W):
        pos.y -= SPEED
    if is_key_down(KeyboardKey.KEY_S):
        pos.y += SPEED

    # mouse input
    pointer_pos = get_mouse_position()

    # if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT)
    begin_drawing() # set up canvas (framebuffer) to start drawing

    # draw floor plan
    draw_texture_ex(house, (0,0), 0.0, 0.6, WHITE)

    # draw bot
    draw_texture_ex(bot, pos, 0.0, 0.1, WHITE)

    # draw pointer
    draw_circle_v(pointer_pos, 10, DARKBLUE)

    # add labels
    steer_angle = f"Steering Angle: ".encode('utf-8')
    draw_text(steer_angle, 20, 20, 17, BLACK)

    speed = f"Speed: ".encode('utf-8')
    draw_text(speed, 20, 40, 17, BLACK)

    rotation_b = f"Rotation: {rot}".encode('utf-8')
    draw_text(rotation_b, 20, 60, 17, BLACK)

    end_drawing() # end canvas and swap buffers    
close_window()
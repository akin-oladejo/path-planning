from pyray import *

# Initialization
SCREEN_WIDTH = 735
SCREEN_HEIGHT = 980

init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "House Bot")  # create window
set_target_fps(60)  # game runs at 60fps

# house plan
house_img = load_image(b"assets/floor-plan.png")
house = load_texture_from_image(house_img)


# vacuum bot
bot_img = load_image(b"assets/bot.png")
bot = load_texture_from_image(bot_img)
bot_width = bot.width
bot_height = bot.height
bot_origin = Vector2(bot_width / 2, bot_height / 2)

# eject images from memnory
unload_image(house_img)
unload_image(bot_img)


# bot params
SCALE = 0.1
POS = Vector2(
    SCREEN_WIDTH / 2 + (bot_origin.x * SCALE),
    SCREEN_HEIGHT / 2 + (bot_origin.y * SCALE),
)
SPEED = 2.0
rot = 0


while not window_should_close():
    # keyboard input
    if is_key_down(KeyboardKey.KEY_D):
        POS.x += SPEED
    if is_key_down(KeyboardKey.KEY_A):
        POS.x -= SPEED
    if is_key_down(KeyboardKey.KEY_W):
        POS.y -= SPEED
    if is_key_down(KeyboardKey.KEY_S):
        POS.y += SPEED
    if is_key_down(KeyboardKey.KEY_LEFT):
        rot -= 1
        if rot < 0:
            rot = 359
    if is_key_down(KeyboardKey.KEY_RIGHT):
        rot += 1
        if rot > 359:
            rot = 0

    # mouse input
    pointer_pos = get_mouse_position()

    # set bg to white
    begin_drawing()  # set up canvas (framebuffer) to start drawing
    clear_background(RAYWHITE)

    # draw floor plan
    draw_texture_ex(house, (0, 0), 0.0, 0.6, WHITE)

    # draw bot, scale and offset
    draw_texture_pro(
        bot,
        [0, 0, bot_width, bot_height],
        [POS.x, POS.y, bot_width * SCALE, bot_height * SCALE], 
        vector2_scale(bot_origin, SCALE), # scale the origin too 
        rot, # rotation
        WHITE,
    )

    # draw pointer
    draw_circle_v(pointer_pos, 10, DARKBLUE)

    # add labels
    steer_angle = f"Steering Angle: ".encode("utf-8")
    draw_text(steer_angle, 20, 20, 17, BLACK)

    speed = f"Speed: ".encode("utf-8")
    draw_text(speed, 20, 40, 17, BLACK)

    rotation_b = f"Rotation: {rot}°".encode("utf-8")
    draw_text(rotation_b, 20, 60, 17, BLACK)

    end_drawing()  # end canvas and swap buffers
close_window()

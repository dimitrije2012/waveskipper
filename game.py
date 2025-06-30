# project wave jumping

# initial
from ursina import *
from math import sin
app = Ursina()

window.title = 'projekat'
window.borderless = False
window.fullscreen = False   
window.exit_button.visible = False     
window.fps_counter.enabled = False   

# sun copied
DirectionalLight(y=2, rotation=(45, -45, 45))
Sky()  # built-in skybox


# ground templated with modifications
pod = Entity(
    model='plane',
    scale=(50,1,50),
    texture='white_cube',
    color=color.rgb(194,178,128),  # sandy
    collider='box',
    position=(0,0,0)
)

# invisible player 1st person template
player = Entity(position=(0,1,0), collider='box')
camera.parent = player
camera.position = (0, 1.5, -10)  # minus fov
camera.rotation_x = 10

# wave starts small then gets higher and higher
talas = Entity(
    model='cube',
    color=color.azure,
    scale=(5, 0.5, 1),
    position=(0, 0.5, 50),
    collider='box'
)

# variables for jump, copied from ursina_for_dummies.html
velocity_y = 0
gravity = 20
jump_force = 18 
is_jumping = False

# default game variable
game_over = False
score = 0
talas_brzina = 10
talas_spawn_distance = 50
segment_count = 10 

# ui
score_txt = Text(text=f"Score: {score}", position=(-0.85, 0.45), origin=(0,0), scale=1.5)
game_over_txt = Text(text='', position=(0, 0), origin=(0,0), scale=2, color=color.red)

# wave segments (different heights)
talas_segments = []

# foam (ADD ASSETS!!!!!)
pena = Entity(
    model='plane',
    color=color.white,
    scale=5,
    position=(0,0,0),
    rotation_x=90,
    alpha=0,
    double_sided=True
)

# hide foam and add fadeout
pena_fade_speed = 2 
pena_active = False


def spawn_talas(z_pos): # copied from cheatsheet
    segment_width = talas_width / segment_count
    segments = []
    for i in range(segment_count):
        x_pos = -talas_width / 2 + i * segment_width + segment_width/2

        base_wave = sin((i / segment_count) * 2 * pi * 3)
        randomness = uniform(-0.5, 0.5)
        height = max(0.5, (base_wave + 1) * 2 + randomness)

        segment = Entity(
            model='cube',
            color=color.azure,
            scale=(segment_width * 0.95, height, 1),
            position=(x_pos, height/2, z_pos),
            collider='box'
        )
        segments.append(segment)
    return segments


MAX_TALAS_VISINA = 3.5

# finally
def update():
    global velocity_y, is_jumping, game_over, score

    if game_over:
        return
    
    # player coordinates
    player.x = clamp(player.x, -23, 23)
    player.z = clamp(player.z, -23, 23)


   # wave forward
    talas.z -= 10 * time.dt

    # distance some math
    distance_ratio = max(min((50 - talas.z) / 50, 1), 0)

    # grow as you go forward
    talas.scale_y = lerp(0.5, MAX_TALAS_VISINA, distance_ratio)
    talas.y = talas.scale_y / 2 

    # reset wave + give points
    if talas.z < player.z:
        if is_jumping:
            score += 1
            score_txt.text = f"Score: {score}"
            talas.z = 50
            talas.scale_y = 0.5
        else:
            game_over = True
            game_over_txt.text = "💀 game over 💀\nR za retry"

    # jump
    if held_keys['space'] and not is_jumping:
        velocity_y = jump_force
        is_jumping = True

    if is_jumping:
        velocity_y -= gravity * time.dt
        player.y += velocity_y * time.dt

        if player.y <= 1:
            player.y = 1
            is_jumping = False
            velocity_y = 0

# from the beginning
def input(key):
    global game_over, score
    if key == 'r' and game_over:
        game_over = False
        player.y = 1
        talas.z = 50
        talas.scale_y = 0.5
        score = 0
        score_txt.text = "Score: 0"
        game_over_txt.text = ''

app.run() # made a mistake here, forgot this

import pgzrun as p
from pgzero.builtins import Actor, keyboard

TITLE = "Bouncing Bob"
WIDTH = 800
HEIGHT = 600
GRAVITY = 1.5
JUMPSPEED = 10
MOVEMENTSPEED = 2

bob = Actor('bob') 
bob_attributes = {'jumping': False, 'velocity': 0}
bob.pos = HEIGHT/2, WIDTH/2
#lvl.pos = 0, 0
ground = Rect((0, 500, WIDTH, 100))                               # type: ignore

def draw():
    screen.fill((225, 225, 255))                                  # type: ignore
    screen.draw.filled_rect(ground, (150, 255, 150))              # type: ignore
    bob.draw()

def update():
    global bob, ground
    
    bob.y += GRAVITY

    if bob_attributes['jumping']:
        bob.y -= bob_attributes['velocity']
        bob_attributes['velocity'] -= GRAVITY/2
        if bob_attributes['velocity'] < 0:  
            bob_attributes['jumping'] = False 

    if bob.bottom > ground.top:
        bob.bottom = ground.top
        bob_attributes['velocity'] = 0

    if (keyboard.up or keyboard.space or keyboard.w) and bob.bottom == ground.top:
        bob_attributes['jumping'] = True
        bob_attributes['velocity'] = JUMPSPEED
    if keyboard.left or keyboard.a:
        bob.x -= MOVEMENTSPEED
    if keyboard.right or keyboard.d:
        bob.x += MOVEMENTSPEED


p.go()
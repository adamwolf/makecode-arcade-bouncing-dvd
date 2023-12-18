"""

Bouncing DVD

August 2021

Adam Wolf

"""

def on_a_pressed():
    dvdlogo.set_velocity(30, 30)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def randomlogo():
    dvdlogo.set_image(logos._pick_random())
bounce_y = False
bounce_x = False
logos: List[Image] = []
dvdlogo: Sprite = None
dvdlogo = sprites.create(assets.image("""
    dvdwhite
"""), SpriteKind.player)
controller.move_sprite(dvdlogo)
dvdlogo.set_velocity(30, 30)
logos = [assets.image("""
        dvdwhite
    """),
    assets.image("""
        dvdred
    """),
    assets.image("""
        dvdpink
    """),
    assets.image("""
        dvdorange
    """),
    assets.image("""
        dvdgreen
    """),
    assets.image("""
        dvdblue
    """),
    assets.image("""
        dvdlightblue
    """),
    assets.image("""
        dvdpurple
    """),
    assets.image("""
        dvdgray
    """),
    assets.image("""
        dvdnavy
    """)]

def on_on_update():
    global bounce_x, bounce_y
    bounce_x = False
    if dvdlogo.left <= 0 and dvdlogo.vx < 0:
        bounce_x = True
        dvdlogo.vx = dvdlogo.vx * -1
        randomlogo()
    elif dvdlogo.right >= scene.screen_width() and dvdlogo.vx > 0:
        bounce_x = True
        dvdlogo.vx = dvdlogo.vx * -1
        randomlogo()
    bounce_y = False
    if dvdlogo.top <= 0 and dvdlogo.vy < 0:
        bounce_y = True
        dvdlogo.vy = dvdlogo.vy * -1
        randomlogo()
    elif dvdlogo.bottom >= scene.screen_height() and dvdlogo.vy > 0:
        bounce_y = True
        dvdlogo.vy = dvdlogo.vy * -1
        randomlogo()
game.on_update(on_on_update)

def on_forever():
    global bounce_x, bounce_y
    if bounce_x and bounce_y:
        bounce_x = False
        bounce_y = False
        music.ba_ding.play()
        info.change_score_by(1)
        effects.confetti.start_screen_effect()
        pause(2000)
        effects.confetti.end_screen_effect()
forever(on_forever)

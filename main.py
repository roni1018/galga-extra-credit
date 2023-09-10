my_sprite2 = sprites.create(img("""
    . . . . . f f 4 4 f f . . . . .
    . . . . f 5 4 5 5 4 5 f . . . .
    . . . f e 4 5 5 5 5 4 e f . . .
    . . f b 3 e 4 4 4 4 e 3 b f . .
    . . f 3 3 3 3 3 3 3 3 3 3 f . .
    . f 3 3 e b 3 e e 3 b e 3 3 f .
    . f 3 3 f f e e e e f f 3 3 f .
    . f b b f b f e e f b f b b f .
    . f b b e 1 f 4 4 f 1 e b b f .
    f f b b f 4 4 4 4 4 4 f b b f f
    f b b f f f e e e e f f f b b f
    . f e e f b d d d d b f e e f .
    . . e 4 c d d d d d d c 4 e . .
    . . e f b d b d b d b b f e . .
    . . . f f 1 d 1 d 1 d f f . . .
    . . . . . f f b b f f . . . . .
"""), SpriteKind.player)
my_sprite2.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(my_sprite2, 200, 200)
def on_event_pressed():
   projectile = sprites.create_projectile_from_sprite(img("""
       . . . . . . . .
       . . . . . . . .
       . . . . . . . .
       . . . . . . . .
       . b b d d b b .
       b 1 1 3 3 1 1 b
       b 1 3 5 5 3 1 b
       b d 3 5 5 3 d b
       c 1 1 d d 1 1 c
       c d 1 d d 1 d c
       . c c 7 6 c c .
       . . 6 7 6 . . .
       . . 6 6 8 8 8 6
       . . 6 8 7 7 7 6
       . . 8 7 7 7 6 .
       . . 8 8 8 6 . .
   """), my_sprite2, 200, 0) 
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)
def on_update_interval():
    bogey = sprites.create(img("""
        ....................ccfff...........
        ..........fffffffffcbbbbf...........
        .........fbbbbbbbbbfffbf............
        .........fbb111bffbbbbff............
        .........fb11111ffbbbbbcff..........
        .........f1cccc11bbcbcbcccf.........
        ..........fc1c1c1bbbcbcbcccf...ccccc
        ............c3331bbbcbcbccccfccddbbc
        ...........c333c1bbbbbbbcccccbddbcc.
        ...........c331c11bbbbbcccccccbbcc..
        ..........cc13c111bbbbccccccffbccf..
        ..........c111111cbbbcccccbbc.fccf..
        ...........cc1111cbbbfdddddc..fbbcf.
        .............cccffbdbbfdddc....fbbf.
        ..................fbdbbfcc......fbbf
        ...................fffff.........fff
    """), SpriteKind.enemy)
    bogey.set_velocity(-100,0)
    bogey.left = scene.screen_width()
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY,True)
game.on_update_interval(500, on_update_interval)
def on_on_overlap(sprite, othersprite):
    othersprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)
def on_projectile_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_projectile_overlap)
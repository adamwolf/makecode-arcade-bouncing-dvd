/**
 * Adam Wolf
 * 
 * Bouncing DVD Logo in MakeCode Arcade
 * 
 * August 2021 -
 */
// Bouncing DVD
// 
// August 2021
// 
// Adam Wolf
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    dvdlogo.setVelocity(30, 30)
})
function randomlogo () {
    dvdlogo.setImage(logos._pickRandom())
}
let bounce_y = false
let bounce_x = false
let logos: Image[] = []
let dvdlogo: Sprite = null
dvdlogo = sprites.create(assets.image`dvdwhite`, SpriteKind.Player)
controller.moveSprite(dvdlogo)
dvdlogo.setVelocity(30, 30)
logos = [
assets.image`dvdwhite`,
assets.image`dvdred`,
assets.image`dvdpink`,
assets.image`dvdorange`,
assets.image`dvdgreen`,
assets.image`dvdblue`,
assets.image`dvdlightblue`,
assets.image`dvdpurple`,
assets.image`dvdgray`,
assets.image`dvdnavy`
]
game.onUpdate(function () {
    bounce_x = false
    if (dvdlogo.left <= 0 && dvdlogo.vx < 0) {
        bounce_x = true
        dvdlogo.vx = dvdlogo.vx * -1
        randomlogo()
    } else if (dvdlogo.right >= scene.screenWidth() && dvdlogo.vx > 0) {
        bounce_x = true
        dvdlogo.vx = dvdlogo.vx * -1
        randomlogo()
    }
    bounce_y = false
    if (dvdlogo.top <= 0 && dvdlogo.vy < 0) {
        bounce_y = true
        dvdlogo.vy = dvdlogo.vy * -1
        randomlogo()
    } else if (dvdlogo.bottom >= scene.screenHeight() && dvdlogo.vy > 0) {
        bounce_y = true
        dvdlogo.vy = dvdlogo.vy * -1
        randomlogo()
    }
    if (bounce_x && bounce_y) {
        bounce_x = false
        bounce_y = false
        music.baDing.play()
        info.changeScoreBy(1)
        effects.confetti.startScreenEffect()
        pause(2000)
        effects.confetti.endScreenEffect()
    }
})

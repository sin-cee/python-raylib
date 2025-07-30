from pyray import *
windowHeight = int(450)
windowWidth = int(800)

direction = 'down'

position = {
    "width": windowWidth//2,
    "height":  windowHeight//2
}

init_window(windowWidth, windowHeight, "Hello")
set_target_fps(60)

def updateBallPosition():
    global direction
    draw_circle(position['width'], position['height'], 30.0, PINK)
    position['width'] = get_mouse_x()
    position['height'] = get_mouse_y()
    if(position['height'] >= windowHeight):
        direction='up'
    if(position['height'] <=0):
        direction='down'
    
    if(direction =='down'):
        position['height'] += 5
    else:
        position['height'] -= 5

def updateGame():
    begin_drawing()
    clear_background(WHITE)
    updateBallPosition()
    end_drawing()

while not window_should_close():
    updateGame()

close_window()

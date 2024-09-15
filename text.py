import pgzrun
width = 600
height = 400

def draw():
    screen.clear()
    screen.draw.text("Welcome to Pygame",(50,50),color = "red")

    circlecolor = "blue"
    circlecoord = (300,350)
    radius = 50
    screen.draw.filled_circle(circlecoord,radius,circlecolor)


pgzrun.go()
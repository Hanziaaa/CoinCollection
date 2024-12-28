import pgzrun 
from random import randint 
WIDTH = 500
HEIGHT = 500
TITLE = "Coin Collector"

bg = Actor("grass",(WIDTH // 2, HEIGHT //2))
robot = Actor("robot_idle")
coin = Actor("coin_gold")
bomb = Actor("bomb")

velocity = 5
over = False 
timer = 0



def start():
    global velocity, over, timer 
    velocity = 5
    robot.pos = WIDTH //2, HEIGHT // 2 
    move_bomb()
    move_coin()

    #clock.schedule_interval(increment_timer,1.0) 
    #start music()
    music.play("House")

def move_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)
    while coin.colliderect(bomb) or coin.colliderect(robot):
        coin.x = randint(20, WIDTH - 20)
        coin.y = randint(20, HEIGHT - 20)




def move_bomb():
    bomb.x = randint(20, WIDTH - 20)
    bomb.y = randint(20, HEIGHT - 20)
    while bomb.colliderect(robot):
        bomb.x = randint(20, WIDTH - 20)
        bomb.y = randint(20, HEIGHT - 20)


def draw():
    screen.clear()
    bg.draw()
    coin.draw()
    bomb.draw()
    robot.draw()
    if over:
        screen.draw.text("Game Over! ", center=(WIDTH // 2, HEIGHT // 2))
    else:
        robot.draw()




def update():
    #while left key is pressed and not at edge 
    if keyboard.LEFT and robot.left > 0:
        # show left facing image and change x velocity 
        robot.image = "robot_left"
        robot.x += -5
    # while right key is pressed and not at edge 
    elif keyboard.RIGHT and robot.right < WIDTH:
        # show right facing image and change x velocity 
        robot.image = "robot_right"
        robot.x += 5 
        # while UP key is pressed and not at edge 
    elif keyboard.UP and robot.top > 0:
        robot.y -=velocity 
        # while DOWN key is pressed and not at edge 
    elif keyboard.DOWN and robot .bottom < HEIGHT:
        robot.y += velocity 




pgzrun.go()
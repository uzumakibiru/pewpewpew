import turtle
import random

plane_lives=["blue","green","yellow","red"]
active_alien_bullet_list=[]
score_list=[]
#Create Screen
screen=turtle.Screen()
screen.title("PewPewPew")
screen.bgcolor("black")
screen.setup(width=500,height=600)
screen.tracer(0)

#Text for score and lives
score= turtle.Turtle()
score.hideturtle()

score.color("white")

score.penup()
score.setpos(-200,280)
score.write("Score: 0")
lives= turtle.Turtle()
lives.hideturtle()

lives.color("white")

lives.penup()
lives.setpos(160,280)
lives.write("Lives: 4")

def game_lost():

    game_over= turtle.Turtle()
    game_over.hideturtle()

    game_over.color("white")

    game_over.penup()
    game_over.write("Game Over")



#Create the shooting plane
def create_plane_shape():
    plane_shape = ((-10, 0), (-8, 2), (0, 2), (2, 4), (8, 4), (10, 2),
                   (2, 2), (2, 0), (10, -2), (8, -4), (2, -4), (2, -2),
                   (-8, -2), (-10, 0))
    
    screen.register_shape("plane", plane_shape)
# plane=turtle.Turtle(shape="triangle")
create_plane_shape()
plane = turtle.RawTurtle(screen)
plane.shape("plane")
plane.color(plane_lives[0])
plane.shapesize(1,2)
plane.penup()
plane.goto(0,-250)


#Create the bad plane
def create_alien_shape(x,y):
    alien = turtle.RawTurtle(screen)
    alien.shape("plane")
    alien.color("red")
    alien.shapesize(1.5,2.5)
    alien.right(180)
    alien.penup()
    alien.goto(x,y)
    return alien
#Move the plane left and right
def plane_leftmovement():
    initial_pos=plane.xcor()
    initial_pos-=30
    if initial_pos <-230:
        initial_pos=-230
    plane.setx(initial_pos)

def plane_rightmovement():
    initial_pos=plane.xcor()
    initial_pos+=30
    if initial_pos >230:
        initial_pos=230
    plane.setx(initial_pos)
#Listen to the keyboard for plane movemnet
def plane_control():
    screen.listen()
    screen.onkey(plane_rightmovement,"Right")
    screen.onkey(plane_leftmovement,"Left")
    screen.onkey(fire_bullet,"space")
#Set the alient spaceship in the screen
x=-200
y=250
alien_list=[]
for _ in range(18):
    
    aliens=create_alien_shape(x,y)
    x+=50
    if x >200:
        y-=50
        x=-200
    alien_list.append(aliens)

#Alien hit by bullet
def alien_bulleted(bullet):
    bullet_x,bullet_y=bullet.pos()
    for index,alien in enumerate(alien_list):
        if abs(bullet_x-alien.xcor())<20 and abs(bullet_y-alien.ycor())<20:
            score_list.append(alien)
            alien_list.pop(index)
            alien.hideturtle()
            alien.clear()
            score_count()
            return True
            
#hero bulle move
def move_fire_bullet(bullet):
    if alien_bulleted(bullet):
            bullet.hideturtle()
            bullet.clear()
            return
    if bullet.ycor()<280:
        
        bullet.sety(bullet.ycor()+10)
        screen.onkey(None,"space")
        # screen.update()
        screen.ontimer(lambda: move_fire_bullet(bullet), 10)

        
        # turtle.time.sleep(0.01)
    else:
        bullet.hideturtle()

#Hero bulleted
def hero_bulleted():
    plane_x,plane_y=plane.pos()
    for index,a_bullet in enumerate(active_alien_bullet_list):
        # print(plane_x-a_bullet.xcor())
        if abs(plane_x-a_bullet.xcor())<20 and abs(plane_y-a_bullet.ycor())<20:
            a_bullet.hideturtle()
            active_alien_bullet_list.remove(a_bullet)
            
            return True
#Fire the bullet
def fire_bullet():
    
    screen.tracer(0)
    
    bullet=turtle.Turtle()
    bullet.penup()
    bullet.color("yellow")
    bullet.shapesize(0.5,0.5)
    bullet.left(90)
    bullet.setpos(plane.xcor(),plane.ycor()+10)
    screen.tracer(1)
    move_fire_bullet(bullet)
    # bullet_move=True
    # while bullet_move:
        
    #     if bullet.ycor()<screen.window_height()/2:
    #         bullet.sety(bullet.ycor()+10)
    #         screen.onkey(None,"space")

    #         if alien_bulleted(bullet):
    #             bullet.hideturtle()
    #             bullet.clear()
    #             bullet_move=False
    #         turtle.time.sleep(0.01)
    #     else:
    #         bullet_move=False
    # bullet.hideturtle()
#Move enemy_bullet
def move_alien_bullet(alien_bullet):
    if hero_bulleted():
        
        plane_lives.remove(plane_lives[0])
        lives_count()
        if plane_lives:
            plane.color(plane_lives[0])
        else:
            return
    if alien_bullet.ycor()>-280 and plane_lives:
            
            alien_bullet.sety(alien_bullet.ycor()-10)
            # screen.update()
            screen.ontimer(lambda: move_alien_bullet(alien_bullet), 10)
    else:
        alien_bullet.hideturtle()
        if alien_bullet in active_alien_bullet_list:
            active_alien_bullet_list.remove(alien_bullet)
#Enemy shoots
def alien_fire_bullet():
    screen.tracer(0)
    random_alien_shooter=random.choice(alien_list)
    
    alien_bullet=turtle.Turtle()
    alien_bullet.shapesize(1,1)
    alien_bullet.color("red")
    alien_bullet.penup()
    alien_bullet.right(90)
    alien_bullet.setpos(random_alien_shooter.xcor(),random_alien_shooter.ycor()-10)
    screen.tracer(1)
    active_alien_bullet_list.append(alien_bullet)
    move_alien_bullet(alien_bullet)
    # alien_bullet_is=True
    # while alien_bullet_is:
    #     if alien_bullet.ycor()>-250:
    #         screen.update()
    #         alien_bullet.sety(alien_bullet.ycor()-10)
    #     else:
    #         alien_bullet_is=False
   
    # alien_bullet.hideturtle()
#Score and lives
def score_count():
    score.clear()
    point=len(score_list)
    score.write(f"Score: {point}")

def lives_count():
    lives.clear()
    lives_no=len(plane_lives)
    lives.write(f"Lives: {lives_no}")

# game_on=True

# while game_on:
    
#     if not plane_lives:
#         game_on=False
#         game_lost()
    
#     alien_fire_bullet()
#     plane_control()
#     screen.update()
def game_on():
    if not plane_lives:
        
        game_lost()
    
    alien_fire_bullet()
    plane_control()
    screen.update()
    screen.ontimer(game_on, 100) 

game_on()



turtle.done()
    

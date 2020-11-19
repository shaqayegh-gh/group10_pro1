from graphics import *
from field import *

class Ball(Field):

    def __init__(self):
        self.ball_pos=(15.5*30,10.5*30)
        self.ball=Circle(Point(self.ball_pos[0],self.ball_pos[1]),10)
        self.ball.setFill(color="white")
        self.add_item(self.ball.draw(self.win))

    def move_ball(self,x,y):
        self.ball_pos[0]+=x
        self.ball_pos[1]+=y

    # reset ball position and bring it to the center of field after a goal
    def reset(self):
        self.ball_pos=(15.5*30,10.5*30)
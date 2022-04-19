# Bulls-Eye
# Luke Han
# lhhan

import math, random
from cmu_112_graphics import *

def appStarted(app):
    app.level = 0

def drawCircle (app, canvas, x, y , r, color):
    pass
# making the target for the arrow to hit
def makingTarget(app, canvas, width, height, r = 50):
    x0 = (app.width/2 + 50)
    x1 = (app.width/2 - 50)
    y0 = (app.height/2 - 50)
    y1 = (app.height/2 + 50)

    # creates the base outline for the target (hits this and get 0 point)
    canvas.create_rectangle(x0, x1, y0, y1,fill= "white", outline = "black")
    # creates the first outercircle, (1 point)
    canvas.create_oval(x0/1.235 - (r/3.5),y0 * 1.3 - (r/11), x1 * 1.27 + (r/11), 
                        y1/1.3 + (r/11), fill = "white", outline = "black")
    # creates the secondary circle(3 points)
    canvas.create_oval(x0/1.225 - (r/7), y0 * 1.05 - (r/11), x1 * 1.235 + (r/7), 
                        y0*1.15 + (r/11), fill = "black", outline = "black")
    # # creates the third circle (5 points)
    # canvas.create_oval(x0 - (r/5), y0 - (r/5), x1 + (r/5), y0 + (r/5),
    #                 fill = "blue", outline = "black")
    # # creates the fourth circle (7 points)
    # canvas.create_oval(x0 - (r/3), y0 - (r/3), x1 + (r/3), y0 + (r/3),
    #                 fill = "red", outline = "black")
    # # creates the innermost circle (9 points)
    # canvas.create_oval(x0 - (r/2), y0 - (r/2), x1 + (r/2), y0 + (r/2),
    #                 fill = "yellow", outline = "black")
    # # creates the bulls-Eye (10 points)
    # canvas.create_oval(x0 - (r/1.1), y0 - (r/1.1), x1 + (r/1.1), y0 + (r/1.1),
    #                 fill = "black", outline = "black")

# attempt to try and move the target
def keyPressed(app, event):
    if event.key in ['Right']:
        app.movement += 10
    elif event.key in ['Left']:
        app.movement -= 10

# creates the horizon for where all the other images will be based off from
def makingLandscape(canvas,x0,x1,y0,y1,height, width):
    canvas.create_line(x0, x1, height/2, fill='black', outline='black')

# atempt to create the Y for the tree
def createTrees(app,canvas,level,locationX, locationY):
    l1 = level//2
    l2 = level//5
    x1 = locationX - math.cos(math.pi/4)
    x2 = locationX + math.cos(math.pi/4)
    canvas.create_line(locationX, locationY, locationX, locationY + l1,
                        fill= "brown")
    canvas.create_line(locationX,locationY + l1, x1, locationY + l1 + l2,
                        fill = "green")
    canvas.create_line(locationX, locationY + l1, x2, locationY + l1 + l2,
                        fill = "green")

# recursively creates more Y's for branches
def makingTrees(app,canvas,level, locationX, locationY):
    if level > 5:
        return None
    if level == 0:
        locationX = random.randint(0,app.width)
        locationY = app.height/2
        newX = math.cos(math.pi/4)
        newY = math.sin(math.pi/4)
        createTrees(app,canvas, level + 1,locationX, locationY)
    else:
        newLocation1 = locationX - math.cos(math.pi/4)
        newLocation2 = locationX + math.cos(math.pi/4)
        createTrees(app,canvas, level + 1,newLocation1, locationY)
        createTrees(app,canvas, level + 1,newLocation2, locationY)

def redrawAll(app,canvas):
    makingTrees(app,canvas, app.level, app.width, app.height)
    makingTarget(app, canvas, app.width, app.height, r = 50)
runApp(width = 800 , height = 800)

# using class
class Arrow(object):
    def __init__(self, arrow):
        self.arrow = arrow
        self.score = {}
        self.totalScore = {}
        # trying to see which arrow that is fired (1-3)
        def getArrow(self):
            for arrow in range(3):
                if arrow == 1:
                    arrow1 = arrow
                    self.score[arrow1] = 0
                if arrow == 2:
                    arrow2 = arrow
                    self.score[arrow2] = 0
                else:
                    arrow3 = arrow
                    self.score[arrow3] = 0
        # getting the score for each arrow
        def getScore(self):
            arrow = 0
            while arrow < 3:
                if arrow == 0:
                    arrow1 = arrow
                    if arrow == "white":
                        self.score[arrow1] += 0
                    if arrow == "green":
                        self.score[arrow1] += 1
                    if arrow == "purple":
                        self.score[arrow1] += 3
                    if arrow == "blue":
                        self.score[arrow1] += 5
                    if arrow == "red":
                        self.score[arrow1] += 7
                    if arrow == "yellow":
                        self.score[arrow1] += 9
                    if arrow == "black":
                        self.score[arrow1] += 10
                if arrow == 1:
                    arrow2 = arrow
                    if arrow == "white":
                        self.score[arrow2] += 0
                    if arrow == "green":
                        self.score[arrow2] += 1
                    if arrow == "purple":
                        self.score[arrow2] += 3
                    if arrow == "blue":
                        self.score[arrow2] += 5
                    if arrow == "red":
                        self.score[arrow2] += 7
                    if arrow == "yellow":
                        self.score[arrow2] += 9
                    if arrow == "black":
                        self.score[arrow2] += 10
                if arrow == 2:
                    arrow3 = arrow
                    if arrow == "white":
                        self.score[arrow3] += 0
                    if arrow == "green":
                        self.score[arrow3] += 1
                    if arrow == "purple":
                        self.score[arrow3] += 3
                    if arrow == "blue":
                        self.score[arrow3] += 5
                    if arrow == "red":
                        self.score[arrow3] += 7
                    if arrow == "yellow":
                        self.score[arrow3] += 9
                    if arrow == "black":
                        self.score[arrow3] += 10
        # putting the players scores into a list
        # def playerScore(self):
        #     if player1:
        #         for keys in self.score:
        #             for vals in self.self[keys]:
        #                 self.playerScore[player1] += vals
        #     elif player2:
        #         for keys in self.score:
        #             for vals in self.self[keys]:
        #                 self.playerScore[player2] += vals


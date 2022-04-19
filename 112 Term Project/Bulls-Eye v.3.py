# Bulls-Eye
# Luke Han
# lhhan

import math, random, sys
from cmu_112_graphics import *


#####################################################
# Main Game
#####################################################
def appStarted(app):
    app.mode = 'startScreen'
    app.Current_Score = 0
    app.High_Score = 0
    # app.x0 = random.randint(0,app.width - 80)
    app.x0 = app.width/2 - 40
    app.x1 = app.x0 + 80
    app.y0 = (app.height / 2) - 80
    app.y1 = (app.height / 2)

    #Z Position: 
    #Y Position: 0 corresponds 
    app.origin = [app.width/2, app.height/2, 0] #(0,0,0)
    app.startingPosition = [app.width/2, app.height/2, app.height/2 - 50] # (0, 0, app.height/2-50)
    app.aimPosition = [app.width/2, app.height/2, 0]
    app.currentPosition = [app.width/2, app.height/2, app.height/2 - 50]
    app.initialVelocity = 150
    app.time = 0
    app.timerDelay = 2000




    # app.origin = (app.width/2, app.height/2) #(0,0,0)
    # app.startingPosition = (app.width/2, app.height - 50)
    # app.currentPosition = (app.width/2, app.height - 50)
    # app.initialVelocity = 5
    # app.arrowLocation = (0,0)
    
#####################################################
# Starting Screen
#####################################################
def startScreen_redrawAll(app,canvas,r = 50):
    canvas.create_text((app.width/2), 9*(app.height/10),
                       text = 'Press any key to start Game',
                       fill = 'black', font = 'Arial 45 bold')
    canvas.create_oval(app.width/4,app.height/4, 3*(app.width/4), 
                         3*(app.height/4), fill = "red", 
                         outline = "black", width = r/25)
    canvas.create_text((app.width/2, app.height/2 - 25), 
                        text = "Bulls-Eye", fill = "yellow", 
                        font ='Arial 45 bold')
    canvas.create_text((app.width/2, app.height/2 + 25),
                        text = "Master Your Aim", fill = "black",
                        font = 'Arial 36 bold')
    canvas.create_line((2*app.width/9), 2*app.height/9, 1*(app.width/3),
                        2.5*(app.height/8), fill = "black", width = r/10)
    canvas.create_line((6.9*app.width/10), 2.7*app.height/8, 4.1*app.width/5, 
                        2.2*app.height/9, fill = "black", width = r/10)
    canvas.create_line((7.1*app.width/10), 1.9*app.height/3, 4.3*(app.width/5),
                        3*(app.height/4), fill = "black", width = r/10)
    canvas.create_line((.6*app.width/4), 3*app.height/4, .875*app.width/3, 
                        1.9*app.height/3, fill = "black", width = r/10)
    canvas.create_line((1.7*app.width/9), 3.1*app.height/4, 1.9*app.width/9, 
                        2.1*app.height/3, fill = "black", width = r/10)
    canvas.create_line(1.9*app.width/9, 2.1*app.height/3, 1.1*app.width/9, 
                        2.15*app.height/3, fill = "black", width = r/10)
    canvas.create_line(4.1*app.width/5, 3.105*app.height/4, 5.6*app.width/7,
                        2.8*app.height/4, fill = "black", width = r/10)
    canvas.create_line(5.6*app.width/7,2.11*app.height/3,8*app.width/9,
                        2.15*app.height/3, fill = "black", width = r/10)
    canvas.create_polygon(1.75*app.width/9, 1.7*app.height/9, 1.9*app.width/9, 
                        2.3*app.height/9, 2.4*app.width/9, 1.9*app.height/9,
                        fill = "white", outline = "black", width = r/10)
    canvas.create_polygon(6.9*app.width/8, 1.9*app.height/9, 7* app.width/9, 
                        2.1*app.height/9, 8.3*app.width/10, 2.5*app.height/9, 
                        fill = "white", outline = "black", width = r/10)

def startScreen_keyPressed(app,event):
    app.mode = 'playArchery'

#####################################################
# Play Archery
#####################################################

def playArchery_redrawAll(app,canvas):
    canvas.create_line(0,(app.height/2) - 50,app.width,(app.height/2) -50, 
                        fill='black')
    playArchery_drawTarget(app,canvas,app.x0,app.y0,app.x1,app.y1,r = 75)
    canvas.create_text(8.5*app.width/10,45,text = "Press 'r' to restart game",
                        fill = "black",font= 'Arial 18 bold')
    canvas.create_text(1.7*(app.width/10), 25, 
                        text = "Arrows Remaining: F'{Arrows}",
                        fill = "black",font= 'Arial 18 bold')
    canvas.create_text(8.5*app.width/10,25,text ="Current Score: F'{Score}",
                        fill = "black",font= 'Arial 18 bold')
    playArchery_drawArrow(app,canvas)

def playArchery_drawTarget(app,canvas,x0,y0,x1,y1,r = 80):
    canvas.create_rectangle(app.x0, app.y0, app.x1, app.y1,
                            fill = "white", outline = "black")
    #creates white circle
    canvas.create_oval(app.x0 - r/80 + 2.3, app.y0 - r/30 + 2.3, 
                        app.x1 + r/80 - 2.3, app.y1 + r/30 - 2.3, 
                        fill = "white", outline = "black")
    # creates black circle
    canvas.create_oval(app.x0 + r/80 + 7, app.y0 - r/5 + 22, app.x1 + r/5 - 22, 
                        app.y1 + r/65 - 7, fill = "grey", outline = "black")
    # creates blue circle
    canvas.create_oval(app.x0 + r/70 + 13, app.y0 + r/5, app.x1 + r/70 - 15, 
                        app.y1 - r/5 +2, fill = "blue", outline = "black")
    #creates red circle
    canvas.create_oval(app.x0 + r/40 + 18, app.y0 -r/4 + 41, app.x1 + r/40 - 21, 
                        app.y1 - r/4, fill = "red", outline = "black")
    # creates yellow circle
    canvas.create_oval(app.x0 + r/25 + 23, app.y0 - r/3 + 53, app.x1 + r/25 -28, 
                        app.y1 + r/25 -27, fill = "yellow", outline = "black")
    # creates green circle
    canvas.create_oval(app.x0 + r/15 + 27, app.y0 - r/15 + 39, 
                        app.x1 - r/15 - 26, app.y1 + r/15 - 34, 
                        fill = "green", outline = 'black')
    # creates the bullseye center
    canvas.create_oval(app.x0 + r/5 + 28, app.y0 -r/5 + 55, app.x1 - r/5 - 27, 
                        app.y1 + r/5 - 50, fill = "black", outline = "black")
    #creates roads
    canvas.create_line(app.x0, app.y1 -50, app.width/2 - 100, app.height, 
                        fill = "black")
    canvas.create_line(app.x1, app.y1 -50, app.width/2 + 100, app.height, 
                        fill = "black")


def playArchery_timerFired(app):
    # currX, currY, currZ = app.currentPosition
    # print(currZ)
    while (app.currentPosition[2] > 0):
        print(app.currentPosition)
        app.time += 0.01
        playArchery_updatePosition(app)
    print(app.currentPosition)

def getAngleY(app):
    x0, y0, z0 = app.startingPosition
    x1, y1, z1 = app.origin
    x2, y2, z2 = app.aimPosition
    return math.atan((y2-y1)/(z1-z0))

def getAngleX(app):
    x0, y0, z0 = app.startingPosition
    x1, y1, z1 = app.origin
    x2, y2, z2 = app.aimPosition
    return math.atan((x2-x1)/(z1-z0))

def xposition(app):
    app.currentPosition[0] = (app.startingPosition[0] + 
                                app.initialVelocity * math.sin(getAngleX(app))*app.time)

def yposition(app):
    app.currentPosition[1] = (app.startingPosition[1] + 0.5*(9.8)*(app.time**2) - 
                                app.initialVelocity*math.sin(getAngleY(app))*app.time)

def zposition(app):
    app.currentPosition[2] = (app.startingPosition[2] - 
                                app.initialVelocity * math.cos(getAngleY(app))*app.time)
    # app.currentPosition[2] = (app.startingPosition[2] - 120 * app.time)

def playArchery_updatePosition(app):
    # print("HERE")
    print(app.currentPosition[2])
    zposition(app)
    yposition(app)
    xposition(app)

def playArchery_drawArrow(app,canvas):
    r = 10
    (cx,cy,cz) = app.currentPosition
    canvas.create_oval(cx - r, cz + cy - r, cx + r, cz + cy + r, fill = "black")

def playArchery_keyPressed(app, event):
    if event.key == "r":
        app.x0 = random.randint(0,app.width - 80)
        app.x1 = app.x0 + 80

def distance(x0, y0, x1, y1):
    return math.sqrt((y1-y0)**2+(x1-x0)**2)

def playArchery_projectileMotion(app, x0, y0, x1, y1):
    period = 2*distance(x0, y0, x1, y1)
    b = (2*math.pi)/period


def playArchery_mousePressed(app,event):
    app.arrowLocation = (event.x, event.y)
    





#####################################################
# Score Screen
#####################################################




runApp(width = 800 , height = 800)
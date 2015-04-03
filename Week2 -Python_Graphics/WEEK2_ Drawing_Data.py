from graphics import *
import random

# Read in and print out the data in the data file
file = open("data.txt",'r')
data = file.readlines()


# Draw in window
window = GraphWin("Visualisation", 1000, 800)
#setBackground(0,0,0)

#Background Boxes
Box1 = Rectangle(Point(0,0),Point(333,800)) #Right
Box2 = Rectangle(Point(666,0),Point(1000,800)) #Left
Box1.setOutline(color_rgb(0,0,0))
Box2.setOutline(color_rgb(0,0,0))
Box1.setFill(color_rgb(0,0,0))
Box2.setFill(color_rgb(0,0,0))
Box1.draw(window) 
Box2.draw(window)

#sets the Title to appear
textName1 = Text(Point(500,400),"Peacock Feather")
textName2 = Text(Point(500,450),"Confusion")
textName1.setFace('arial')
textName1.setStyle('bold')
textName2.setFace('arial')
textName2.setStyle('bold italic')
textName1.setSize(35)
textName2.setSize(35)
textName1.draw(window)
textName2.draw(window)

time.sleep(2.0) # delays time/draw for specified duration

#Removes the Title
textName1.undraw()
textName2.undraw()
time.sleep(1)

#--------THE CIRCLE SIZES ARE MADE FROM RETRIEVING THE DATA FILE NUMBERS--------

#Creates Black-Top-WhiteBox-Circles 
for percentNum in data:
    sphere1 = Circle(Point(500,400-float(percentNum)),float(percentNum))
    sphere1.setOutline(color_rgb(0,0,0))
    sphere1.draw(window)
    #time.sleep(0.1) # delays time/draw for specified duration between each circle
    
#sphere1B = sphere1.getCenter(),sphere1.getRadius()
#sphere1B.move(Point(100,100)   
     
    
#Creates Black-Bottom-WhiteBox-Circles
for percentNum in data:
    sphere2 = Circle(Point(500,400+float(percentNum)),float(percentNum))
    sphere2.setOutline(color_rgb(0,0,0))
    sphere2.draw(window)
    #time.sleep(0.1) # delays time/draw for specified amount between each circle     
    
#Creates White-Top-BlackBoxLEFT + White-Bottom-BlackBoxRight (Circles)
for percentNum in data:
    sphere3 = Circle(Point(166,400-float(percentNum)),float(percentNum))
    sphere5 = Circle(Point(832,400+float(percentNum)),float(percentNum))
    sphere3.setOutline(color_rgb(255,255,255))
    sphere5.setOutline(color_rgb(255,255,255))
    sphere3.draw(window)
    sphere5.draw(window)
    #time.sleep(0.1) # delays time/draw for specified amount between each circle
    
#Creates White-Bottom-BlackBoxLEFT + White-Top-BlackBoxRight (Circles)
for percentNum in data:
    sphere4 = Circle(Point(166,400+float(percentNum)),float(percentNum))
    sphere6 = Circle(Point(832,400-float(percentNum)),float(percentNum))
    sphere4.setOutline(color_rgb(255,255,255))
    sphere6.setOutline(color_rgb(255,255,255))
    sphere4.draw(window)
    sphere6.draw(window)
    #time.sleep(0.1) # delays time/draw for specified amount between each circle
    
#Will Create the other circles for image

#Creates Black-Top-WhiteBox-Circles 
    
for percentNum in data:
    sphere1B = Circle(Point(500,120+float(percentNum)),float(percentNum))
    sphere2B = Circle(Point(500,680-float(percentNum)),float(percentNum))
    sphere3B = Circle(Point(166,120+float(percentNum)),float(percentNum))
    sphere4B = Circle(Point(166,680-float(percentNum)),float(percentNum))
    sphere5B = Circle(Point(832,120+float(percentNum)),float(percentNum))
    sphere6B = Circle(Point(832,680-float(percentNum)),float(percentNum))
    sphere1B.setOutline(color_rgb(0,0,0))
    sphere2B.setOutline(color_rgb(0,0,0))
    sphere3B.setOutline(color_rgb(255,255,255))
    sphere4B.setOutline(color_rgb(255,255,255))
    sphere5B.setOutline(color_rgb(255,255,255))
    sphere6B.setOutline(color_rgb(255,255,255))
    sphere1B.draw(window)
    sphere2B.draw(window)
    sphere3B.draw(window)
    sphere4B.draw(window)
    sphere5B.draw(window)
    sphere6B.draw(window)
    #time.sleep(0.1) # delays time/draw for specified duration between each circle
    
for percentNum in data:
    sphere1C = Circle(Point(500,120-float(percentNum)),float(percentNum))
    sphere2C = Circle(Point(500,680+float(percentNum)),float(percentNum))
    sphere1C.setOutline(color_rgb(0,0,0))
    sphere2C.setOutline(color_rgb(0,0,0))
    sphere1C.draw(window)
    sphere2C.draw(window)
    #time.sleep(0.1) # delays time/draw for specified duration between each circle  

#leftBoxTOP/BOTTOM
for percentNum in data:    
    sphere3C = Circle(Point(166,120-float(percentNum)),float(percentNum))
    sphere5C = Circle(Point(166,680+float(percentNum)),float(percentNum))
    sphere3C.setOutline(color_rgb(255,255,255))
    sphere5C.setOutline(color_rgb(255,255,255))
    sphere3C.draw(window)
    sphere5C.draw(window)
    
#RightBoxTOP/BOTTOM    
for percentNum in data:    
    sphere4C = Circle(Point(832,120-float(percentNum)),float(percentNum))
    sphere6C = Circle(Point(832,680+float(percentNum)),float(percentNum))
    sphere4C.setOutline(color_rgb(255,255,255))
    sphere6C.setOutline(color_rgb(255,255,255))
    sphere4C.draw(window)
    sphere6C.draw(window)    
    
#Four corner circles 
for percentNum in data:
    sphereTL = Circle(Point(166,120),float(percentNum))
    sphereBL = Circle(Point(166,680),float(percentNum))
    sphereTR = Circle(Point(832,120),float(percentNum))
    sphereBR = Circle(Point(832,680),float(percentNum))
    sphereTL.setOutline(color_rgb(255,255,255))
    sphereBL.setOutline(color_rgb(255,255,255))
    sphereTR.setOutline(color_rgb(255,255,255))
    sphereBR.setOutline(color_rgb(255,255,255))
    sphereTL.draw(window) 
    sphereBL.draw(window)
    sphereTR.draw(window) 
    sphereBR.draw(window) 

# Mid Top/Bottom circles   
for percentNum in data:
    sphere1D = Circle(Point(500,133),float(percentNum))
    sphere2D = Circle(Point(500,680),float(percentNum))
    sphere1D.setOutline(color_rgb(0,0,0))
    sphere2D.setOutline(color_rgb(0,0,0))
    sphere1D.draw(window)
    sphere2D.draw(window)
    #time.sleep(0.1) # delays time/draw for specified duration between each circle

#The last 3 Mid X axis circles to finish       
for percentNum in data:
    sphere3E = Circle(Point(166,400),float(percentNum))
    sphere4E = Circle(Point(832,400),float(percentNum))
    sphere3E.setOutline(color_rgb(255,255,255))
    sphere4E.setOutline(color_rgb(255,255,255))
    sphere3E.draw(window) 
    sphere4E.draw(window)

for percentNum in data:
    sphere1E = Circle(Point(500,400),float(percentNum))
    sphere1E.setOutline(color_rgb(0,0,0))
    sphere1E.draw(window)  
    time.sleep(0.1)
        
    
#X co-ordinate line
#line = Line(Point(100,700),Point(700,100))
#line.setWidth(4)
#line.draw(window)

#Y co-ordinate line
#line = Line(Point(100,100),Point(700,100))
#line.setWidth(4)
#line.draw(window)

# When mouse is clicked, closes the window
window.getMouse()
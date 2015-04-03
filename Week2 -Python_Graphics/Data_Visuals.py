import pygame, time

    Initialise display for drawing
	pygame.display.init()

    
    file = open("DatNum.txt")
    DatNum = file.readlines()
    
    
    Set display size and get a canvas (surface) for drawing onto
	canvas = pygame.display.set_mode((320,240))

    #Load in an image from the resources folder
	#img = pygame.image.load("res/kitten.png")

    #"Blit" the image onto the canvas
	#canvas.blit(img,(110,80))

    Refresh the display
	pygame.display.update()

    Wait for 60 seconds and then close the display window
	time.sleep(5)
	pygame.display.quit()
    
    
    
    
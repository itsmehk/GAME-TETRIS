
import tkMessageBox
import random 
import pygame, sys
import time

colors = [
(0,   0,   225  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) 
]

  
def score(count, gameDisplay):
    font=pygame.font.SysFont("comicsansms", 20)
    scores = font.render("Score: "+str(count),1,(255,255,255))
    gameDisplay.blit(scores,(20,20))
def display_box(screen, message):
    		fontobject=pygame.font.SysFont('Arial', 18)
    		if len(message) != 0:
        		screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                	((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    			pygame.display.flip()


class Brick:
	def __init__(self, x, y, width, height,colors):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colors=colors[random.randrange(0,len(colors)-1)]
	def collision(self):
		if 285 - self.y == self.height :
			return True
		else:
			return False


	def update(self, yupdate):
		if self.collision()==False:
			self.y += yupdate
		else:
			self.y += 0
	def render(self, window):
			pygame.draw.rect(window,self.colors , (self.x, self.y, self.width, self.height))
	def rotate_blocks(self):
		x=self.height
		self.height=self.width
		self.width=x
	def move_left(self):
            self.x-=15
    	def move_right(self):
            self.x+=15
	
		
		
		
	
	def quit(self):
		pygame.display.update()
		pygame.mixer.music.stop()
		time.sleep(1)
		sys.exit()
	

		

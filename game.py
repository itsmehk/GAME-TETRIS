import pygame,sys,random,time
from Brick import *
pygame.init()
Display=pygame.display.set_mode((300,300))
pygame.display.set_caption('TETRIS')
yupdate = 5	
pygame.mixer.music.load('Original Tetris Theme Tetris Soundtrack Gameboy -[ mymp3download.net ].mp3')
pygame.mixer.music.play(11)  
clock = pygame.time.Clock()
gameExit=False
lst=[]
count=0
level=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



for y in range(len(level)):
	for x in range(len(level[y])):
		if (level[y][x] == 1):
			lst.append(Brick(x*15, y*15, 15, 15,[
(0,   0,   225  ),(255, 85,  85),(100, 200, 115),(120, 108, 230)]))


while not gameExit:
	
	flag=0
	x,y=0,0
	movex,movey=0,0
	brick = Brick(x,y,30,15,[(0,   0,   225  ),(255, 85,  85),(100, 200, 115),(120, 108, 230) ])
	
	while flag!=1:
	     key_actions = {
			'ESCAPE':	brick.quit,
			
		}
	     for event in pygame.event.get():
			
			if event.type==pygame.QUIT:
				brick.quit()
			if event.type==pygame.KEYDOWN:
			    for key in key_actions:
						if event.key == eval("pygame.K_"+key):
							key_actions[key]()
			    if event.key==pygame.K_LEFT:
                    		if(brick.width==30 and brick.height==15):
                        		if(brick.x!=0):
                            			if(level[brick.y/15+1][brick.x/15-1]!=1):
                                			brick.move_left()
                    		elif(brick.width==15 and brick.height==30):
                        		if(brick.x!=0):
                            			if(level[brick.y/15+1][brick.x/15-1]!=1 and level[brick.y/15+2][brick.x/15-1]!=1):
                                			brick.move_left()            
                	    elif event.key==pygame.K_RIGHT:
                    		if(brick.width==30 and brick.height==15):
                        		if(brick.x!=300-brick.width):
                            			if(level[brick.y/15+1][brick.x/15+2]!=1):
                                			brick.move_right()
                    	    	elif(brick.width==15 and brick.height==30):
                        		if(brick.x!=300-brick.width):
                            			if(level[brick.y/15+1][brick.x/15+1]!=1 and level[brick.y/15+2][brick.x/15+1]!=1):
                                			brick.move_right()
                	    if event.key==pygame.K_UP:
                    		if(brick.width==30 and brick.height==15):
                        		if(level[brick.y/15+1][brick.x/15]!=1 and level[brick.y/15+2][brick.x/15]!=1 and level[brick.y/15+1][brick.x/15+1]!=1):
                            			brick.rotate_blocks()
                    		elif(brick.width==15 and brick.height==30):
                        		if(level[brick.y/15+1][brick.x/15+1]!=1):
                            			brick.rotate_blocks()

	     
	 
	     Display.fill((0,0,0))
	     
	     for y in range(len(level)):
			for x in range(len(level[y])):
						 if brick.width!=15 and (level[brick.y/15+1][brick.x/15] == 1 or level[brick.y/15+1][brick.x/15 +1] == 1 or level[brick.y/15+1][brick.x/15 +2]==1):
							level[brick.y/15][brick.x/15]=1
							level[brick.y/15][brick.x/15 +1]=1
							level[brick.y/15][brick.x/15 +2]=1
							lst.append(Brick(brick.x,brick.y, 30, 15,[(255, 85,  85),(255,0,0) ]))
							flag=1
						 if(brick.width==15 and brick.height==30):
                    					if(level[brick.y/15+2][brick.x/15]==1):
                        					level[brick.y/15][brick.x/15]=1
                        					level[brick.y/15+1][brick.x/15]=1
                        					lst.append(Brick(brick.x,brick.y,15,30,[(0,   0,   225  ),(255, 85,  85),(100, 200, 115),(120, 108, 230),(255, 140, 50 ),(50,  120, 52 ),(146, 202,73 ),(150, 161, 218 ),(35,  35,  35) ]))
                       						flag=1
	     brick.update(yupdate)
	     brick.render(Display)

	     for bricks in lst: 
		bricks.render(Display)
	     
	     for y in range(len(level)):
			for x in range(len(level[y])):
				if (level[3][x]==1):
					display_box(Display,'GAMEOVER || Score : '+str(h))
					pygame.mixer.music.stop()
					time.sleep(1)
					sys.exit()
	     
	     score(count, Display)
	     h=count     
	     pygame.draw.rect(Display,(0,0,225),(0,285,300,15))
	     pygame.display.flip()
	     clock.tick(30)
	count+=1
	
	    

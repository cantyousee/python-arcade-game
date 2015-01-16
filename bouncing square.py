import pygame

# Define some colors as global constants
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED   = ( 255,   0,   0)
GREEN = (   0, 255,   0)
BLUE  = (   0,   0, 255)

# Initialize the game engine
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Danny's Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop ---
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # if user clicked close
			done = True # Flag that we are done so exit this loop
			
	# Set the screen background
	screen.fill(BLACK)
	
	# Draw the rectangle
	pygame.draw.rect(screen,BLUE, [rect_x, rect_y, 50, 50])
	pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
	
	# Move the rectangle starting point
	rect_x += rect_change_x
	rect_y += rect_change_y

	# Bounce the rectangle if needed
	if rect_y > 450: # 500(screen height) - 50(rectangle height)
		rect_change_y = rect_change_y * -1
	if rect_x > 650: # 700(screen width)  - 50(rectangle width)
		rect_change_x = rect_change_x * -1
	if rect_y < 0: 
		rect_change_y = rect_change_y * -1
	if rect_x < 0:
		rect_change_x = rect_change_x * -1
		
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	# --- Limit to 60 frames per second
	clock.tick(60)
	
# Close the window and quit.
# If you forget this line, the program will "hang"
# on exit if running from IDLE.
pygame.quit()

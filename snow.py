# Import libraries of functions
import pygame
import math
import random

# Initialize the game engine
pygame.init()

# Define colors
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED   = ( 255,   0,   0)
GREEN = (   0, 255,   0)
BLUE  = (   0,   0, 255)

# Set the width and height of the screen
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create an empty array
snow_list = []

for i in range(50):
	x = random.randrange(0, 400)
	y = random.randrange(0, 400)
	snow_list.append([x, y])
	
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop ---
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # if user clicked close
			done = True # Flag that we are done so exit this loop
			
	# Set the screen background
	screen.fill(BLACK)
		
	for i in range(len(snow_list)):
		
		# Draw the snowflake
		pygame.draw.circle(screen, WHITE, snow_list[i], 2)
	
		# Move the snowflake down one pixel
		snow_list[i][1] += 5
	
		# If the snowflake has moved off the bottom of the screen...
		if snow_list[i][1] > 400:
			# Reset it just above the top
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# Give it a new x position
			x = random.randrange(0, 400)
			snow_list[i][0] = x
		
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	# --- Limit to 20 frames per second
	clock.tick(60)
	
# Close the window and quit.
# If you forget this line, the program will "hang"
# on exit if running from IDLE.
pygame.quit()

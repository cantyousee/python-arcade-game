import pygame

# Define some colors as global constants
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
RED   = ( 255,   0,   0)
GREEN = (   0, 255,   0)
BLUE  = (   0,   0, 255)

def draw_snowman(screen, x, y):
	#Draw a circle for the head
	pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
	#Draw the middle snowman circle
	pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
	#Draw the bottom snowman circle
	pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])

def draw_stick_figure(screen, x, y):
	# Head
	pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)
	
	# Legs
	pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 2)
	pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)
	
	# Body
	pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
	
	# Arms
	pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
	pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)
	
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

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop ---
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # if user clicked close
			done = True # Flag that we are done so exit this loop
	# --- End event processing ---
	
	# --- Game logic ---
	pos = pygame.mouse.get_pos()
	x = pos[0]
	y = pos[1]
	# --- End game logic ---
	
	# --- Drawing code ---
	screen.fill(WHITE) # Set the screen background
	
	# Call draw stick figure function
	draw_stick_figure(screen, x, y)	
	
	# --- End drawing code ---
	
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	# --- Limit to 60 frames per second
	clock.tick(60)
	
# Close the window and quit.
# If you forget this line, the program will "hang"
# on exit if running from IDLE.
pygame.quit()

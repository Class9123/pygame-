
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the resolution
resolution = (800, 600)

# Create a screen with full screen mode and scaling
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN | pygame.SCALED)

# Set the color
bg_color = (255,0,0)  # Black background

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Fill the screen with the background color
    screen.fill(bg_color)
    
    # Update the display
    pygame.display.flip()

import pygame
import time
import os

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Ensure the 'pygame_pngs' directory exists
output_dir = 'pygame_pngs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Absolute path for the output file
output_file = os.path.join(output_dir, 'game_output.png')

# Check if the directory is writable
if not os.access(output_dir, os.W_OK):
    raise PermissionError(f"Cannot write to directory: {output_dir}")

# Function to save the image with retries
def save_image_with_retries(screen, output_file, retries=5, delay=0.05):
    for _ in range(retries):
        try:
            pygame.image.save(screen, output_file)
            return True  # Image saved successfully
        except pygame.error as e:
            print(f"Error saving image: {e}")
            time.sleep(delay)
    print("Failed to save image after several retries")
    return False  # Image saving failed

# Circle parameters
circle_radius = 50
circle_color = (255, 0, 0)
circle_x = 0

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Draw a red circle
    pygame.draw.circle(screen, circle_color, (circle_x, height // 2), circle_radius)
    circle_x = (circle_x + 5) % width  # Move the circle horizontally

    # Update the display
    pygame.display.flip()

    # Save the current frame to a file with retries
    if not save_image_with_retries(screen, output_file):
        # Handle failure (e.g., retry later or exit gracefully)
        pass

    # Small delay to control the frame rate
    time.sleep(0.5)

pygame.quit()

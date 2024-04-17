import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 50, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
CAR_SPEED = 5
OBSTACLE_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE_POSITION = (10, 10)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Clock
clock = pygame.time.Clock()

# Player car
player_car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
player_car_img.fill((255, 0, 0))  # Red car

# Obstacles
obstacles = []

# Score
score = 0

# Function to create a new obstacle
def create_obstacle():
    x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT
    obstacles.append(pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_car_img.move_ip(-CAR_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        player_car_img.move_ip(CAR_SPEED, 0)

    # Check for collisions with obstacles
    player_car_rect = pygame.Rect(player_car_img.get_rect())
    for obstacle in obstacles:
        if player_car_rect.colliderect(obstacle):
            running = False  # Game over

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player car
    screen.blit(player_car_img, (player_car_rect.x, player_car_rect.y))

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.move_ip(0, OBSTACLE_SPEED)
        pygame.draw.rect(screen, WHITE, obstacle)

    # Remove obstacles that have gone off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

    # Display score
    score_text = pygame.font.SysFont(None, 36).render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, SCORE_POSITION)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

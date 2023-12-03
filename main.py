import os
import sys
import pygame
import importlib

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Collection")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game directory and icon size
GAMES_DIR = "games"
ICON_SIZE = (100, 100)

def load_game_modules():
    """
    Dynamically load game modules from the games directory.
    Returns a list of tuples (module, icon, title).
    """
    games = []
    for game in os.listdir(GAMES_DIR):
        if os.path.isdir(os.path.join(GAMES_DIR, game)):
            # Import the game module
            module = importlib.import_module(f"{GAMES_DIR}.{game}.{game}")

            # Load the icon and title
            icon_path = os.path.join(GAMES_DIR, game, "icon.png")
            title = getattr(module, "TITLE", "Untitled Game")
            icon = pygame.image.load(icon_path)
            icon = pygame.transform.scale(icon, ICON_SIZE)

            games.append((module, icon, title))
    return games

def main():
    # Load game modules
    games = load_game_modules()

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Display game icons and titles
        for i, (module, icon, title) in enumerate(games):
            x = 50 + (ICON_SIZE[0] + 50) * (i % 5)
            y = 50 + (ICON_SIZE[1] + 50) * (i // 5)
            screen.blit(icon, (x, y))
            font = pygame.font.Font(None, 24)
            text = font.render(title, True, BLACK)
            screen.blit(text, (x, y + ICON_SIZE[1] + 5))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

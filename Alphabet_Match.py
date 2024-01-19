import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 800, 600
CARD_SIZE = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2  # Pairs of cards
random.shuffle(cards)
flipped = []  # List to store flipped cards
matched = []  # List to store matched cards
game_over = False

# Initialize Pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle Game")
clock = pygame.time.Clock()

def draw_card(x, y, card_value, is_flipped):
    font = pygame.font.Font(None, 36)
    card_text = font.render(card_value, True, BLACK)
    card_rect = card_text.get_rect(center=(x, y))

    pygame.draw.rect(screen, WHITE if is_flipped else BLACK, (x - CARD_SIZE/2, y - CARD_SIZE/2, CARD_SIZE, CARD_SIZE))
    screen.blit(card_text, card_rect)

def draw_game_over():
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over!", True, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, game_over_rect)

def main():
    global flipped, matched, game_over

    while not game_over:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(flipped) < 2:
                    x, y = pygame.mouse.get_pos()
                    index = y // CARD_SIZE * (WIDTH // CARD_SIZE) + x // CARD_SIZE

                    if index not in flipped and index not in matched:
                        flipped.append(index)

        # Draw cards
        for i, card in enumerate(cards):
            row, col = divmod(i, WIDTH // CARD_SIZE)
            x, y = col * CARD_SIZE + CARD_SIZE / 2, row * CARD_SIZE + CARD_SIZE / 2

            if i in flipped or i in matched:
                draw_card(x, y, card, True)
            else:
                draw_card(x, y, "", False)

        # Check for matches
        if len(flipped) == 2:
            card1, card2 = cards[flipped[0]], cards[flipped[1]]
            if card1 == card2:
                matched.extend(flipped)
            flipped = []

        # Check for game over
        if len(matched) == len(cards):
            game_over = True

        pygame.display.flip()
        clock.tick(FPS)

    # Display Game Over text
    draw_game_over()
    pygame.display.flip()

    # Allow the Game Over text to be displayed for a few seconds before exiting
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

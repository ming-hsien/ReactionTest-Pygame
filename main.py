import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction testing")

start_img = pygame.image.load("no_button.png")
target_img = pygame.image.load("yes_button.png")

start_img = pygame.transform.scale(start_img, (400, 400))
target_img = pygame.transform.scale(target_img, (400, 400))

image_rect = start_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

wait_time = random.uniform(2, 5)
change_time = time.time() + wait_time

def main():
    game_running = True
    show_target = False
    start_time = None
    reaction_time = None

    while game_running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and show_target:
                reaction_time = round(time.time() - start_time, 3) 
        
        if not show_target and time.time() >= change_time:
            show_target = True
            start_time = time.time()
        
        if show_target:
            screen.blit(target_img, image_rect)
        else:
            screen.blit(start_img, image_rect)

        if reaction_time is not None:
            font = pygame.font.Font(None, 50)
            text = font.render(f"Reaction Time:{reaction_time}sec", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - 200, HEIGHT - 100))

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
import sys
import pygame
from .constants import *


def return_score_board(clock, screen, background_image, font):

    nr1_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    nr1_text = font.render('Play (or B)', True, (0,255,0))
    nr1_text_rect = nr1_text.get_rect(center=nr1_rect.center)
    
    scoreboard = True

    while scoreboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    scoreboard = False
                    return menu_loop(screen, background_image, font)
        
        screen.blit(background_image, (0,0)),
        pygame.draw.rect(screen, (255,255,255), nr1_rect, 0),
        screen.blit(nr1_text, nr1_text_rect)

        arrow_width = 20
        arrow_height = 20
        gap = 150
        arrow_x = nr1_rect.left - gap  # a bit to the right of the rect
        arrow_y = nr1_rect.centery

        arrow_points = [
            (arrow_x, arrow_y),  # Tip of the arrow
            (arrow_x + arrow_width, arrow_y - arrow_height // 2),  # Top back
            (arrow_x + arrow_width, arrow_y + arrow_height // 2)   # Bottom back
        ]

        pygame.draw.polygon(screen, (0, 255, 0), arrow_points)

        pygame.display.flip() 
        clock.tick(60) / 1000

    return nr1_rect
    

def update_score_board():
    # Datetime
    # Name
    # In top 10?
    # Sort in top 10
    pass

def menu_loop(level, clock, screen, background_image, font):
    # TODO: Use update_score_board
    # update_score_board(score, name)
    
    play_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    play_text = font.render('Play (or B)', True, (0,255,0))
    play_text_rect = play_text.get_rect(center=play_rect.center)

    score_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5*2, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    score_text = font.render('Score Board', True, (0,255,0))
    score_text_rect = score_text.get_rect(center=score_rect.center)

    settings_rect = pygame.Rect(
            (SCREEN_WIDTH/4, SCREEN_HEIGHT/4.5*3, 
             SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6),
            )
    level_text = font.render('Medium', True, (0,255,0))
    level_text_rect = level_text.get_rect(center=settings_rect.center)

    menu_running = True

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                print("Clicked")
                state = "game"
                menu_running = False
                return state
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(pygame.mouse.get_pos()):
                    state = "game"
                    menu_running = False
                    return state, level
                if score_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_running = False
                    return return_score_board(clock, screen, background_image, font)
                if settings_rect.collidepoint(pygame.mouse.get_pos()):
                    level += 1
                    if level > 3:
                        level = 1
                    if level == 1:
                        level_text = font.render('Easy', True, (0,255,0))
                    elif level == 2:
                        level_text = font.render('Medium', True, (0,255,0))
                    elif level == 3:
                        level_text = font.render('Hard', True, (0,255,0))
                    
            
            # TODO: Add menu browsing logic

        screen.fill((0,0,0))
        screen.blit(background_image, (0,0))
        pygame.draw.rect(screen, (255,255,255), play_rect, 2)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (255,255,255), score_rect, 2)
        screen.blit(score_text, score_text_rect)
        pygame.draw.rect(screen, (255,255,255), settings_rect, 2)
        screen.blit(level_text, level_text_rect)
        pygame.display.update()
        clock.tick(60) / 1000
import pygame

pygame.mixer.init()

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()
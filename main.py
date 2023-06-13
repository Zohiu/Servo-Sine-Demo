import pygame
import math
import random

pygame.init()

pygame.display.set_caption('Quick Start')
WIDTH, HEIGHT = 1000, 600
window_surface = pygame.display.set_mode((WIDTH + 1, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

clock = pygame.time.Clock()
delta = clock.tick()

length = 1000  # In time, milliseconds.
max_amplitude = 255

hertz = 5
y_offset = -max_amplitude
amplitude = 100


def gety(x):
    return (math.sin((2 * math.pi * (x / length)) * hertz) * current_amplitude) + y_offset


font = pygame.font.Font("font.otf", 24)

is_running = True

while is_running:
    window_surface.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    y_offset += delta * 0.05
    if y_offset > max_amplitude:
        y_offset = -max_amplitude
        hertz = 5
        amplitude = 100

    hertz += delta * 0.0025
    amplitude += delta * 0.0075

    # Calculate current amplitude based on maximum and offset
    current_amplitude = max(0, min(max_amplitude, max_amplitude - y_offset - (max_amplitude - ((amplitude - max(-min(0, max_amplitude + (y_offset - amplitude)), max(0, -1 * (max_amplitude - (y_offset + amplitude))))) + y_offset))))

    # Draw grid lines at ever 100ms
    for x in [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
        pygame.draw.line(window_surface, (0, 50, 0), (x, HEIGHT / 2 - max_amplitude),
                         (x, HEIGHT - (HEIGHT / 2 - max_amplitude)))


    # Middle line
    pygame.draw.line(window_surface, (255, 0, 0), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))

    # Amplitude lines
    pygame.draw.line(window_surface, (0, 0, 255), (0, HEIGHT / 2 + current_amplitude + y_offset), (WIDTH, HEIGHT / 2 + current_amplitude + y_offset))
    pygame.draw.line(window_surface, (0, 0, 255), (0, HEIGHT / 2 - current_amplitude + y_offset), (WIDTH, HEIGHT / 2 - current_amplitude + y_offset))

    # Max amplitude lines
    pygame.draw.line(window_surface, (255, 0, 255), (0, HEIGHT / 2 + max_amplitude), (WIDTH, HEIGHT / 2 + max_amplitude))
    pygame.draw.line(window_surface, (255, 0, 255), (0, HEIGHT / 2 - max_amplitude), (WIDTH, HEIGHT / 2 - max_amplitude))

    points = [(0, HEIGHT/2 + y_offset)]

    # Calculate all sine wave points based on sample length
    for x in range(length):
        points.append((x, gety(x) + HEIGHT / 2))

    points.append((WIDTH + 1, points[-1][1]))
    points.append((WIDTH + 1, HEIGHT / 2 + y_offset))
    # hertz += delta * 0.001

    # Draw sine wave
    pygame.draw.polygon(window_surface, (255, 255, 255), points, 1)

    # Text render
    text = font.render(f"{round(hertz)} Hz | {round(max_amplitude)} max amplitude | {round(amplitude)} input amp. | {round(current_amplitude)} actual amp. | {round(y_offset)} y offset", True, (0, 0, 255))
    window_surface.blit(text, (10, 5))

    delta = clock.tick(60)
    text = font.render(f"Sinewave demo | made by Zohiu | Goal: Work with a servo; Stay in bounds | {round(1000 / delta)} fps", True, (0, 0, 255))
    window_surface.blit(text, (10, HEIGHT - 40))

    pygame.display.update()
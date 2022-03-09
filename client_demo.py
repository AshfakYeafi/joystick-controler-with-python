import pygame

pygame.init()


def main():
    pygame.display.set_caption('JoyStick Example')
    surface = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    font = pygame.font.Font(None, 20)
    linesize = font.get_linesize()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joy in joysticks:
        joy.init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((0, 0, 0))
        position = [10, 10]

        for joy in joysticks:
            image = font.render('name: ' + joy.get_name(), 1, (0, 200, 0))
            surface.blit(image, position)
            position[1] += linesize

            image = font.render('button count: {0}'.format(joy.get_numbuttons()), 1, (0, 200, 0))
            surface.blit(image, position)
            position[1] += linesize

            for i in range(joy.get_numbuttons()):
                if joy.get_button(i):
                    image = font.render('{0}: push'.format(i), 1, (0, 200, 0))
                    surface.blit(image, position)
                    position[1] += linesize

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()


main()
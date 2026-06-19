import pygame

print('set up start')
pygame.init()
window = pygame.display.set_mode(size=(600, 400))
print('Set up end')

print('loop start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

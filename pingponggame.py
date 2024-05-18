import pygame

pygame.init()
WIDTH,HEIGHT= 700,500
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PING PONG")

PADDLE1= pygame.Rect(0,200,40,130)
PADDLE2= pygame.Rect(660,200,40,130)



WHITE=(255,255,255)
RED=(255,0,0)

FPS= 60

def draw_screen():
    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN,RED,PADDLE1)
    pygame.draw.rect(SCREEN,RED,PADDLE2)
    pygame.display.update()



def main():
    
    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            PADDLE1.move_ip(0,-1)
        if keys_pressed[pygame.K_s]:
            PADDLE1.move_ip(0,1)

        if keys_pressed[pygame.K_UP]:
            PADDLE2.move_ip(0,-1)
        if keys_pressed[pygame.K_DOWN]:
            PADDLE2.move_ip(0,1)
        draw_screen()

    pygame.quit()


if __name__=="__main__":
    main()
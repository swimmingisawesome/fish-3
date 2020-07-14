import pygame
import random
pygame.init()


screen_info = pygame.display.Info()
print(screen_info)

w = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = (0, 127, 255)
w.fill(color)


fish_image = pygame.image.load('fish (1).png')
fish_image = pygame.transform.smoothscale(fish_image,(80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (400, 300)


speed = pygame.math.Vector2(10, 0)
rotation = random.randint (0, 360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, int(rotation))
def move_fish():
  global fish_image
  fish_rect.move_ip(speed)
  
  if fish_rect.top < 0 or fish_rect.bottom > 600:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1])    
       
  if fish_rect.right < 0 or fish_rect.left > 800:
    speed[0] *= -1
    fish_image = pygame.transform.flip(fish_image, True, False)
    fish_rect.move_ip(speed[0], 0)                                                     

def main():
  while True:
    c.tick(60)
    move_fish()
    w.fill(color)
    w.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__=='__main__':
  main()
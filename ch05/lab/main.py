#import pygame

coords = []
n=None
count=None
max_so_far=None



def foo():
  count = 0      
  upper_limit= 10
  iters= {}
  start= 2
  max_so_far=count
  for n in range(start, upper_limit):
    while n != 1:
      if n % 2 == 0:
        n = n // 2
        count += 1
      else:
        n = n * 3 + 1
        count += 1     
      if count> max_so_far:
        max_so_far=count
      iters.update({n : count})
  print(iters)
  print("Max num of iterations: ", max_so_far)
          
  # scale=5
  # pygamae.init()
  # display = pygame.display.set_mode()
  # display.set_colorkey("white")
  # pygame.draw.lines(display, "black", False, {iters})
  # new_display = pygame.transform.flip(display, False, True)
  # display.blit(new_display, (0, 0))
  # font_name= None
  # font = pygame.font.init(font_name, 10)
  # msg = font.render(f"Max # of iterations: {max_so_far}", False, "white")
  # display.blit(msg, (10, 10))


foo()

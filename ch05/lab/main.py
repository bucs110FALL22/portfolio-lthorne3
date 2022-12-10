import pygame




def foo():     
  upper_limit= 20
  iters= {
    1:0
  }
  start= 2
  max_so_far=0
  for n in range(start, upper_limit+1):
    i=n
    count= 0
    while i != 1:
      if i % 2 == 0:
        i = i // 2
        count += 1
      else:
        i = i * 3 + 1
        count += 1 
    if count > max_so_far:
      max_so_far=count
    iters.update({n : count})


  print(iters)
  print("Max num of iterations: ", max_so_far)
          

  scale=10
  for j in iters:
    iters[j]= iters[j]*scale
    j=j*scale
  iters[n]= count
  coords= list(iters.items())
  pygame.init()
  display = pygame.display.set_mode()
  display.set_colorkey("white")
  new_display = pygame.transform.flip(display, False, True)
  display.blit(new_display, (0,0))
  pygame.draw.lines(display, "white", False, coords)
  font_name= None
  pygame.font.init()
  font= pygame.font.Font(font_name, 20)
  msg = font.render(f"Max # of iterations: {max_so_far}", False, "white")
  display.blit(msg, (0,200))
  pygame.display.flip()
  pygame.time.wait(2000)
 



foo()

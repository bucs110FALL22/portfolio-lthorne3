import pygame

coords = []
n=None
count=None
max_so_far=None
upper_limit=200


def foo(n):
    count = 0
    max_so_far = count 
    while n != 1:
        coords.append([n, count])
        print(n, end=', ')
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1

      
    print(n, end='. ')
    print("count =", count)
    if count > max_so_far:
        max_so_far = count
    for i in [coords]:
      if coords[i]>coords[i+1]:
        max_val= coords[i+1]
    iters = {
        n: count
    }
    scale=5
    display = pygame.display.set_mode()
    display.set_colorkey("white")
    pygame.draw.lines(display, "black", False, coords*5)
    new_display = pygame.transform.flip(display, False, True)
    display.blit(new_display, (0, 0))
    font = pygame.font.Font(None, 10)
    msg = font.render("msg", False, "white")
    display.blit(msg, (10, 10))


foo(10)

from Rectangle import Rectangle
from Surface import Surface

def main():
  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.width, r.height) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  r.zeroes()
  assert((r.x, r.y, r.width, r.height) == (0,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  r.zeroes()
  assert((r.x, r.y, r.width, r.height) == (1,0,1,1))
  r = Rectangle(1, 1, -1, 1)
  r.zeroes()
  assert((r.x, r.y, r.width, r.height) == (1,1,0,1))
  r = Rectangle(1, 1, 1, -1)
  r.zeroes()
  assert((r.x, r.y, r.width, r.height) == (1,1,1,0))

  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.width, s.rect.height) ==   (10,10,10,10))
  srect = s.getRect()
  assert((srect.x,  s.getRect().y, srect.width,  srect.height) == (10,10,10,10))
  assert s.image 
  print("Test Complete!")

main()



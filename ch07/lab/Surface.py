from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, width, height):
    '''
    __init__ sets parameters for the surface class
    self: (Surface) the surface object
    filename: (str) string containing file image name
    x: (int) the x coordinate of the top left corner of rect
    y: (int) the y coordinate of the top left corner of rect
    w: (int) the width of rect
    h: (int) the height of rect
    return: none
    '''
    
    self.rect= Rectangle(x, y, width, height)
    self.image= filename
    self.x=x 
    self.y=y
    self.width=width
    self.height=height

  def getRect(self):
    '''
    getRect() returns a rectangle object
    self: (Surface) the surface object
    return: (Rectangle) rectangle object in self.rect
    '''
    return self.rect
    
    
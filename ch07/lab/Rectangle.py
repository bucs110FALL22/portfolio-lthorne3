class Rectangle:
  def __init__(self, x, y, width, height):
    '''
    __init__ sets parameters for the surface class
    self: (Rectangle) the rectangle object
    x: (int) the x coordinate of the top left corner of rect
    y: (int) the y coordinate of the top left corner of rect
    w: (int) the width of rect
    h: (int) the height of rect
    return: none
    '''
    self.x=x
    self.y=y
    self.width=width
    self.height=height
    
  def zeroes(self):
    '''
    if any of the parameters are <0, then they will equal 0
    self: (Rectangle) the rectangle object
    return: none
    '''
    if self.x < 0:
      self.x=0
    if self.y<0:
      self.y=0
    if self.width<0:
      self.width=0
    if self.height<0:
      self.height=0

  def __str__(self):
    '''
    creates a string of rectangle information called return_str
    self: (Rectangle) the rectangle object
    return: (string) return_str
    '''
    return_str= f"(x: {self.x},y: {self.y}) width: {self.width}, height: {self.height}."
    return return_str

    
      
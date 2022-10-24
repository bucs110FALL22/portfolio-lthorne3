class Goomba:
  def __init__(self):
    self.moving_forward=True
    self.num_of_lives=1
    self.is_alive=True

class Tube:
  def __init__(self):
    self.color= "green"
    self.height= 30 #px
    self.mario_on_top=True

class Mystery:
  def __init__(self):
    self.is_hit=False
    self.coins_released=1
    self.shape="square"
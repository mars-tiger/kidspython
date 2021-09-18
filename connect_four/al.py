import turtle

def draw_piece(row, col, color):
  pass
  
def draw(x, y):
  global board, rb, winner
  pass
  
  
def check_winner():
  pass

def draw_board():
  pass


radius = 23
gap = 2
square_size = 2 * (radius + gap)
offset_x = -180
offset_y = 100

board = [
  [None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None],
]

winner = ""

rb = "r"

t = turtle.Turtle()
t.ht()
t.speed(200)

draw_board()

wn = turtle.Screen()
wn.onclick(draw)
wn.mainloop()

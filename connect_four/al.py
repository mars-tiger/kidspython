import turtle

def draw_piece(row, col, color):
  pass
  
def draw(x, y):
  global board, rb, winner
  pass
  
  
def check_winner():
  pass

def draw_board(x, y, size, x2, y2):
  t.up()
  t.goto(x, y)
  t.down()
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.up()
  t.goto(x2, y2)
  s = 25
  for i in range(5):
    for i in range(7):
      t.circle(23)
      t.up()
      t.forward(25)
      t.down()
    t.up()
    t.goto(x2, y2 - s)
    s = s + 25
    t.down()


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

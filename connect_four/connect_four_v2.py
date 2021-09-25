import turtle
  
def draw_piece(row, col, color):
  x = offset_x + 25 + col * 2 * (radius + gap)
  y = offset_y - 25 - row * 2 * (radius + gap)
  t.up()
  t.home()
  t.goto(x,y)
  t.down()
  t.color(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  
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
draw_piece(0, 0, "blue")
draw_piece(0, 1, "red")
draw_piece(1, 0, "green")

t.up()
t.home()
t.down()


wn = turtle.Screen()
wn.onclick(draw)
wn.mainloop()

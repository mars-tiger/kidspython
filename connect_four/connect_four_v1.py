import turtle

def draw_circle():
  t.color("green")
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  
def draw_piece(row, col, color):
  x = col  + offset_x + 25
  y = -row  + offset_y - 25
  t.up()
  t.home()
  t.goto(x,y)
  t.down()
  t.circle(radius)
  
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
draw_piece(0, 0, "green")

t.up()
t.home()
t.down()
draw_circle()

wn = turtle.Screen()
wn.onclick(draw)
wn.mainloop()

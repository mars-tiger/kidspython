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
  col = int((x - offset_x) // square_size)
 
  row = None
  for r in range(5, -1, -1):
    if not board[r][col]:
      row = r
      break
 
  if row is None or winner:
    return
 
  draw_piece(row, col, rb)
  board[row][col] = rb
 
  if rb == "red":
    rb = "blue"
  else:
    rb = "red"
 
  winner = check_winner()
 
def check_winner():
  for row in range(6):
    for col in range(4):
      if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col]:
        return board[row][col]
  return ""

def draw_board():
 # TODO: use a for loop to simplify the code
 t.color("purple")
 t.begin_fill()
 t.up()
 t.goto(190, -180)
 t.down()
 t.left(90)
 t.forward(310)
 t.left(90)
 t.forward(380)
 t.left(90)
 t.forward(310)
 t.left(90)
 t.forward(380)
 t.end_fill()
                 
 for row in range(6):
   for col in range(7):
     draw_piece(row,col,"white")
   
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

rb = "red"

t = turtle.Turtle()
t.ht()
t.speed(200)


def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return t.up()
        t.goto(100, -100)                              
        t.write("ava")

        return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]

    if all([board[row][col] for row in range(len(board)) for col in range(len(board[0]))]):
        return "nobody"

    return ""


draw_board()
#draw_piece(0, 0, "blue")
#draw_piece(0, 1, "red")
#draw_piece(3, 5, "purple")

t.up()
t.home()
t.down()


wn = turtle.Screen()
wn.onclick(draw)
wn.mainloop()

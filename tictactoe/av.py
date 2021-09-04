


import turtle

import turtle
def draw_star(row, col):
  x = col * size / 3 + offset_x + size / 27
  y = -row * size / 3 + offset_y - size / 6
  t.up()
  t.goto(x, y)
  t.down()
  t.forward(80)
  t.backward(80/2)
  t.left(60)
  t.up()
  t.forward(80/2)
  t.down()
  t.right(180)
  t.forward(80)
  t.left(180)
  t.forward(80/2)
  t.left(60)
  t.up()
  t.backward(80/2)
  t.down()
  t.forward(80)


def draw_s(row, col):
  x = col * size / 3 + offset_x + 25
  y = -row * size / 3 + offset_y - 25
  t.up()
  t.home()
  t.goto(x,y)
  t.down()
  for i in range(4):
    t.forward(50)
    t.right(90)




def draw(x, y):
    global board, xo, winner
    col = int((x - offset_x) // square_size)
    row = int((offset_y - y) // square_size)

    if board[row][col] or winner:
        return

    board[row][col] = xo
    if xo == "x":
        draw_x(row, col)
        xo = "o"
    else:
        draw_o(row, col)
        xo = "x"

    winner = check_winner()

    if winner:
        t.up()
        t.goto(offset_x + size / 2, offset_y + 10)
        t.write("%s wins!" % winner, align="center", font=("Arial", 32, "bold"))


def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]

    if all([board[row][col] for row in range(len(board)) for col in range(len(board[0]))]):
        return "nobody"

    return ""


def draw_board():
    for i in range(4):
        t.up()
        t.goto(offset_x, -size / 3 * i + offset_y)
        t.down()
        t.forward(size)

    t.right(90)
    for i in range(4):
        t.up()
        t.goto(offset_x + i * size / 3, offset_y)
        t.down()
        t.forward(size)


size = 300
square_size = size / 3
offset_x = -size / 2
offset_y = size / 2
board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]
winner = ""
xo = "x"
xo_size = size / 6

t = turtle.Turtle()
t.ht()
t.speed(200)
draw_board()
wn = turtle.Screen()
wn.onclick(draw)
wn.mainloop()




























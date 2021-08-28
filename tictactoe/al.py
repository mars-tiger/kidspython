import tutle

def draw_star(size, x, y):
  t.up()
  t.goto(x, y)
  t.down()
  t.forward(size)
  t.backward(size/2)
  t.left(60)
  t.up()
  t.forward(size/2)
  t.down()
  t.right(180)
  t.forward(size)
  t.left(180)
  t.forward(size/2)
  t.left(60)
  t.up()
  t.backward(size/2)
  t.down()
  t.forward(size)

def draw_board(size, x, y):
  t.up()
  t.goto(x, y)
  t.down()
  for i in range(4):
    t.forward(size)
    t.right(90)
  for i in range(2):
    for i in range(2):
      t.forward(size/3)
      t.right(90)
      t.forward(size)
      t.right(180)
      t.forward(size)
      t.right(90)
    t.forward(size/3)
    t.right(90)

t = turtle.Turtle()
draw_star(25, 0, 0)  

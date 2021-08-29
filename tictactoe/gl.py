def draw_x(row, col):
  x = col * size / 3 + offset_x + size / 6
  y = -row * size / 3 + offset_y - size / 6

  for i in range(3):
    t.up()
    t.home()
    t.goto(x, y)
    t.right(i * 60)
    t.forward(25)
    t.down()
    t.backward(50)

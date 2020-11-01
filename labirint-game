import play

play.set_backdrop("indigo")

#круг
ball = play.new_circle(x = 0, y = -200, radius = 20, color = "yellow")

#палочка
wall1 = play.new_box(x = -200, y = 0, width = 400,height =10, color = "white")

wall2 = play.new_box(x = -100, y = 100, width = 10,height =200, color = "white")

wall3 = play.new_box(x = -50, y = 0, width = 100,height =10, color = "white")

finish = play.new_text(words = "FINISH", x = -250, y = 150, font = None, font_size = 70, color = "white")
#-------------------------------------------

@play.when_program_starts
def start():
  ball.start_physics(bounciness = 0.2)
  wall1.start_physics(can_move = False)
  wall2.start_physics(can_move = False)
  wall3.start_physics(can_move = False)


@play.repeat_forever
def do():
  ball.physics.y_speed = 0
  ball.physics.x_speed = 0

  if play.key_is_pressed('w'):
    ball.physics.y_speed = 10
  if play.key_is_pressed('s'):
    ball.physics.y_speed = -10
  if play.key_is_pressed('d'):
    ball.physics.x_speed = 10
  if play.key_is_pressed('a'):
    ball.physics.x_speed = -10

  if ball.is_touching(finish):
    wall1.hide()
    wall2.hide()
    wall3.hide()
    finish.hide()
    play.new_text(words = "YOU WIN", x = 0, y = 0, font = None, font_size = 100, color = "yellow")
play.start_program()

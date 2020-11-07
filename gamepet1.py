
import play
#photo sprite
photo = play.new_image(image = "1.png", x=  0, y = 0, size = 50)

#text sprite
text = play.new_text(words = "Hello", x = 0, y = -200,font_size =50, color = "pink")

@play.when_program_starts
def start():
  pass

@play.repeat_forever
def do():
  if play.key_is_pressed('s'):
    text.words = "Crying"
    text.color = play.random_color()
    photo.image = "2.jpg"

  if play.key_is_pressed('f'):
    text.words = "Make up"
    photo.image = "1.png"

play.start_program()

#   a123_apple_1.py
import turtle as trtl
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

apple = trtl.Turtle()
apple.penup()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_the_apple():
  drawer.clear()
  wn.tracer(True)
  apple.goto(0, -200)
  wn.tracer(False)
  apple.hideturtle()

  

def draw_an_A():
  drawer.goto(-22, -45)
  drawer.color("white")
  drawer.write("A", font=("Arial", 55, "bold")) 


#-----function calls-----
draw_apple(apple)
draw_an_A()
wn.onkeypress(drop_the_apple, "a")

wn.listen()
wn.bgpic("background.gif")
wn.mainloop()
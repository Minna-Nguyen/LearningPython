import tkinter
# Luodaan kilpikonna
import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

# kilpikonna tekee 18 kierrosta
sade = 10
while sade < 100:
  kilpikonna.circle(sade)
  sade = sade + 5

tkinter.mainloop()
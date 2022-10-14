
import turtle as t
  

t.bgcolor("sky blue")
t.speed(0)
  

def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor (color)
    t.goto (x, y)
    t.pendown()
    t.begin_fill()
    t.circle (radius)
    t.end_fill()

 

draw_circle ("#ffffff", 30, 0, 0)
draw_circle ("#ffffff", 120, 0, -240)
  
# Drawing left eye
draw_circle ("#ffffff", 2, -10, 40) 
 
# Drawing right eye
draw_circle ("#ffffff", 2, 10, 40) 
 
# Drawing nose
draw_circle ("#FF6600", 3, 0, 35)  
   
# Drawing buttons on


x=-15
for i in range(6):
    x-=30
    draw_circle ("#ffffff", 2, 0, x)

  
  
  
# Function to draw arms 
def create_line(x, y, length, angle):
    t.penup()
    t.goto(x, y)
    t.lt(angle)
    t.pendown()
    t.forward(length)
    t.lt(360-angle)


create_line(-70, -50, 100, 100) 

create_line(70, -50, 100, 70)

create_line(-70, -200, 100, -100)

create_line(70, -200, 100, -70)

t.exitonclick()
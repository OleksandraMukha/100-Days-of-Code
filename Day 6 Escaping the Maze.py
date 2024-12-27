"""
On Day 6 of my 100 Days of Code journey, 
I focused on learning Python functions, indentation, while loops, 
and problem-solving with Karel. I applied these skills to build 
the "Escape the Maze" project, which used loops and logic to navigate 
Karel through a maze successfully.
"""
#Reeborg's World Wevsite Link
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Python Code
def turn_right():
        turn_left()
        turn_left()
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    

 

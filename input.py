import random
import turtle
l = "abcdefghijklmnoprstuvwxyz"
u = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
n = "0123456789"
s = "[]{}()*;/,.-_!?^#§£$%&="
a = l + u + n + s

ln = 1
style = ('Times New Roman', 20, 'bold')


def x(num):
    try:
        num = int(turtle.textinput("Password's lenght", "Press 0 to exit"))
        turtle.clear()
        turtle.color('deep pink')
        p = "".join(random.sample(a, num))
        if num != 0:
            turtle.write("Password : \n", font=style, align='center')
            turtle.write(f"{p}", font=style, align='center')

        if num == 0:
            turtle.clear()
            turtle.write("You used AndyPassGen\n Thank you!!!\n Click here ", font=style, align='center')
            turtle.exitonclick()
            turtle.mainloop()
            return num


    except:
        turtle.clear()
        turtle.write("Not valid ", font=style, align='center')
        num = 1


    return num


while ln != 0:
    x(ln)
    ln = x(ln)


turtle.exitonclick()
turtle.mainloop()









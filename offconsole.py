import random
import turtle
import time
bgcolor = turtle.textinput("offconsole", "Your BG for today: ")
color = turtle.textinput("offconsole", "Your favourite color: ")
t = turtle.Pen()
turtle.bgcolor(bgcolor)
t.pencolor(color)
a = ''
b = ''
c = ''
d = 0
e = 0
f = 0
cmd = '0'
z = 0
newgroup = ''
t.clear()
t.write("Welcome to offconsole! Read document with comands before use.")
time.sleep(3)
t.clear()
while cmd != 'stop':
    cmd = turtle.textinput("offconsole", "Your command:")
    if cmd == "write":
        yourgroup = turtle.textinput("offconsole", "Select group(a, b or c): ")
        yourtext = turtle.textinput("offconsole", "Text: ")
        if yourgroup == "a":
            a += yourtext
        elif yourgroup == "b":
            b += yourtext
        else:
            c += yourtext
        t.write("Successfully!")
        time.sleep(1)
        t.clear()
    if cmd == "check":
        yourgroup = turtle.textinput("offconsole", "Select group: ")
        if yourgroup == "a":
            t.write(a)
            time.sleep(3)
            t.clear()
        elif yourgroup == "b":
            t.write(b)
            time.sleep(3)
            t.clear()
        elif yourgroup == "d":
            t.write(d)
            time.sleep(3)
            t.clear()
        elif yourgroup == "e":
            t.write(e)
            time.sleep(3)
            t.clear()
        elif yourgroup == "f":
            t.write(f)
            time.sleep(3)
            t.clear()
        elif yourgroup == newgroup:
            t.write(newgroupcol)
            time.sleep(3)
            t.clear()
        elif yourgroup == "c":
            t.write(c)
            time.sleep(3)
            t.clear()
    if cmd == "gen":
        x = int(turtle.numinput("offconsole", "first: "))
        y = int(turtle.numinput("offconsole", "second: "))
        gen = random.randint(x,y)
        yourgroup = turtle.textinput("offconsole", "Select group(d, e or f): ")
        if yourgroup == "d":
            d += gen
        elif yourgroup == "e":
            e += gen
        else:
            f += gen
        t.write("Successfully!")
        time.sleep(3)
        t.clear()
    if cmd == "new":
        newgroup = turtle.textinput("offconsole", "Group name(you are creating a list of 3 cells): ")
        newgroupcol = [[] for i in range(3)]
        t.write("Successfully!")
        time.sleep(3)
        t.clear()
    if cmd == "fill":
        col = int(turtle.numinput("offconsole", "How many cells would you like to fill per time: "))
        for i in range(col):
            inf = turtle.textinput("offconsole", "What you would like to write?: ")
            newgroupcol[z].append(inf)
            z += 1
        t.write("Successfully!")
        time.sleep(3)
        t.clear()
    if cmd == "fillspecial":
        colspec = int(turtle.numinput("offconsole", "What cell would you like to fill: "))
        inf = turtle.textinput("offconsole", "What would you like to write?: ")
        newgroupcol[colspec].append(inf)
        t.write("Successfully!")
        time.sleep(1)
        t.clear()
    if cmd == "credits":
        t.write("Noobisbro, 2021.")
        time.sleep(3)
        t.clear()
    if cmd == "calc":
        do = turtle.textinput("offconsole", "What do you want to do: ")
        x = int(turtle.numinput("offconsole", "first: "))
        y = int(turtle.numinput("offconsole", "second: "))
        if do == "*":
            resdo = x*y
        elif do == "/":
            resdo = x/y
        elif do == "-":
            resdo = x-y
        elif do == "+":
            resdo = x+y
        t.write(resdo)
        time.sleep(3)
        t.clear()
    if cmd == "cleardisk":
        a = ''
        b = ''
        c = ''
        d = 0
        e = 0
        f = 0
        cmd = '0'
        z = 0
        t.clear()



        
    


        
        


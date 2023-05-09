from tkinter import Tk, HIDDEN, NORMAL, Canvas

def toggle_eyes():
    current_color = c.itemcget(eye_left,'fill')
    new_color = body_color if current_color=='white' else 'white'
    current_state=c.itemcget(pupil_left,'state')
    new_state = NORMAL if current_state==HIDDEN else HIDDEN
    c.itemconfigure(pupil_left,state=new_state)
    c.itemconfigure(pupil_right,state=new_state)
    c.itemconfigure(eye_left,fill=new_color)
    c.itemconfigure(eye_right,fill=new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left,10,-5)
        c.move(pupil_right,-10,-5)
        c.crossed_eyes=True
    else:
        c.move(pupil_left,-10,5)
        c.move(pupil_right,10,5)
        c.crossed_eyes=False

def show_happy(event):
    if(20<=event.x and event.x<=350) and (20<=event.y and event.y<=350):
        c.itemconfigure(mouth_happy,state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad,state=HIDDEN)
        c.happy_level=10
    return

def hide_happy(event):
    c.itemconfigure(mouth_happy,state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad,state=HIDDEN)
    c.happy_level=10
    return

def sad():
    if c.happy_level==0:
        c.itemconfigure(mouth_happy,state=HIDDEN)
        c.itemconfigure(mouth_normal,state=HIDDEN)
        c.itemconfigure(mouth_sad,state=NORMAL)
    else:
        c.happy_level -= 1
    win.after(500,sad)


win=Tk()

c=Canvas(win, width=400, height=400)
c.configure(bg="light yellow",highlightthickness=0)

body_color = "light pink"
body = c.create_oval(35,20,365,350,outline=body_color,fill=body_color)

foot_left=c.create_oval(65,320,145,360,outline=body_color,fill=body_color)
foot_right=c.create_oval(250,320,330,360,outline=body_color,fill=body_color)

#ear_left= c.create_oval(75,80,75,80,outline=body_color,fill=body_color)
eye_left=c.create_oval(130,110,160,155,outline=body_color,fill="white")
pupil_left=c.create_oval(140,145,150,155,outline='black',fill='black')

eye_right=c.create_oval(230,110,260,155,outline=body_color,fill="white")
pupil_right=c.create_oval(240,145,250,155,outline='black',fill='black')

mouth_normal=c.create_line(170,250,200,262,230,250, smooth=1, width=2, state=NORMAL,fill='#ff69b4')
mouth_happy=c.create_line(170,250,200,282,230,250, smooth=1, width=2, state=HIDDEN,fill='#ff69b4')
mouth_sad=c.create_line(170,250,200,230,230,250, smooth=1, width=2, state=HIDDEN,fill='#ff69b4')



c.pack()

c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)

c.crossed_eyes = False
c.happy_level=10

win.after(1000,blink)
win.after(6000,sad)


win.mainloop()
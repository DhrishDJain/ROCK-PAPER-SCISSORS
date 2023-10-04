from tkinter import *
from tkinter import ttk
from time import sleep
import random

#GUI
root=Tk()
root.configure(background="black",width=1000)
root.maxsize(1100,1300)
root.minsize(1100,1300)
root.title("ROCK PAPER SCISSOR GAME")
# creating canvaskmijf
canvas = Canvas(background="black",border=2,height=900)
your_score=0
comp=0

#decision making logic
def logic(player,com):
    global your_score
    global comp
    
    if player==com :
        return "DRAW"
    elif player==1 and com==2:
        comp+=1
        print(your_score,comp)
    
        return "YOU LOSE"
    elif player==2 and com==3:
        comp+=1
        print(your_score,comp)
        return "YOU LOSE"
    elif player==3 and com==1:
        comp+=1
        print(your_score,comp)
        return "YOU LOSE"
    else:
        your_score+=1
        print(your_score,comp)
        return "YOU WON"
#function to chose between 3 for oppoent
def computer():
    global com
    global oppchoise
    choise=["1","2","3"]
    com=int(random.choice(choise))
    if com==1:
       oppchoise="ROCK"
    elif com==2:
        oppchoise="PAPER"
    else:
        oppchoise="SCISSOR"
    print(f"computer choose {com}")


def display(player):
    global z
    global pls
    global ops
    global opp

    #calling computer function to set oppent choise
    computer()
    #To prevent erro of z not defind and clearing previous result,your score,opponent score and opponent choise
    try:
        clr(z)
        clr(pls)
        clr(ops)
        clr(opp)
        
    except:
        pass
    
    z=canvas.create_text(576,170,fill="yellow",font=('typewriter 50 bold'))
    canvas.itemconfig(z,text=logic(player,com))
    
    
    pls=canvas.create_text(525, 300, text=f"YOUR SCORE : {your_score}", fill="pink", font=('typewriter 25 bold'))
    ops=canvas.create_text(566, 400, text=f"OPPONENT SCORE : {comp}", fill="pink", font=('typewriter 25 bold'))
    opp=canvas.create_text(930, 160, text=f"{oppchoise}", fill="#00FFFF", font=('typewriter 25 bold'))
    

#function to get user choise by collecting text from the button which is pressed
def click_animation(r):
    r.config(relief=SUNKEN)
    r.update()
    r.config(relief=RAISED)
    sleep(0.3)
    
        
def playerchoise(event):
    pltext=event.widget.cget("text")
    if pltext=="ROCK":
        click_animation(r)
        player=1
    elif pltext=="PAPER":
        click_animation(p)
        player=2
    else:
        click_animation(s)
        player=3
    
    display(player)

    
#function to clear previous text
def clr(i):
    try:
       canvas.delete(i)
    except:
        pass

canvas.create_text(176, 50,text="YOUR CHOISE", fill="#DF00FF",font='typewriter 25 bold')
canvas.create_text(920, 50,text=f"OPPONENT CHOOSE", fill="#DF00FF",font='typewriter 25 bold')
canvas.create_rectangle(852,109,1010,205,outline="#00FFFF",width=12)

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting background of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover,foreground=colorOnLeave))
	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave,foreground=colorOnHover))

# BUTTONS
rock=canvas.create_rectangle(30,522,310,638,outline="red",width=12)
r=Button(canvas,text="ROCK",width=13,height=2,bg="black",font="comicsansmc 25 bold",foreground="red",activebackground="red",justify=LEFT,relief=RAISED)
r.place(x=34,y=527)
changeOnHover(r,"red","black")
r.bind('<Button-1>',playerchoise)

paper=canvas.create_rectangle(30,122,310,238,outline="blue",width=12)
p=Button(canvas,text="PAPER",width=13,height=2,bg="black",font="comicsansmc 25 bold",foreground="blue",activebackground="blue",justify=CENTER)
p.place(x=35,y=127)
p.bind('<Button-1>',playerchoise)
changeOnHover(p,"blue","black")

scissor=canvas.create_rectangle(30,322,310,438,outline="green",width=12)
s=Button(canvas,text="SCISSOR",width=13,height=2,bg="black",font="comicsansmc 25 bold",foreground="green",activebackground="green",justify=RIGHT)
s.place(x=34,y=327)
s.bind('<Button-1>',playerchoise)
changeOnHover(s,"green","black")
canvas.pack(fill=BOTH)
root.mainloop()


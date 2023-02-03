from tkinter import *
from tkinter import messagebox

#TODO list:
#setup ui
#function to create X and O
#Functionality:
turns=0
score_0=0
score_X=0
game_is_on=True
button_1_0 = False
button_1_X = False
button_2_0 = False
button_2_X = False
button_3_0 = False
button_3_X = False
button_4_0 = False
button_4_X = False
button_5_0 = False
button_5_X = False
button_6_0 = False
button_6_X = False
button_7_0 = False
button_7_X = False
button_8_0 = False
button_8_X = False
button_9_0 = False
button_9_X = False
def button_1_pressed():
    global turns,button_1_0,button_1_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_1.config(text=0)
        button_1_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on=False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_1.config(text=X)
        button_1_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_2_pressed():
    global turns,button_2_0,button_2_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_2.config(text=0)
        button_2_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_2.config(text=X)
        button_2_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_3_pressed():
    global turns,button_3_0,button_3_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_3.config(text=0)
        button_3_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_3.config(text=X)
        button_3_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_4_pressed():
    global turns,button_4_0,button_4_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_4.config(text=0)
        button_4_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_4.config(text=X)
        button_4_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_5_pressed():
    global turns,button_5_0,button_5_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_5.config(text=0)
        button_5_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_5.config(text=X)
        button_5_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")

def button_6_pressed():
    global turns,button_6_0,button_6_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_6.config(text=0)
        button_6_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_6.config(text=X)
        button_6_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_7_pressed():
    global turns,button_7_0,button_7_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_7.config(text=0)
        button_7_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_7.config(text=X)
        button_7_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")

def button_8_pressed():
    global turns,button_8_0,button_8_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_8.config(text=0)
        button_8_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0 += 1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_8.config(text=X)
        button_8_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def button_9_pressed():
    global turns,button_9_0,button_9_X,game_is_on,score_0,score_X
    turns += 1
    if turns%2==0:
        button_9.config(text=0)
        button_9_0=True
        if button_1_0 and button_2_0 and button_3_0 or button_4_0 and button_5_0 and button_6_0 or button_7_0 and button_8_0 and button_9_0 or button_1_0 and button_4_0 and button_7_0 or button_2_0 and button_5_0 and button_8_0 or button_3_0 and button_6_0 and button_9_0 or button_1_0 and button_5_0 and button_9_0 or button_3_0 and button_5_0 and button_7_0:
            messagebox.showinfo(message="0 win")
            score_0+=1
            change_score_0()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="X turn")
    else:
        button_9.config(text=X)
        button_9_X=True
        if button_1_X and button_2_X and button_3_X or button_4_X and button_5_X and button_6_X or button_7_X and button_8_X and button_9_X or button_1_X and button_4_X and button_7_X or button_2_X and button_5_X and button_8_X or button_3_X and button_6_X and button_9_X or button_1_X and button_5_X and button_9_X or button_3_X and button_5_X and button_7_X:
            messagebox.showinfo(message="X win")
            score_X+=1
            change_score_X()
            game_is_on = False
        elif (button_1_0 or button_1_X) and (button_2_0 or button_2_X) and (button_3_0 or button_3_X) and (button_4_0 or button_4_X) and (button_5_0 or button_5_X) and (button_6_0 or button_6_X) and (button_7_0 or button_7_X) and (button_8_0 or button_8_X) and (button_9_0 or button_9_X):
            messagebox.showinfo(message="Draw")
        else:
            turn_label.config(text="0 turn")
def reset():
    global buttons_list,turns,button_1_0,button_1_X,button_2_0,button_2_X,button_3_0,button_3_X,button_4_0,button_4_X,button_5_0,button_5_X,button_6_0,button_6_X,button_7_0,button_7_X,button_8_0,button_8_X,button_9_0,button_9_X
    turns=0
    button_1_0 = False
    button_1_X = False
    button_2_0 = False
    button_2_X = False
    button_3_0 = False
    button_3_X = False
    button_4_0 = False
    button_4_X = False
    button_5_0 = False
    button_5_X = False
    button_6_0 = False
    button_6_X = False
    button_7_0 = False
    button_7_X = False
    button_8_0 = False
    button_8_X = False
    button_9_0 = False
    button_9_X = False
    for button in buttons_list:
        button.config(text="")
    turn_label.config(text="X turn")
def change_score_0():
    global score_0
    score_0_label.config(text=f"Score of 0: {score_0}")
def change_score_X():
    global score_X
    score_X_label.config(text=f"Score of X: {score_X}")
def reset_scores():
    global score_0,score_X
    score_0=0
    score_X=0
    score_0_label.config(text=f"Score of 0: {score_0}")
    score_X_label.config(text=f"Score of X: {score_X}")
#UI Setup:
window=Tk()
window.title("TIC-TAC-TOE")
window.config(padx=50,pady=50,bg="coral")

buttons_list=[]
score_0_label=Label(text=f"Score of 0: {score_0}",padx=5,pady=5,bg="coral",fg="black")
score_0_label.grid(row=0,column=0)

score_X_label=Label(text=f"Score of X: {score_X}",padx=5,pady=5,bg="coral",fg="black")
score_X_label.grid(row=1,column=0)

turn_label=Label(text="X turn",padx=5,pady=5,bg="coral",fg="black")
turn_label.grid(row=2,column=0,columnspan=3)

button_1=Button(width=7,height=7,command=button_1_pressed)
button_1.grid(row=3,column=0)
buttons_list.append(button_1)

button_2=Button(width=7,height=7,command=button_2_pressed)
button_2.grid(row=3,column=1)
buttons_list.append(button_2)

button_3=Button(width=7,height=7,command=button_3_pressed)
button_3.grid(row=3,column=2)
buttons_list.append(button_3)

button_4=Button(width=7,height=7,command=button_4_pressed)
button_4.grid(row=4,column=0)
buttons_list.append(button_4)

button_5=Button(width=7,height=7,command=button_5_pressed)
button_5.grid(row=4,column=1)
buttons_list.append(button_5)

button_6=Button(width=7,height=7,command=button_6_pressed)
button_6.grid(row=4,column=2)
buttons_list.append(button_6)

button_7=Button(width=7,height=7,command=button_7_pressed)
button_7.grid(row=5,column=0)
buttons_list.append(button_7)

button_8=Button(width=7,height=7,command=button_8_pressed)
button_8.grid(row=5,column=1)
buttons_list.append(button_8)

button_9=Button(width=7,height=7,command=button_9_pressed)
button_9.grid(row=5,column=2)
buttons_list.append(button_9)

reset_button=Button(text="Reset",command=reset,bg="coral",highlightthickness=0,padx=5,pady=5)
reset_button.grid(row=6,column=0)

reset_score_button=Button(text="Reset scores",command=reset_scores,bg="coral",highlightthickness=0,padx=5,pady=5)
reset_score_button.grid(row=6,column=1,columnspan=2)
window.mainloop()






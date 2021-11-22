import tkinter as tk
from tkinter.constants import FALSE, S, TRUE
from tkinter.font import Font
from typing import Text
import time


time1=0
LP="O"
turn="O"





root=tk.Tk()




canvas=tk.Canvas(root,width=300,height=300,bg="#FF9B6A")
canvas.grid(columnspan=3,rowspan=3)
BUTTON_WIDTH_HEIGHT=4






       



#button
def XOButton(col,row,colour):


    #buttonPressedCommand
    def command(Value):    
        if  Value=="X":
            X_OText.set("O")
            turn="O"  
        elif Value=="O":
            X_OText.set("X")
            turn="X"    
        elif Value=="":
            X_OText.set("X")
            turn=""
        print(turn)

            

    #button
    X_OText=tk.StringVar(root,"",str(col)+str(row))
    X_OButton=tk.Button(width=BUTTON_WIDTH_HEIGHT*2,height=BUTTON_WIDTH_HEIGHT,textvariable=X_OText,font="Impact",bg=colour,command=command("x"),borderwidth = 0)
    X_OText.set("")
    X_OButton.grid(column=col,row=row)

for row in range(3):
    for column in range(3):
        XOButton(row,column,"#88E0EF")











   

        






root.mainloop()
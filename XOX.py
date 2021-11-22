import tkinter as tk
from tkinter import font


#previous player set as None
previousPlayer=""


#Function To choose next player
class PLayerSet:
    def __init__(self,PreviousPlayer):
        self.name=PreviousPlayer
    def NextPlayer(PreviousPlayer):
        global previousPlayer
        if PreviousPlayer=="X":
            PreviousPlayer="O"
            previousPlayer="O"

        elif PreviousPlayer=="O":
            PreviousPlayer="X"
            previousPlayer="X"

        elif PreviousPlayer=="":
            PreviousPlayer="X"
            previousPlayer="X"

        return PreviousPlayer

#PLayerSet.NextPlayer(PLayerSet,"X")
#print(previousPlayer)





#tkinter Window#########################
root=tk.Tk()




canvas=tk.Canvas(root,height=300,width=300,bg="#94B3FD")
canvas.grid(columnspan=3,rowspan=3)


ButtonImage=tk.PhotoImage(file="logo.png")



def PlacePlayer(col,row,Colour):

    def Command():  
        global previousPlayer
        PLayerSet.NextPlayer(previousPlayer)
        PlayerText.set(previousPlayer)

    PlayerText=tk.StringVar(root,"")
    box=tk.Button(root,height=4,width=10,textvariable=PlayerText,command=Command,font="Impact",bg=Colour,borderwidth=0)
    box.grid(column=col,row=row)

for row in range(3):
    for column in range(3):
        PlacePlayer(column,row,"#B983FF")



root.mainloop()

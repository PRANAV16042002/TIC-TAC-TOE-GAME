import tkinter as tk
from tkinter import messagebox

# Global Variables
xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1  # 1 for X, 0 for O

def sum(a, b, c):
    return a + b + c

def checkWin():
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            messagebox.showinfo("Tic Tac Toe", "X Won the match!")
            resetGame()
            return True
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            messagebox.showinfo("Tic Tac Toe", "O Won the match!")
            resetGame()
            return True
    return False

def onClick(index):
    global turn
    if xState[index] == 0 and zState[index] == 0:
        if turn == 1:
            buttons[index].config(text="X")
            xState[index] = 1
            turn = 0
        else:
            buttons[index].config(text="O")
            zState[index] = 1
            turn = 1
        if checkWin():
            return
        if sum(xState) + sum(zState) == 9:  # Check for draw
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            resetGame()

def resetGame():
    global xState, zState, turn
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    for button in buttons:
        button.config(text="")

# Creating the main window
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

# Creating buttons for the game grid
for i in range(9):
    button = tk.Button(root, text="", font="Arial 20 bold", width=5, height=2, command=lambda i=i: onClick(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the main loop
root.mainloop()

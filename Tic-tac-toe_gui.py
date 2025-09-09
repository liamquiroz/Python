import tkinter as tk
from tkinter import messagebox

# Game window
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Check for winner
def check_winner():
    global current_player

    # Rows, Columns, Diagonals
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Check if board is full
def board_full():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Handle click
def on_click(r, c):
    global current_player

    if buttons[r][c]["text"] == "":
        buttons[r][c]["text"] = current_player
        buttons[r][c]["state"] = "disabled"

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
            return
        elif board_full():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Reset board
def reset_board():
    global current_player
    current_player = "X"
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = ""
            buttons[r][c]["state"] = "normal"

# Create grid of buttons
for r in range(3):
    for c in range(3):
        btn = tk.Button(root, text="", font=("Arial", 32), width=5, height=2,
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c)
        buttons[r][c] = btn

# Reset button
reset_btn = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_board)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()
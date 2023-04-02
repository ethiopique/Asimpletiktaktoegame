import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", width=10, height=5,
                                   font=("Helvetica", 20, "bold"),
                                   command=lambda i=i, j=j: self.button_click(i, j))
                if (i + j) % 2 == 0:
                    button.configure(bg="white")
                else:
                    button.configure(bg="light gray")
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

            # Set the background color of "X" buttons to red and "O" buttons to blue
            if i == 0:
                self.buttons[i][0].configure(bg="red")
                self.buttons[i][2].configure(bg="blue")
            elif i == 1:
                self.buttons[i][1].configure(bg="red")
            else:
                self.buttons[i][0].configure(bg="blue")
                self.buttons[i][2].configure(bg="red")

    def button_click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].configure(text=self.current_player)
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != "":
            return True
        else:
            return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.configure(text="")
        self.current_player = "X"

root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()

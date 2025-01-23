import os

class Board:
    def __init__(self):
        self.cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("------------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("------------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
            return True
        else:
            return False

    def is_winner(self, player):
        # Check all winning combinations
        return (
            (self.cells[1] == player and self.cells[2] == player and self.cells[3] == player) or
            (self.cells[4] == player and self.cells[5] == player and self.cells[6] == player) or
            (self.cells[7] == player and self.cells[8] == player and self.cells[9] == player) or
            (self.cells[1] == player and self.cells[4] == player and self.cells[7] == player) or
            (self.cells[2] == player and self.cells[5] == player and self.cells[8] == player) or
            (self.cells[3] == player and self.cells[6] == player and self.cells[9] == player) or
            (self.cells[1] == player and self.cells[5] == player and self.cells[9] == player) or
            (self.cells[3] == player and self.cells[5] == player and self.cells[7] == player)
        )

    def is_tie(self):
        return " " not in self.cells[1:]

    def reset(self):
        self.cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe by Tanzir\n")

def refresh_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print_header()
    board.display()

# Main game loop
while True:
    refresh_screen()

    # Player X's turn
    while True:
        x_choice = int(input("\nX) Please choose 1 - 9: "))
        if board.update_cell(x_choice, "X"):
            break
        else:
            print("Cell already taken. Choose another.")

    refresh_screen()
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nIt's a tie!\n")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            board.reset()
            continue
        else:
            break

    # Player O's turn
    while True:
        o_choice = int(input("\nO) Please choose 1 - 9: "))
        if board.update_cell(o_choice, "O"):
            break
        else:
            print("Cell already taken. Choose another.")

    refresh_screen()
    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nIt's a tie!\n")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == "yes":
            board.reset()
            continue
        else:
            break

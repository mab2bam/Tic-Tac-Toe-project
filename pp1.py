import tkinter as tk

def set_tile(row, column):
    global curr_player, game_over

    if game_over:
        return

    if board[row][column]["text"] != "":
        # Tile already taken
        return

    # Mark the board with the current player's symbol
    board[row][column]["text"] = curr_player

    # Check for a winner or a draw
    if check_winner():
        game_over = True
        score[curr_player] += 1
        label["text"] = f"{curr_player} wins! Score: X-{score['X']} O-{score['O']} Draws-{score['Draws']}"
        update_tile_colors()
        return

    # Check for a draw
    if turns == 9:
        game_over = True
        score['Draws'] += 1
        label["text"] = f"It's a draw! Score: X-{score['X']} O-{score['O']} Draws-{score['Draws']}"
        return

    # Switch player
    curr_player = 'O' if curr_player == 'X' else 'X'
    label["text"] = f"{curr_player}'s turn"

def check_winner():
    # Check rows and columns
    for i in range(3):
        if (board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] and
            board[i][0]["text"] != ""):
            return True
        if (board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"] and
            board[0][i]["text"] != ""):
            return True

    # Check diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and
        board[0][0]["text"] != ""):
        return True
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and
        board[0][2]["text"] != ""):
        return True

    return False

def update_tile_colors():
    # Color the winning tiles
    for i in range(3):
        if (board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] and
            board[i][0]["text"] != ""):
            for j in range(3):
                board[i][j].config(bg="lightgrey", fg="yellow")
        if (board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"] and
            board[0][i]["text"] != ""):
            for j in range(3):
                board[j][i].config(bg="lightgrey", fg="yellow")
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and
        board[0][0]["text"] != ""):
        for i in range(3):
            board[i][i].config(bg="lightgrey", fg="yellow")
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and
        board[0][2]["text"] != ""):
        for i in range(3):
            board[i][2-i].config(bg="lightgrey", fg="yellow")

def new_game():
    global turns, game_over, curr_player

    turns = 0
    game_over = False
    curr_player = 'X'

    label["text"] = f"{curr_player}'s turn"

    for i in range(3):
        for j in range(3):
            board[i][j].config(text="", bg="gray", fg="blue")

def exit_game():
    window.destroy()

# Game setup
score = {'X': 0, 'O': 0, 'Draws': 0}
curr_player = 'X'
turns = 0
game_over = False

# Window setup
window = tk.Tk()
window.title("Tic Tac Toe")

frame = tk.Frame(window)
label = tk.Label(frame, text=f"{curr_player}'s turn", font=("Consolas", 20), bg="gray", fg="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

board = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Consolas", 50, "bold"),
                                       bg="gray", fg="blue", width=4, height=2,
                                       command=lambda r=row, c=column: set_tile(r, c))
        board[row][column].grid(row=row+1, column=column)

restart_button = tk.Button(frame, text="Restart", font=("Consolas", 20), bg="gray", fg="white",
                           command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

exit_button = tk.Button(frame, text="Exit", font=("Consolas", 20), bg="gray", fg="white",
                        command=exit_game)
exit_button.grid(row=5, column=0, columnspan=3, sticky="we")

frame.pack()
window.mainloop()

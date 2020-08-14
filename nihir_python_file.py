import random

def set_match_mode(last_move="O"):

    player_options = ["user", "easy", "medium"]

    while True:

        match_cells = []
        for cell in range(9):
            match_cells.append(" ")

        user_command = input("Input command:").split()

        try:
            if user_command[0] == "start":
                if user_command[1] in player_options:
                    if user_command[2] in player_options:
                        first_player = user_command[1]
                        second_player = user_command[2]
                        display_match_cells(match_cells)
                        check_move(match_cells, (first_player, second_player), last_move)

        except IndexError:
            print("Bad parameters!")

        if len(user_command) == 1:
            if user_command[0] != "exit":
                print("Bad parameters!")
            else:

                exit()

        else:
            print("Bad parameters!")


def display_match_cells(match_cells):

    print("-" * 9)
    for rows in range(0, 9, 3):
        print("|", end = " ")
        print(match_cells[rows], match_cells[rows + 1], match_cells[rows + 2], sep = " ", end = " |")
        print("")
    print("-" * 9)


def user_move(match_cells):

    match_coordinates = {(1, 3) : 0, (2, 3) : 1, (3, 3) : 2,
                         (1, 2) : 3, (2, 2) : 4, (3, 2) : 5,
                         (1, 1) : 6, (2, 1) : 7, (3, 1) : 8}

    is_cell_occupied = True

    while is_cell_occupied is True:

        user_coordinates = input("Enter the coordinates:").split()

        try:
            user_coordinates[0] = int(user_coordinates[0])
            user_coordinates[1] = int(user_coordinates[1])
        except:
            print("You should enter numbers!")
            continue

        if (0 < user_coordinates[0] < 4) and (0 < user_coordinates[1] < 4):
            user_coordinate = match_coordinates[user_coordinates[0], user_coordinates[1]]
            if match_cells[user_coordinate] == " ":
                is_cell_occupied = False
                break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
            continue

    return user_coordinate


def easy_computer_move(match_cells):

    is_cell_occupied = True

    while is_cell_occupied is True:
        computer_coordinate = random.randint(0, 8)
        if match_cells[computer_coordinate] == " ":
            is_cell_occupied = False
            break

    return computer_coordinate


def medium_computer_move(match_cells, last_move):

    if last_move == "O":
        current_move = "X"
    elif last_move == "X":
        current_move = "O"

    cells = []
    for cell in range(9):
        cells.append(int(cell))

    is_cell_occupied = True

    while is_cell_occupied is True:

        computer_coordinate = medium_difficulty_AI(match_cells, current_move)
        if computer_coordinate == -1:
            computer_coordinate = medium_difficulty_AI(match_cells, last_move)
            if computer_coordinate == -1:
                computer_coordinate = random.choice(cells)
                cells.remove(computer_coordinate)

        if match_cells[computer_coordinate] == " ":
            is_cell_occupied = False
            break

    return computer_coordinate

def medium_difficulty_AI(match_cells, move):

    computer_coordinate = -1

    if move == "O":
        current_move = "O"
        last_move = "X"
    elif move == "X":
        current_move = "X"
        last_move = "O"

    for rows in range(0, 9, 3):
        if match_cells[rows] == match_cells[rows + 1] == current_move:
            computer_coordinate = rows + 2
            break
        if match_cells[rows + 1] == match_cells[rows + 2] == current_move:
            computer_coordinate = rows
            break
        if match_cells[rows] == match_cells[rows + 2] == current_move:
            computer_coordinate = rows + 1
            break

    for columns in range(0, 3):
        if match_cells[columns] == match_cells[columns + 3] == current_move:
            computer_coordinate = columns + 6
            break
        if match_cells[columns] == match_cells[columns + 6] == current_move:
            computer_coordinate = columns + 3
            break
        if match_cells[columns + 3] == match_cells[columns + 6] == current_move:
            computer_coordinate = columns
            break

    if match_cells[0] == match_cells[4] == current_move:
        computer_coordinate = 8
    if match_cells[0] == match_cells[8] == current_move:
        computer_coordinate = 4
    if match_cells[4] == match_cells[8] == current_move:
        computer_coordinate = 0

    if match_cells[2] == match_cells[4] == current_move:
        computer_coordinate = 6
    if match_cells[2] == match_cells[6] == current_move:
        computer_coordinate = 4
    if match_cells[4] == match_cells[6] == current_move:
        computer_coordinate = 2

    return computer_coordinate


def check_move(match_cells, players, last_move):

    player_moves = {"user" : "user_move(match_cells)",
                    "easy" : "easy_computer_move(match_cells)",
                    "medium" : "medium_computer_move(match_cells, last_move)"}

    first_player, second_player = players

    if last_move == "O":
        coordinate = eval(player_moves[first_player])
    elif last_move == "X":
        coordinate = eval(player_moves[second_player])

    make_move(match_cells, (first_player, second_player), (last_move, coordinate))


def make_move(match_cells, players, moves):

    first_player, second_player = players

    last_move, coordinate = moves

    if last_move == "O":

        match_cells[coordinate] = "X"
        last_move = "X"
        if first_player == "easy":
            print('Making move level "easy"')
        elif first_player == "medium":
            print('Making move level "medium"')

    elif last_move == "X":

        match_cells[coordinate] = "O"
        last_move = "O"
        if second_player == "easy":
            print('Making move level "easy"')
        elif second_player == "medium":
            print('Making move level "medium"')

    check_match_status(match_cells, (first_player, second_player), last_move)


def check_match_status(match_cells, players, last_move):

    points_X , points_O = calculate_points(match_cells)

    display_match_cells(match_cells)

    if " " in match_cells:
        if points_X == 0:
            if points_O == 0:
                first_player, second_player = players
                check_move(match_cells, (first_player, second_player), last_move)
    if " " not in match_cells:
        if points_X == 0:
            if points_O == 0:
                print("Draw")
    else:
        if points_X > 0:
            print("X wins")
        elif points_O > 0:
            print("O wins")

    print("")

    set_match_mode(last_move)


def calculate_points(match_cells):

    points_X = points_O = 0

    for rows in range(0, 9, 3):
        if match_cells[rows] == match_cells[rows + 1] == match_cells[rows + 2]:
            if match_cells[rows] == "X":
                points_X += 1
            elif match_cells[rows] == "O":
                points_O += 1

    for rows in range(0, 3):
        if match_cells[rows] == match_cells[rows + 3] == match_cells[rows + 6]:
            if match_cells[rows] == "X":
                points_X += 1
            elif match_cells[rows] == "O":
                points_O += 1

    if match_cells[0] == match_cells[4] == match_cells[8]:
        if match_cells[0] == "X":
            points_X += 1
        elif match_cells[0] == "O":
            points_O += 1

    if match_cells[2] == match_cells[4] == match_cells[6]:
        if match_cells[2] == "X":
            points_X += 1
        elif match_cells[2] == "O":
            points_O += 1

    return points_X, points_O


def main():

    set_match_mode()


if __name__ == "__main__":

    main()
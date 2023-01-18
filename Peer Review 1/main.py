ROWS = 3
COLUMNS = 3


def main():
    print("***** THE TIC-TAC-TOE GAME - powered by PYTHON *****")
    frame = list()
    for i in range(ROWS):
        row = [" "] * COLUMNS
        frame.append(row)
    gamer = 0
    plays = 0
    table_print_function(frame)
    while (gamer == 0) or (gamer == 1) and (plays < 9):
        if gamer == 0:
            print("Player O is your turn!")
            frame = action(frame, gamer)
            gamer = check(frame, gamer)
            plays += 1
        elif gamer == 1:
            print("Player X is your turn!")
            frame = action(frame, gamer)
            gamer = check(frame, gamer)
            plays += 1
    if gamer == 2:
        print("The winner is Player O!")
    elif gamer == 3:
        print("The winner is Player X!")
    if plays == (ROWS * COLUMNS):
        print("Draw! No winner.")


def table_print_function(table):
    print(f"{table[0]}\n{table[1]}\n{table[2]}")


def action(game, turn):
    state = False
    while state is False:
        coordinate_x = input("Insert x coordinate where you want to put your sign: ")
        coordinate_y = input("Insert y coordinate where you want to put your sign: ")
        try:
            y = int(coordinate_y) - 1
            x = int(coordinate_x) - 1
            if game[y][x] == " ":
                if turn == 0:
                    game[y][x] = "O"
                else:
                    game[y][x] = "X"
                state = True
                table_print_function(game)
                return game
            else:
                print("Error, the space is already occupied!")
        except ValueError:
            print("Insert numbers!")
        except IndexError:
            print("Insert a valid index!")


def check(desk, user):
    a = None
    if user == 0:
        a = "O"
    elif user == 1:
        a = "X"
    for rows in range(ROWS):
        if (desk[0][rows] == a) and (desk[1][rows] == a) and (desk[2][rows] == a):
            user += 2
    for column in range(COLUMNS):
        if (desk[column][0] == a) and (desk[column][1] == a) and (desk[column][2] == a):
            user += 2
    if (desk[0][0] == a) and (desk[1][1] == a) and (desk[2][2] == a):
        user += 2
    elif (desk[2][0] == a) and (desk[1][1] == a) and (desk[0][2] == a):
        user += 2
    else:
        if user == 0:
            user = 1
        elif user == 1:
            user = 0
    return user


if __name__ == '__main__':
    main()

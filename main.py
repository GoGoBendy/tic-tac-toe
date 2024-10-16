line1 = [1, 2, 3]
line2 = [4, 5, 6]
line3 = [7, 8, 9]

WINNER = False

TURNCOUNTER = 1


# places an O in the desired spot
def placeo(n):
    if n == 1:
        line1[0] = "O"
    elif n == 2:
        line1[1] = "O"
    elif n == 3:
        line1[2] = "O"
    elif n == 4:
        line2[0] = "O"
    elif n == 5:
        line2[1] = "O"
    elif n == 6:
        line2[2] = "O"
    elif n == 7:
        line3[0] = "O"
    elif n == 8:
        line3[1] = "O"
    elif n == 9:
        line3[2] = "O"


# places an X in the desired spot
def placex(n):
    if n == 1:
        line1[0] = "X"
    elif n == 2:
        line1[1] = "X"
    elif n == 3:
        line1[2] = "X"
    elif n == 4:
        line2[0] = "X"
    elif n == 5:
        line2[1] = "X"
    elif n == 6:
        line2[2] = "X"
    elif n == 7:
        line3[0] = "X"
    elif n == 8:
        line3[1] = "X"
    elif n == 9:
        line3[2] = "X"


# checks whether or not the same symbol is in a row, column, or diagonal
def check_winner(line4, line5, line6):
    if line4[0] == line4[1] == line4[2]:
        return True
    elif line5[0] == line5[1] == line5[2]:
        return True
    elif line6[0] == line6[1] == line6[2]:
        return True
    elif line4[0] == line5[0] == line6[0]:
        return True
    elif line4[1] == line5[1] == line6[1]:
        return True
    elif line4[2] == line5[2] == line6[2]:
        return True
    elif line4[0] == line5[1] == line6[2]:
        return True
    elif line4[2] == line5[1] == line6[0]:
        return True
    else:
        return False


# prints the board
while check_winner(line1, line2, line3) is False:
    print()
    print(f"{line1[0]} | {line1[1]} | {line1[2]}")
    print("——————————")
    print(f"{line2[0]} | {line2[1]} | {line2[2]}")
    print("——————————")
    print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    # asks the player where they want to place their symbol
    if TURNCOUNTER != 2:
        player1 = int(input("Player 1, where do you want to place an X? "))
        placex(player1)
        TURNCOUNTER += 1
    else:
        player2 = int(input("Player 2, where do you want to place an O? "))
        placeo(player2)
        TURNCOUNTER -= 1
print()
print(f"{line1[0]} | {line1[1]} | {line1[2]}")
print("——————————")
print(f"{line2[0]} | {line2[1]} | {line2[2]}")
print("——————————")
print(f"{line3[0]} | {line3[1]} | {line3[2]}")
if TURNCOUNTER == 2:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")


def printBoard(xState, zState):
    zero = {'X' if xState[0] else ('0' if zState[0]else 0)}
    one = {'X' if xState[1] else ('1' if zState[0]else 1)}
    tow = one = {'X' if xState[2] else ('2' if zState[0]else 2)}
    three = one = {'X' if xState[3] else ('3' if zState[0]else 3)}
    four = one = {'X' if xState[4] else ('4' if zState[0]else 4)}
    five = one = {'X' if xState[5] else ('5' if zState[0]else 5)}
    six = one = {'X' if xState[6] else ('6' if zState[0]else 6)}
    seven = one = {'X' if xState[7] else ('7' if zState[0]else 7)}
    eight = one = {'X' if xState[8] else ('8' if zState[0]else 8)}
    print(f"{zero} | {one} | {tow} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for X and 0 for O
    print("Welcome to ic Tac Toe")
    while():
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = input("Please enter a value ")
            xState(value) = 1
        else:
            print("X' Chance")
            value = int(input("Please enter a value"))
            zState(value) = 1



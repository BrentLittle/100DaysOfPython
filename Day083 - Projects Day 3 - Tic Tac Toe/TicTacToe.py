import os


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.turn = 0
        self.possibelToWin = False

    def updateTurn(self):
        self.turn += 1
        if self.turn >= 3:
            self.possibleToWin = True


class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def checkForWinner(self, location):
        return (
            self.checkVertical(location)
            or self.checkHorizontal(location)
            or self.checkDiagnal(location)
        )

    def checkVertical(self, location):
        columnNum = (location - 1) - (((location - 1) // 3) * 3)
        return (
            self.board[columnNum] == self.board[columnNum + 3]
            and self.board[columnNum + 3] == self.board[columnNum + 6]
        )

    def checkHorizontal(self, location):
        rowNum = (location - 1) // 3 * 3
        return (
            self.board[rowNum] == self.board[rowNum + 1]
            and self.board[rowNum + 1] == self.board[rowNum + 2]
        )

    def checkTLBRDiagonal(self):
        return self.board[0] == self.board[4] and self.board[4] == self.board[8]

    def checkTRBLDiagonal(self):
        return self.board[2] == self.board[4] and self.board[4] == self.board[6]

    def checkDiagnal(self, location):
        index = location - 1
        if index == 0 or index == 8:  # check the top left to bottom right diagonal
            return self.checkTLBRDiagonal()
        elif index == 2 or index == 6:  # check the top right to bottom left diagonal
            return self.checkTRBLDiagonal()
        elif index == 4:  # As this is the middle square we must check both diagonals
            return self.checkTLBRDiagonal() or self.checkTRBLDiagonal()
        else:  # the location was not one that we needed to check for a diagonal winning situation
            return False

    def updateCell(self, location, player):
        self.board[location - 1] = player.token
        player.updateTurn()

    def availableLocations(self):
        return [
            index + 1 for index in range(len(self.board)) if self.board[index] == " "
        ]

    def __str__(self):
        underscoreLine = "-----------"
        return (
            f" {self.board[0]} | {self.board[1]} | {self.board[2]} \n"
            + f"{underscoreLine}\n"
            + f" {self.board[3]} | {self.board[4]} | {self.board[5]} \n"
            + f"{underscoreLine}\n"
            + f" {self.board[6]} | {self.board[7]} | {self.board[8]} "
        )


def main():
    clearConsole()

    playerTurn = True  # True will be player 1's turn False will be Player Two's Turn

    board = Board()

    p1 = Player("Player 1", "X")
    p2 = Player("Player 2", "O")

    currentPlayer = None

    greeting()

    while True:
        # swap the player that needs to play for this turn
        if playerTurn:
            currentPlayer = p1
        else:
            currentPlayer = p2

        print(f"\nIt is {currentPlayer.name}'s Turn!")
        print(f"Current Board \n{board}\n")
        print(f"Reference Board")
        outputReferenceBoard()
        print(f"\nAvailable Moves: {availableLocations(board)}")

        playerSelection = 0
        while True:
            try:
                playerSelection = int(
                    input(
                        "Please select a location that is available to place your token at: "
                    )
                )
            except ValueError:
                print("Please enter one of the values that are available!")
                continue

            if playerSelection in board.availableLocations():
                break
            else:
                print("That is not a valid move as someone has already played there!")
                print("Please enter one of the values that are available!")
                continue

        board.updateCell(playerSelection, currentPlayer)

        if currentPlayer.turn >= 3 and board.checkForWinner(playerSelection):
            break

        playerTurn = not playerTurn
        clearConsole()

    announceWinner(currentPlayer)
    playAgain()


def playAgain():
    userInput = input("Would you like to play again? (Y/n):")
    if userInput == "Y" or userInput == "y":
        main()
    else:
        print("Thank You for playing")


def announceWinner(player):
    clearConsole()
    print(f"{player.name.upper()} WINS!!")


def greeting():
    print("Welcome to the Game of Tic Tac Toe!")
    print(
        "When Prompted please enter a location on the grid that you would like to place your token"
    )


def outputReferenceBoard():
    print(
        f" 1 | 2 | 3 \n"
        + f"-----------\n"
        + f" 4 | 5 | 6 \n"
        + f"-----------\n"
        + f" 7 | 8 | 9 "
    )


def availableLocations(board):
    output = ""
    for location in board.availableLocations():
        output += f"{location}, "
    return output[:-2]


def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()

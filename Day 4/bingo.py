from typing import List

def getData():

    inp = open("input.txt", "r")

    numbers = inp.readline().strip().split(",")

    for j in range(0, len(numbers)):
        numbers[j] = int(numbers[j])

    inp.readline()

    board = buildBoard()
    boards = [board]

    i = 0
    for line in inp:

        line = line.strip()

        if line == "":

            board = buildBoard()            
            boards.append(board)
            i = 0

        else:
            nums = line.split()
            for j in range(0, 5):
                board[i][j] = int(nums[j])
            i = i+1

    return [numbers, boards]

def buildBoard():
    board = []
    for i in range(0, 5):
        board.append([0]*5)

    return board

def buildCards(boards : List[List[List[int]]]) -> List[List[List[bool]]]:

    cards = []

    for board in boards:
        card = []
        for i in range(0, 5):
            card.append([False] * 5)

        cards.append(card)

    return cards


def checkCard(board: List[List[int]], card: List[List[bool]], val:int) -> bool:

    for i in range(0,5):
        for j in range(0, 5):

            if board[i][j] == val:
                card[i][j] = True
                
    return checkRows(card) or checkCols(card)

def checkRows(card: List[List[bool]]):

    for i in range(0, 5):
        win = True

        for j in range(0, 5):
            win = win and card[i][j]
        
        if win:
            return True

    return False

def checkCols(card: List[List[bool]]):

    for j in range(0, 5):
        win = True

        for i in range(0, 5):
            win = win and card[i][j]
        
        if win:
            return True

    return False

def tallyPoints(board: List[List[int]], card: List[List[bool]]) -> int:

    total = 0
    for i in range(0, 5):
        for j in range(0, 5):

            if not card[i][j]:
                total += board[i][j]

    print("Total: {}".format(total))

    return total


def playBingo(numbers: List[int], boards: List[List[List[int]]]) -> int:

    cards = buildCards(boards)

    for number in numbers:

        for i in range(0, len(boards)):

            if checkCard(boards[i], cards[i], number):

                print("Board {} won with {}.".format(i+1, number))

                return tallyPoints(boards[i], cards[i]) * number

def playSquidBingo(numbers: List[int], boards: List[List[List[int]]]) -> int:

    cards = buildCards(boards)
    finishedBoards = [False] * len(boards)

    wins = 0

    for number in numbers:

        for i in range(0, len(boards)):

            if finishedBoards[i]:
                continue

            elif checkCard(boards[i], cards[i], number):

                finishedBoards[i] = True
                wins = wins + 1

                if wins == len(boards):
                    print("Board {} won last with {}.".format(i+1, number))

                    return tallyPoints(boards[i], cards[i]) * number

                else:
                    print("Board {} finished with {}. Marking done.".format(i+1, number))

data = getData()
boards = data[1]
numbers = data[0]


for board in boards:
    for row in board:
        print(row)
    print()

print(playBingo(numbers, boards))
print(playSquidBingo(numbers, boards))

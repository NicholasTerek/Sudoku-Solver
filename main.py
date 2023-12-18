from typing import List, Tuple, Optional

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(board: List[List[int]]) -> bool:
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for number in range(1,10):
        if valid(board, number, (row, col)):
            board[row][col] = number
                        
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

def print_board(board: List[List[int]]) -> None:
    for row in range(len(board)):  
        if row % 3 ==0 and row != 0:
            print("- - - - - - - - - - - - - - -")

        for col in range(len(board[0])):
            if col % 3 ==0 and col != 0:
                print("|", end ="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end=" ")
    
    return None
               
def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col) 
    
    return None

def valid(board: List[List[int]], number: int, position: Tuple[int, int]) -> bool:
    
    for col in range(len(board[0])):
        if board[position[0]][col] == number and position[1] != col:
            return False
    for row in range(len(board[0])):
        if board[row][position[1]] == number and position[0] != row:
            return False
    box_x = position[1] // 3
    box_y = position[0] // 3

    for row in range(box_y *3, box_x *3 + 3):
        for col in range(box_x *3, box_y *3 +3):
            if board[row][col] == number and (row,col) != position:
                return False
    return True



print_board(board)
solve(board)
print("____________________")
print_board(board)

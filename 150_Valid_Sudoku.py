'''
Valid Sudoku
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ary=[]
        valid = True 

        for row in board:
            for i in row :
                ary.append(i)
        
         #check rows is valid numbers
        for i in range(0,9):
            #print(ary[i*9: (i*9)+9])
            row =ary[i*9: (i*9)+9]
            valid = self.validData(row)
            
            #if any row has invalid data then break the loop and return false
            if valid == False:
                return valid
                break
        
        #check column has valid numbers
        col_ary=[]
        
        for i  in range(0,9):
            for j in range(0,9):                
                col_ary.append(ary[i + j*9])

            #print(col_ary)
            valid = self.validData(col_ary)
            
            #if any row has invalid data then break the loop and return false
            if valid == False:
                return valid
                break    
            #resetting column ary
            col_ary=[]

        #extract row and column of 3 boxes each 
        box_ary=[]
        
        #version 1 , iterate first 3 horizontal boxes 
        # for i in range(0,9,3):
        #     for j in range(0,3):
        #       box_ary.append(i + j*9 )      
        #       box_ary.append(i + j*9 +1 )
        #       box_ary.append(i + j*9 +2 )
        #     print(box_ary)
        #     box_ary=[]

        for k in range(0,55,27):
            for i in range(0,9,3):
                for j in range(0,3):
                    # uncomment below code to check logic 
                    # box_ary.append(k+i +j*9 )      
                    # box_ary.append(k+i +j*9 +1 )
                    # box_ary.append(k+i +j*9 +2 )

                    box_ary.append(ary[k+i +j*9] )      
                    box_ary.append(ary[k+i +j*9 +1] )
                    box_ary.append(ary[k+i +j*9 +2] )
                print(box_ary)

                valid= self.validData(box_ary)
                if valid == False:
                    return False 

                box_ary=[]


        return valid
    
            

         
    def validData(self,ary) -> bool :
        #data = dict()
        data = []
        for val in ary:
            if val in data:
                return False
            else:
                if val != "." :
                    data.append(val)
        return True
    

        



obj= Solution()

board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]

validSudoku = obj.isValidSudoku(board)

#testrow = ["1","2",".",".","3",".",".","2","."]

#print(obj.validData(testrow))
print('valid sudoku', validSudoku)

# #invalid data in row 3
# board_row = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".","9",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# validSudoku = obj.isValidSudoku(board_row)
# print('invalid data in row 3 : valid sudoku', validSudoku)


        
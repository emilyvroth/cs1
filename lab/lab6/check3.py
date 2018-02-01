import string
import lab06_util as util

def okay_to_add(row_num,col_num,num):
	if row_num>8 or row_num<0 or col_num>8 or col_num<0 or num not in string.digits[1:10]:
		return False 
	for l in range(9):
		if bd[row_num][l] == num and l!=col_num:
			return False
		if bd[l][col_num] == num and l!=row_num:
			return False
	section_row=(row_num//3)*3
	section_col=(col_num//3)*3
	for m in range(section_row,section_row+3):
		for n in range(section_col,section_col+3):
			if bd[m][n] == num and m!=row_num and n!=col_num:
				return False
	return True

def num_not_there(row_num,col_num):
	if bd[row_num][col_num]=='.':
		return True
	return False

def verify_board(bd):
	for i in range(len(bd)):
		if '.' in bd[i]:
			return False
		for j in range(len(bd[i])):
			if not okay_to_add(i,j,bd[i][j]):
				return False
	return True

def print_board(bd):
	for i in range(len(bd)):
		if i%3==0:
			print("-"*(len(bd[i])*3+4))
		row=''
		for j in range(len(bd[i])):
			if j%3==0:
				row+="|"
			row+=" "+bd[i][j]+" "
		row+="|"
		print(row)
	print("-"*(len(bd[i])*3+4))


if __name__ == '__main__':

	file=input("Enter a file name: ")
	bd=util.read_sudoku(file)

	while not verify_board(bd):

		print_board(bd)

		row_num=int(input("row index to place value: "))
		col_num=int(input("column index to place a value: "))
		num=input("The value to place: ")

		if not okay_to_add(row_num,col_num,num):
			print("This number cannot be added")
			continue
		bd[row_num][col_num]=num
	print_board(bd)
	print("Congratulations, the puzzle is solved!")
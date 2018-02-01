import string
bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def okay_to_add(row_num,col_num,num):

	if row_num>8 or row_num<0 or col_num>8 or col_num<0 or num not in string.digits[1:10]:
		return False 
	for l in range(9):
		if bd[row_num][l] == num:
			return False
		if bd[l][col_num] == num:
			return False
	section_row=(row_num//3)*3
	section_col=(col_num//3)*3
	for m in range(section_row,section_row+3):
		for n in range(section_col,section_col+3):
			if bd[m][n] == num:
				return False
	return True

def num_not_there(row_num,col_num):
	if bd[row_num][col_num]=='.':
		return True
	return False

if __name__ == '__main__':
	while True:
	
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

		row_num=int(input("row index to place value: "))
		col_num=int(input("column index to place a value: "))
		num=input("The value to place: ")

		if not okay_to_add(row_num,col_num,num) or not num_not_there(row_num,col_num):
			print("This number cannot be added")
			continue
		bd[row_num][col_num]=num


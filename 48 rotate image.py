from pprint import pprint

matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16],
]

#the_len = len(matrix)
#matrix[1][2],matrix[2][1] = matrix[2][1],matrix[1][2]
#for i in range(0,the_len):
#	pprint(matrix[i])

def rotate(matrix):
	the_len = len(matrix);
	for i in range(the_len//2):
		matrix[i],matrix[the_len-1-i] = matrix[the_len-i-1],matrix[i]
		#print(matrix)

	for i in range(0,the_len):
		for j in range(i,the_len):
			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
			#matrix[i][j],matrix[j][the_len-1-i],matrix[the_len-1-i][the_len-1-j],matrix[the_len-1-j][i] \
			#= matrix[the_len-1-j][i],matrix[the_len-1-i][the_len-1-j],matrix[j][the_len-1-i],matrix[i][j]
			#matrix[i][j],matrix[j][the_len-i-1] = matrix[j][the_len-i-1],matrix[i][j]
			#pprint(matrix[i][j])
			

rotate(matrix)

print(matrix)
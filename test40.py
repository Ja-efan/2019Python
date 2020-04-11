# 07092019
# 09-09

def matrix_addition(*matrix_variables):
	return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]

matrix_y = [[2, 5], [2, 1]] # 이차원리스트 == 행렬
matrix_z = [[2, 4], [5, 3]]

print(matrix_addition(matrix_y, matrix_z))

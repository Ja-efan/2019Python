# 07092019
# 09-10


def vector_subtraction(*vector_variables):
	return [value[0] - sum(value[1:]) for value in zip(*vector_variables)]
    # sum(value[1:]) 은 1번째 value 부터 끝 까지 더해라

print(vector_subtraction([1, 3], [2, 4]))
print(vector_subtraction([1, 5], [10, 4], [4, 7]))

# 07092019
# 09-08


def scalar_vector_product(alpha, vector_variable):
    return [alpha * t for t in vector_variable]
    # alpha x t 를 할건데 t는 vector_variable에 있는 값들

print(scalar_vector_product(5,[1,2,3,4]))

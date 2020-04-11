def kwargs_test(**kwargs):
    print(kwargs)
    print("first calue is {first}".format(**kwargs))
    print("second calue is {second}".format(**kwargs))
    print("third calue is {third}".format(**kwargs))

kwargs_test(first=3,second=4,third=5)

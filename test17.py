def return_sen(sen,n):
    sen += str(n)
    n -= 1
    if n < 0:
        return sen
    else:
        return(return_sen(sen,n))

sentence = "i love you"
print(return_sen(sentence,5))

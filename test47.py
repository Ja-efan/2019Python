# 07102019
# (1) 기본 암호화 프로그램

def makeCodebook():
    decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m',\
			'*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}

    encbook = {}
    # 이 코드의 key code
    for k in decbook: # decbook의 키값과 val값을 서로 바꿈
        val = decbook[k]
        encbook[val] = k

    return encbook, decbook


def encrypt(msg, encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])
            print(msg)
    return  msg


def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])
            print(msg)
    return msg


if __name__ == '__main__': # __name__ 은 특별한 변 like 'main()'
    plaintext = 'I love you with all my heart'

    encbook, decbook = makeCodebook()
    ciphertext = encrypt(plaintext, encbook)
    print (ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print (deciphertext)

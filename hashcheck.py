# 07112019
# hash test

from Crypto.Hash import SHA256 as SHA
SIZE = 1024*256

def getFileHash(filename):
    hash = SHA.new()

    h = open(filename, 'rb')
    content = h.read(SIZE)
    while content:
        hash.update(content)
        hashval = hash.digest()
        content = h.read(SIZE)

		#각 파일의 hash value를 출력해 보자!

    h.close()

    return hashval

def hashCheck(file1, file2):
    hashval1 = getFileHash(file1)
    print("file1's hash: ",hashval1)
    hashval2 = getFileHash(file2)
    print("file2's hash: ",hashval2)

    if hashval1 == hashval2:
        print('Two Files are Same')
    else:
        print('Two Files are Different')

def main():
    file1 = 'plain.txt'
    file2 = 'plain.txt.enc.dec'

    hashCheck(file1, file2)

if __name__ == '__main__':
    main()

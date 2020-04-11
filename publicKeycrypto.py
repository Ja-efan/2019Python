# 07112019
# 개인키 공개키 생성 후 메시지 암호화

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypto(msg):
	privatekey = RSA.generate(1024)  #RSA.generate()를 이용하여 개인키 생성
	print("개인키: ",privatekey)

	encryptor = PKCS1_OAEP.new(privatekey) #참고 개인키로 메시지 암호화
	encrypted = encryptor.encrypt(msg)
	print(encrypted)


	publickey = privatekey.publickey() #private_key.publickey로 공개키 생성  => 공개키로 메시지 암호화
	print("공개키 : ",publickey)

	encryptor1 = PKCS1_OAEP.new(publickey) #참고 공개키로 메시지 암호화
	encrypted1 = encryptor.encrypt(msg)
	print(encrypted1)


if __name__ == '__main__':
	msg = 'chongju University'
	rsa_encrypto(msg.encode('utf-8'))

# message digest 5 (proffsor Rivest back 1991)
# 128 bit long sequence (hash or the message digest)
# sha2 # sha3 // better approches
# encode is used to convert the string to bytes -utf
from hashlib import md5
s = 'this is a message!' #b - byte
#result = md5(s) #define string
result = md5(s.encode())
#32 hexdecimal character
#hexdigest() returns a readable hexadecimal string, which is commonly used to display hashes.
#nibbles (we can store a hexadcimal character in 4 bits -0.5 byte)
#128/4=32
#print(result.digest())
#approach not collision free
print(result.hexdigest()) 

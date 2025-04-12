# message digest 5 (proffsor Rivest back 1991)
# 128 bit long sequence (hash or the message digest)
# sha2 # sha3 // better approches
from hashlib import md5
s = b'this is a message!' #b - byte
result = md5(s) #define string
#32 hexdecimal character
#nibbles (we can store a hexadcimal character in 4 bits -0.5 byte)
#128/4=32
print(result.digest())
#approach not collision free


from hashlib import sha256
#output is a 256 bits long sequence (message digest)
# bitcoin uses to generates hash
#64 charactrs long hexadecimal 
#256/4=64 
s='Just keep on shining like you do!'
s2 = 'Just keep on shining like you do'
result =sha256(s.encode())
result2=sha256(s2.encode())
#byte represetation of string
#encoding the string to bytes
print (result.digest())
print (result.hexdigest())
#64 hexadecimal string output
print (result2.digest())
print (result2.hexdigest())

#'avalache effect'


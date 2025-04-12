from hashlib import sha512
#output is a 512 bits long sequence (message digest)
# bitcoin uses to generates hash
#2^512=the number of possible hashes
#b/c of the birthday paradox -2^256
s='Just keep on shining like you do!'
s2 = 'Just keep on shining like you do'
result =sha512(s.encode())
result2=sha512(s2.encode())
#byte represetation of string
#encoding the string to bytes
print (result.digest())
print (result.hexdigest())
#64 hexadecimal string output
print (result2.digest())
print (result2.hexdigest())

#'avalache effect'


import hashlib
md5 = hashlib.md5()

md5.update(b'Python rocks!')
print (md5.digest())
# b'\x14\x82\xec\x1b#d\xf6N}\x16*+[\x16\xf4w'

md5 = hashlib.md5()
print (md5.hexdigest())
# 'd41d8cd98f00b204e9800998ecf8427e'

sha = hashlib.sha1(b'Hello Python').hexdigest()
print (sha)
#'422fbfbc67fe17c86642c5eaaa48f8b670cbed1b'


import binascii
dk = hashlib.pbkdf2_hmac(hash_name='sha256',
        password=b'bad_password34', 
        salt=b'bad_salt', 
        iterations=100000)
print (binascii.hexlify(dk))

# Here we create a SHA256 hash on a password using a lousy 
# salt but with 100,000 iterations. Of course, SHA is not 
# actually recommended for creating keys of passwords. 
# Instead you should use something like scrypt instead. 
# Another good option would be the 3rd party package, bcrypt. 
# It is designed specifically with password hashing in mind.
import hashlib
BLOCKSIZE = 65536
fileToOpen = 'test.txt'
hasher = hashlib.md5()
with open(fileToOpen, 'rb') as afile:
	buf = afile.read(BLOCKSIZE)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())

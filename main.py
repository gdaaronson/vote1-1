

import hashlib

def hashme(n):
	return hashlib.sha256(n).hexdigest()


def main():
	# 0-255
	VBidS = ['187', '42', '83', '154', '172', '52', '98', '250', '7', '23']

	VBidShash = []

	GOVsN = ['a83', 'a93j', 'a983', 'a93', 'a9d8', 'f83', 'f7r', 'ghw', '28dj', 'fi4']
	GOVsNhash = []

	print "VoteBox Info 1:"
	print VBidS

	print "Gov Info 1:"
	print GOVsN

	for each in VBidS:
		VBidShash.append(hashme(each))

	for each in GOVsN:
		GOVsNhash.append(hashme(each))


main()

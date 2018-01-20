#find_transformations.py
import sys

def tokenize(textFile):
	tokens = []
	with open(textFile) as infile:
		for line in infile:
			lines = line.split()
			if len(lines) > 0:	
				for i in lines:
					tokens.append(i)
			else:
				tokens.append('\n')
	print tokens
def findTrans(file1, file2):
	

def main():
	args = sys.argv
	if len(args) != 3:
		print "Usage: find_transformations.py file1.txt file2.txt"
		print "[!] Args: " + str(args)
		sys.exit(0)
	tokenizedFile1 = tokenize(args[1])
	tokenizedFile2 = tokenize(args[1])
	findTrans(tokenizedFile1,tokenizedFile2)

if __name__ ==  '__main__':
	main()
#1 edits out initital codon sequence in a file of gentic information
inputopen= open("input.txt")
inputread= inputopen.read()
print(inputread[15:400])
#create text file with output(how to rename multi line output within python from the command line)

codingopen= open("codinginput.txt")
codingread=codingopen.read()

for line in codingread:
    inputlength= len(codinginput)
    print(line + str(inputlength))

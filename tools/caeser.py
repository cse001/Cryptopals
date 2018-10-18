#The code that lists out all the possible outcomes of caeser cipher
#Uses prettytable - pip3 install prettytable
#Uses python 3
from prettytable import PrettyTable
def caeser(str,count):
    retval = ''
    for i in range(len(str)):
        char = str[i]
        asciivalue = ord(char)
        if (asciivalue >=65 and asciivalue<=90) :
            retval += chr((asciivalue-65+count)%26+65)
        else:
            if (asciivalue >=97 and asciivalue <=122):
                retval += chr((asciivalue-97+ count)%26 + 97)
            else:
                retval += char
    return retval
inputStr = input("Enter The String: ")
table = PrettyTable(['Key','Text'])
for i in range(26):
    table.add_row([i,caeser(inputStr,i)])
print(table)

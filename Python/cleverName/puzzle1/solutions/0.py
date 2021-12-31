# EXAMPLE SOLUTION

file = open('flag0.txt','r')

def char_jump(char1,char2,char3):
    char4 = file.read(1)
    eof = 0
    if not char4:
        eof = 1
    return char1,char2,char3,char4,eof;

def num_check(char1,char2,char3):
    if (ord(char1) >=48 and ord(char1) <=57):
        if (ord(char2) >=48 and ord(char2) <= 57):
            if (ord(char3) >=48 and ord(char3) <=57):
                return 1
    return 0

def main():

    char1 = file.read(1)
    char2 = file.read(1)
    char3 = file.read(1)
    char4 = file.read(1)
    result = ""

    while True:
    
        if not num_check(char1,char2,char3):
            char1,char2,char3,char4,eof = char_jump(char2,char3,char4)
            if eof:
                print(result)
                break
            continue
    
        if not (int(char1)%2):
            if (char2 == '3'):
                if (char3 == '9'):
                    result += char4

        char1,char2,char3,char4,eof = char_jump(char2,char3,char4)

        if eof:
            print(result)
            break

main()
file.close()

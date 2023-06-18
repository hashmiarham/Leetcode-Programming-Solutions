import random

def encode(s):
    if len(s) < 4:
        print(s[::-1])
    else:
        sc = ""
        cd = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        cdl = cd.split()
        for i in range(3):
            sc += random.choice(cdl)
        sc += s[1:] + s[0]
        for i in range(3):
            sc += random.choice(cdl)
        print(sc)

def decode(s):
    if len(s) < 4:
        print(s[::-1])
    else:
        c = ""
        n = s[3:-3]
        c = n[-1] + s[3:-4]
        print(c)

encode("arham")
decode("ghfafarzghf")

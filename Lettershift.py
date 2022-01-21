#Adding a function to add characters to the output string

def addstring(ADDChar):
    #A crude way of turning all the letters back into a string.

    try:
        retstring = newstring+ADDChar
    except:
        retstring=ADDChar
    return retstring

# Getting the string from the user

print("Insert string to shift")
strin = input()
strin = str(strin)

# Getting the shift amount from the user.

print("Insert shift amount")
shift = input()
try:
    shift = int(shift)
except: #  Set the shift to 0 if python doesn't recognise a shift amount.
    shift = 0
    print("Integer not detected. Defaulting to no shift.")

# Dictionary for capitalization and letters

Lettercaps = {
        "A":"cap",
        "B":"cap",
        "C":"cap",
        "D":"cap",
        "E":"cap",
        "F":"cap",
        "G":"cap",
        "H":"cap",
        "I":"cap",
        "J":"cap",
        "K":"cap",
        "L":"cap",
        "M":"cap",
        "N":"cap",
        "O":"cap",
        "P":"cap",
        "Q":"cap",
        "R":"cap",
        "S":"cap",
        "T":"cap",
        "U":"cap",
        "V":"cap",
        "W":"cap",
        "X":"cap",
        "Y":"cap",
        "Z":"cap",
        "a":"noc",
        "b":"noc",
        "c":"noc",
        "d":"noc",
        "e":"noc",
        "f":"noc",
        "g":"noc",
        "h":"noc",
        "i":"noc",
        "j":"noc",
        "k":"noc",
        "l":"noc",
        "m":"noc",
        "n":"noc",
        "o":"noc",
        "p":"noc",
        "q":"noc",
        "r":"noc",
        "s":"noc",
        "t":"noc",
        "u":"noc",
        "v":"noc",
        "w":"noc",
        "x":"noc",
        "y":"noc",
        "z":"noc"
        }

#Setting up the loop

for char in strin:

    if Lettercaps.get(char) == "cap":
        CCap = True
        LetterNumber = {
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,
            "Z":26
            }

#Setting up a dictionary.
    elif Lettercaps.get(char) == "noc":
        CCap = False
        LetterNumber = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,
            "i":9,
            "j":10,
            "k":11,
            "l":12,
            "m":13,
            "n":14,
            "o":15,
            "p":16,
            "q":17,
            "r":18,
            "s":19,
            "t":20,
            "u":21,
            "v":22,
            "w":23,
            "x":24,
            "y":25,
            "z":26
            }

# Else statement set up for Misc characters.
    else:
        newchar = char
        newstring = addstring(newchar)
        continue

    #Referencing the dictionary for a character
    num = LetterNumber.get(char)
    #Debug print
    #print(num)

    #add test

    num = num + shift

    #Setting up reverse dictionary
    if CCap == False:
        NumtoLet = {
            1:"a",
            2:"b",
            3:"c",
            4:"d",
            5:"e",
            6:"f",
            7:"g",
            8:"h",
            9:"i",
            10:"j",
            11:"k",
            12:"l",
            13:"m",
            14:"n",
            15:"o",
            16:"p",
            17:"q",
            18:"r",
            19:"s",
            20:"t",
            21:"u",
            22:"v",
            23:"w",
            24:"x",
            25:"y",
            26:"z"
            }
    if CCap == True:
        NumtoLet =  {
            1:"A",
            2:"B",
            3:"C",
            4:"D",
            5:"E",
            6:"F",
            7:"G",
            8:"H",
            9:"I",
            10:"J",
            11:"K",
            12:"L",
            13:"M",
            14:"N",
            15:"O",
            16:"P",
            17:"Q",
            18:"R",
            19:"S",
            20:"T",
            21:"U",
            22:"V",
            23:"W",
            24:"X",
            25:"Y",
            26:"Z"
            }

    # A rudimentary modulo function

    while True:
        if num > 26:
            num -= 26
        elif num < 1:
            num += 26
        else:
            break

    #convert back to letters
    newchar = NumtoLet.get(num)
    newstring = addstring(newchar)

    #debug print
    #print(newchar)

print("The resulting shifted string is:")
print(newstring)

# I uploaded this to Github.

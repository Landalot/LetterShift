# Getting the string from the user

strin = input()
strin = str(strin)

#Setting up the loop

for char in strin:

    if char == "A" or char == "B" or char == "C" or char == "D" or char == "E" or char == "F" or char == "G" or char == "H" or char == "I" or char == "J" or char == "K" or char == "L" or char == "M" or char == "N" or char == "O" or char == "P" or char == "Q" or char == "R" or char == "S" or char == "T" or char == "U" or char == "V" or char == "W" or char == "X" or char == "Y" or char == "Z":
        print("This is a cap")
        continue

#Setting up a dictionary.

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
        "z":26,
        }

    #Referencing the dictionary for a character
    num = LetterNumber.get(char)
    #Debug print
    #print(num)

    #add test

    num = num + 2

    #Setting up reverse dictionary
    NumtoLet = LetterNumber = {
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
        26:"z",
        }

    #convert back to letters

    try:
        newchar = NumtoLet.get(num)
        if newchar == None:
            newchar = "?"
    except:
        newchar = "?"

    #debug print
    #print(newchar)

    #A crude way of turning all the letters back into a string.

    try:
        newstring = newstring+newchar
    except:
        newstring=newchar

print(newstring)
